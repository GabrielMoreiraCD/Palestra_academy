"""Gera os arquivos de colagem da skill, a partir de skill/copiloto-rh/.

Uso:  python app/gerar-colar-no-chat.py   (rodar da raiz do projeto)

Produz DOIS arquivos:

  COLAR-NO-CHAT.md        base leve (SKILL + guardrails + rubricas), ~19 mil caracteres.
                          E o caminho PADRAO da palestra. Cada modulo e colado depois,
                          no passo em que for usado, direto do arquivo dele.

  COLAR-NO-CHAT-TUDO.md   skill inteira num texto so, ~37 mil caracteres. Use quando
                          nao houver limite de uso apertado e voce quiser colar uma vez so.

Por que a versao leve e o padrao: em conta gratuita, colar 37 mil caracteres e depois
mandar 3 curriculos e uma transcricao de 251 linhas estoura o limite antes do fim da
sessao. A versao leve corta a base pela metade e carrega cada modulo so quando precisa.

Sempre que editar algo em skill/copiloto-rh/, rode isto de novo.
"""

import io
import os

BASE = os.path.join('skill', 'copiloto-rh')

# Base comum: vale para os quatro modulos, sempre necessaria.
NUCLEO = [
    ('SKILL.md', None),
    ('guardrails.md', 'ANEXO A'),
    ('rubricas.md', 'ANEXO B'),
]

# Modulos: colados um a um, no passo em que sao usados.
MODULOS = [
    ('01-perfil-de-vaga.md', 'ANEXO C'),
    ('02-matriz-de-evidencia.md', 'ANEXO D'),
    ('03-avaliacao-entrevista.md', 'ANEXO E'),
    ('04-trilha-onboarding.md', 'ANEXO F'),
]

CABECALHO_LEVE = """# COPILOTO DE RH — base para colar no chat

> Copie TUDO deste arquivo e cole como primeira mensagem de uma conversa nova.
> Isto e a base do copiloto: identidade, regras de conduta e rubricas.
>
> Os quatro modulos (perfil de vaga, matriz de evidencia, avaliacao, trilha) NAO estao
> aqui. Cada um e colado no passo em que voce for usa-lo, seguindo o GUIA_AO_VIVO.md.
> Isso economiza limite de uso em conta gratuita.
>
> Se preferir colar tudo de uma vez: use `COLAR-NO-CHAT-TUDO.md`.
>
> Gerado a partir de `skill/copiloto-rh/`. Nao edite este arquivo:
> edite os originais e rode `python app/gerar-colar-no-chat.py`.

---

"""

CABECALHO_TUDO = """# COPILOTO DE RH — arquivo unico, skill completa

> A skill inteira em um so texto, com os quatro modulos. Copie TUDO daqui e cole como
> primeira mensagem da conversa. Depois disso, mande o briefing, os curriculos ou a
> transcricao.
>
> Sao ~37 mil caracteres. Em conta gratuita isso consome bastante do seu limite: se voce
> for rodar a palestra inteira, prefira `COLAR-NO-CHAT.md` (base leve) e cole cada modulo
> no passo em que ele for usado.
>
> Gerado a partir de `skill/copiloto-rh/`. Nao edite este arquivo:
> edite os originais e rode `python app/gerar-colar-no-chat.py`.

---

"""

MAPA_ANEXOS = {
    'guardrails.md': 'ANEXO A',
    'rubricas.md': 'ANEXO B',
    '01-perfil-de-vaga.md': 'ANEXO C',
    '02-matriz-de-evidencia.md': 'ANEXO D',
    '03-avaliacao-entrevista.md': 'ANEXO E',
    '04-trilha-onboarding.md': 'ANEXO F',
}


def remover_frontmatter(texto):
    """Tira o bloco YAML --- ... --- do inicio do SKILL.md."""
    if not texto.startswith('---'):
        return texto
    fim = texto.find('\n---', 3)
    if fim == -1:
        return texto
    return texto[fim + 4:].lstrip('\n')


def montar(cabecalho, secoes, presentes):
    """Junta cabecalho + secoes num texto unico, resolvendo os links entre arquivos."""
    partes = [cabecalho]
    for nome, rotulo in secoes:
        texto = io.open(os.path.join(BASE, nome), encoding='utf-8').read()
        if rotulo is None:
            texto = remover_frontmatter(texto)
        else:
            partes.append('\n\n---\n\n# %s — %s\n\n' % (rotulo, nome))
        partes.append(texto)

    saida = ''.join(partes)

    # Links entre arquivos nao funcionam num texto unico.
    for arquivo, anexo in MAPA_ANEXOS.items():
        if arquivo in presentes:
            alvo_link = '%s (%s, abaixo neste mesmo texto)' % (anexo, arquivo)
            alvo_cod = '`%s` (%s)' % (arquivo, anexo)
        else:
            alvo_link = ('%s — nao esta neste texto; cole o arquivo %s quando o guia '
                         'mandar' % (anexo, arquivo))
            alvo_cod = '`%s` (cole quando o guia mandar)' % arquivo
        saida = saida.replace('[%s](%s)' % (arquivo, arquivo), alvo_link)
        saida = saida.replace('`%s`' % arquivo, alvo_cod)

    return saida.replace('../../schemas/', 'schemas/')


def gravar(nome_arquivo, conteudo):
    destino = os.path.join(BASE, nome_arquivo)
    io.open(destino, 'w', encoding='utf-8', newline='').write(conteudo)
    print('gerado: %-24s  linhas: %4d  caracteres: %6d'
          % (destino, conteudo.count('\n'), len(conteudo)))


def main():
    nomes_nucleo = {n for n, _ in NUCLEO}
    nomes_todos = {n for n, _ in NUCLEO + MODULOS}

    gravar('COLAR-NO-CHAT.md', montar(CABECALHO_LEVE, NUCLEO, nomes_nucleo))
    gravar('COLAR-NO-CHAT-TUDO.md', montar(CABECALHO_TUDO, NUCLEO + MODULOS, nomes_todos))


if __name__ == '__main__':
    main()
