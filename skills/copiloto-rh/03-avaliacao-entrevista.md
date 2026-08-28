# Módulo 3 — Transcrição da entrevista → avaliação

**Entrada:** transcrição ou notas da entrevista + `vaga.json` + a matriz de evidência do
candidato, se existir.

**Saída:** avaliação por critério ancorada em trechos literais, contradições, desafio
técnico derivado das lacunas e briefing para o comitê.

---

## Peça 1 — Avaliação por critério

Um bloco por critério. Nunca some numa nota final (ver `rubricas.md` seção 5).

```
### c2 — Autonomia na definição do problema
**Resultado:** ATENDE

**Trechos:**
> "eles pediram um relatório de churn, mas eu percebi que a pergunta real era outra,
> então voltei e perguntei o que iam fazer com o número" (entrevista, bloco Núcleo)

**Leitura:** demonstrou reformular a demanda antes de executar — comportamento de pleno
segundo a rubrica. Trouxe o exemplo espontaneamente, sem sondagem.

**O que ainda não sabemos:** se isso se repete quando a área discorda. Não perguntamos.
```

Campos obrigatórios em cada bloco: **Resultado**, **Trechos** (literais, com localização),
**Leitura** (marcada como leitura), **O que ainda não sabemos**.

Se um critério `ESSENCIAL` ficou `NÃO_DEMONSTRADO`, escreva explicitamente:

> `NÃO_DEMONSTRADO — falha do roteiro, não do candidato. A pergunta X não foi feita.`

---

## Peça 2 — Contradições e sinais fracos

Duas listas separadas, e a distinção entre elas importa:

**Contradições** — divergência factual entre fontes. Sempre vira pergunta neutra:

```
CV diz: "liderei equipe de 4 pessoas"
Entrevista diz: "a gente era em 4, mas quem coordenava era o Rafael"
Pergunta: "me ajuda a entender como funcionava a divisão de papéis nesse time?"
```

**Sinais fracos** — coisas que chamaram atenção mas não sustentam conclusão. Cada um com o
aviso de que é sinal fraco e a pergunta que confirmaria ou derrubaria.

```
Sinal fraco: usou "a gente" em todos os exemplos técnicos, "eu" só nos administrativos.
Isso NÃO é conclusão — pode ser cultura de time ou modéstia.
Pergunta: "nesse projeto, qual parte foi você que escreveu?"
```

**Nunca** liste um sinal fraco sem a pergunta correspondente. Sinal fraco sem pergunta
vira preconceito com aparência de análise.

---

## Peça 3 — `avaliacao.json`

Siga `../../schemas/avaliacao.schema.json`.

> **Convenção:** nos textos escreva com acento (`NÃO_DEMONSTRADO`, `PREOCUPAÇÃO`).
> **Dentro do JSON, sempre sem acento** (`NAO_DEMONSTRADO`, `PREOCUPACAO`) — é o que o
> schema aceita.

```json
{
  "vaga_id": "",
  "candidato_id": "",
  "data_entrevista": "AAAA-MM-DD",
  "entrevistadores": [""],
  "resultados": [
    {
      "criterio_id": "c1",
      "resultado": "SUPERA | ATENDE | NAO_DEMONSTRADO | PREOCUPACAO",
      "trechos": [{ "citacao": "", "localizacao": "" }],
      "leitura": "",
      "nao_sabemos": ""
    }
  ],
  "contradicoes": [{ "fonte_a": "", "fonte_b": "", "pergunta": "" }],
  "sinais_fracos": [{ "sinal": "", "pergunta": "", "aviso": "sinal fraco, não conclusão" }],
  "gaps_para_onboarding": [
    { "criterio_id": "", "descricao": "", "sugestao_trilha": "" }
  ],
  "proxima_etapa_sugerida": "",
  "decisao": null,
  "decidido_por": null
}
```

`decisao` e `decidido_por` ficam `null`. **Você nunca preenche esses dois campos.** Eles
existem para a pessoa preencher no sistema, e é isso que torna a decisão rastreável.

`gaps_para_onboarding` é a ponte para o Módulo 4 — todo `NÃO_DEMONSTRADO` e todo `INDÍCIO`
que sobreviveu à entrevista entra aqui.

---

## Peça 4 — Desafio técnico

Só gere se houver lacuna que a conversa não fechou. Se não houver, diga: "não recomendo
desafio técnico — as lacunas restantes se resolvem em 20 minutos de conversa, e desafio
custa horas do candidato."

Regras em `rubricas.md` seção 6. Formato do enunciado:

```
## Desafio: <título>
**Tempo estimado:** X horas (teto real, não "sugestão")
**Prazo de entrega:** X dias
**Por que este desafio:** <a lacuna que ele fecha — o candidato tem direito de saber>

### Contexto
<situação realista, dados fictícios, sem trabalho aproveitável pela empresa>

### O que entregar

### Como será avaliado
| Critério | O que buscamos |

### Alternativa
Se você não puder dedicar essas horas, oferecemos conversa técnica de 60 min sobre um
projeto seu já existente. As duas opções valem igual no processo.
```

A alternativa não é gentileza. É correção de viés: desafio de 4 horas seleciona quem tem
4 horas livres, não quem é melhor.

---

## Peça 5 — Briefing do comitê

Uma página. Estrutura:

1. **A vaga em duas linhas** — problema a resolver, não descrição de cargo
2. **O que a entrevista mostrou** — por critério, uma linha cada, com o resultado
3. **O que continua em aberto** — o que não sabemos e o que responderia
4. **Próxima etapa sugerida** — com o que ela resolveria
5. **A decisão é de vocês** — o que precisa ser decidido, por quem, e com que informação

Ao final, sempre:

> Este documento contém dado pessoal de candidato. Compartilhe apenas com quem participa
> da decisão e observe o prazo de retenção definido pela empresa.

---

## Fechamento obrigatório

```
## O QUE FALTA VERIFICAR
## DECISÃO HUMANA NECESSÁRIA
```
