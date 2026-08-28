"""Valida os blocos JSON dos arquivos de gabarito/ contra os schemas de schemas/.

Uso:  python app/validar-gabarito.py   (rodar da raiz do projeto)

Serve para dois momentos:
  1. Ao preparar a palestra, conferindo que o gabarito bate com o contrato.
  2. Durante a palestra, se alguem quiser validar a propria saida: salve o JSON
     gerado num arquivo e rode `python app/validar-gabarito.py caminho.json vaga`.

Requer jsonschema (`pip install jsonschema`). Sem ele, valida apenas o parse.
"""

import io
import json
import os
import re
import sys

try:
    import jsonschema
    TEM_JSONSCHEMA = True
except ImportError:
    TEM_JSONSCHEMA = False

# (arquivo de gabarito, schema, chave que identifica o bloco certo)
ALVOS = [
    ('gabarito/01-vaga.md', 'schemas/vaga.schema.json', 'vaga_id'),
    ('gabarito/02-matriz-evidencia.md', 'schemas/matriz_evidencia.schema.json', 'candidatos'),
    ('gabarito/04-avaliacao.md', 'schemas/avaliacao.schema.json', 'resultados'),
    ('gabarito/05-trilha-onboarding.md', 'schemas/trilha_onboarding.schema.json', 'blocos'),
]

SCHEMA_POR_NOME = {
    'vaga': 'schemas/vaga.schema.json',
    'matriz': 'schemas/matriz_evidencia.schema.json',
    'avaliacao': 'schemas/avaliacao.schema.json',
    'trilha': 'schemas/trilha_onboarding.schema.json',
}


def validar(obj, caminho_schema, rotulo):
    """Retorna True se valido. Imprime os erros encontrados."""
    if not TEM_JSONSCHEMA:
        print('parse OK  %s  (instale jsonschema para validar o contrato)' % rotulo)
        return True

    schema = json.load(io.open(caminho_schema, encoding='utf-8'))
    erros = sorted(
        jsonschema.Draft7Validator(schema).iter_errors(obj),
        key=lambda e: list(e.path),
    )
    if not erros:
        print('VALIDO    %s  ->  %s' % (rotulo, caminho_schema))
        return True

    print('INVALIDO  %s  (%d erro(s))' % (rotulo, len(erros)))
    for erro in erros[:8]:
        caminho = '/'.join(str(p) for p in erro.absolute_path) or '(raiz)'
        print('   em %s' % caminho)
        print('      %s' % erro.message[:200])
    if len(erros) > 8:
        print('   ... e mais %d' % (len(erros) - 8))
    return False


def extrair_blocos_json(caminho_md, chave):
    """Devolve o ultimo bloco ```json do arquivo que contenha `chave` na raiz."""
    texto = io.open(caminho_md, encoding='utf-8').read()
    encontrado = None
    for bloco in re.findall(r'```json\n(.*?)\n```', texto, re.S):
        try:
            obj = json.loads(bloco)
        except ValueError as e:
            print('PARSE FALHOU em %s: %s' % (caminho_md, e))
            continue
        if isinstance(obj, dict) and chave in obj:
            encontrado = obj
    return encontrado


def modo_arquivo_unico(caminho, nome_schema):
    if nome_schema not in SCHEMA_POR_NOME:
        print('Schema desconhecido: %s' % nome_schema)
        print('Use um destes: %s' % ', '.join(sorted(SCHEMA_POR_NOME)))
        return 1
    obj = json.load(io.open(caminho, encoding='utf-8'))
    ok = validar(obj, SCHEMA_POR_NOME[nome_schema], caminho)
    return 0 if ok else 1


def modo_gabarito():
    falhas = 0
    for md, schema, chave in ALVOS:
        if not os.path.exists(md):
            print('AUSENTE   %s' % md)
            falhas += 1
            continue
        obj = extrair_blocos_json(md, chave)
        if obj is None:
            print('SEM BLOCO %s (nenhum JSON com a chave "%s")' % (md, chave))
            falhas += 1
            continue
        if not validar(obj, schema, md):
            falhas += 1

    print('')
    print('TODOS VALIDOS' if falhas == 0 else '%d PROBLEMA(S)' % falhas)
    return 0 if falhas == 0 else 1


if __name__ == '__main__':
    if len(sys.argv) == 3:
        sys.exit(modo_arquivo_unico(sys.argv[1], sys.argv[2]))
    if len(sys.argv) == 1:
        sys.exit(modo_gabarito())
    print(__doc__)
    sys.exit(2)
