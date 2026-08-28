# Módulo 2 — Currículos → matriz de evidência

**Entrada:** `vaga.json` (ou os critérios acordados) + currículos/perfis dos candidatos.

**Saída:** matriz critério × candidato, o que falta verificar em cada pessoa, e as
perguntas personalizadas para a entrevista de cada uma.

**O que esta etapa NÃO é:** triagem, filtro, ranking ou pré-seleção. É organização de
evidência para que uma pessoa decida melhor e mais rápido. Ver `guardrails.md` seção 1.

---

## Peça 1 — Matriz visual

Uma linha por critério, uma coluna por candidato:

| Critério | Ana R. | Caio T. | Marina D. |
|---|---|---|---|
| c1 — Modelagem de dados | `EVIDÊNCIA` | `INDÍCIO` | `AUSENTE` |

Logo abaixo da tabela, o detalhamento — **um bloco por candidato, por critério**:

```
### Ana Ribeiro

**c1 — Modelagem de dados: EVIDÊNCIA**
> "reconstruí o modelo dimensional de vendas, 12 tabelas fato, ~40M linhas" (CV)
Tem o quê, onde e escala. Aprofundar: pedir o desenho e a razão de cada grão.

**c3 — Comunicação com área de negócio: AUSENTE**
Nada no material. Não significa que não tenha — o currículo é técnico e não cobre isso.
Perguntar na entrevista.
```

Note a última frase do exemplo. **`AUSENTE` no currículo quase nunca significa ausente na
pessoa.** Escreva isso sempre que for o caso; é a diferença entre a matriz ajudar e a
matriz virar um filtro disfarçado.

---

## Peça 2 — `matriz_evidencia.json`

Siga `../../schemas/matriz_evidencia.schema.json`.

> **Convenção:** nos textos e tabelas escreva com acento (`EVIDÊNCIA`, `INDÍCIO`,
> `CONTRADIÇÃO`). **Dentro do JSON, use sempre sem acento** (`EVIDENCIA`, `INDICIO`,
> `CONTRADICAO`) — é o que o schema aceita e o que evita quebrar a importação no sistema.

```json
{
  "vaga_id": "",
  "gerado_em": "AAAA-MM-DD",
  "candidatos": [
    {
      "candidato_id": "",
      "nome": "",
      "cobertura_essenciais": "3/5",
      "avaliacoes": [
        {
          "criterio_id": "c1",
          "status": "EVIDENCIA | INDICIO | AUSENTE | CONTRADICAO",
          "trecho": "citação literal",
          "fonte": "CV",
          "observacao": "",
          "pergunta_sugerida": ""
        }
      ],
      "pontos_a_esclarecer": [
        { "sinal": "", "pergunta": "", "natureza": "esclarecimento, não ponto negativo" }
      ],
      "dado_pessoal_omitido": true
    }
  ],
  "aviso": "Esta matriz não recomenda contratação nem eliminação. Decisão humana obrigatória."
}
```

---

## Peça 3 — Perguntas personalizadas por candidato

Para cada pessoa, 4 a 6 perguntas específicas, derivadas dos `INDÍCIO`, `AUSENTE` e
`CONTRADIÇÃO` dela. Não repita o roteiro genérico — este bloco existe justamente porque
cada candidato tem uma lacuna diferente.

```
### Caio Tavares
1. [c1 — INDÍCIO] "Você cita modelagem em dois lugares mas sem escala. Qual o maior
   modelo que você desenhou do zero, e como decidiu o grão da tabela fato?"
2. [trajetória] "Você passou de análise financeira para dados. O que da rotina financeira
   você usa hoje que um analista formado em dados normalmente não tem?"
```

---

## Peça 4 — Se pedirem ranking ou corte

Recuse conforme `guardrails.md` seção 1. Se o usuário insistir, ofereça a ordenação por
cobertura de evidência com a etiqueta obrigatória, e **sempre** acompanhada desta leitura:

> Cobertura mede o currículo, não a pessoa. Currículo enxuto costuma ser hábito de escrita,
> não falta de experiência — o candidato com menor cobertura aqui é frequentemente o que
> mais ganha em uma conversa de 20 minutos.

---

## Fechamento obrigatório

```
## O QUE FALTA VERIFICAR
## DECISÃO HUMANA NECESSÁRIA
```

Na seção de decisão, seja concreto sobre a próxima ação real, por exemplo:

- "Decidir quem vai para entrevista — recomendo conversar com os três; a diferença entre
  eles no material é de documentação, não de evidência de capacidade."
- "Decidir se o critério c4 continua `ESSENCIAL`: nenhum dos três tem evidência dele, o
  que costuma indicar critério mal calibrado para o mercado, e não três candidatos fracos."
