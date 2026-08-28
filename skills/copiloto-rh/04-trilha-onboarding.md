# Módulo 4 — Contratado + função + data de início → trilha de onboarding

**Entrada mínima:** nome, função e data de início.
**Entrada ideal:** o `vaga.json` da vaga que ele preencheu + o `avaliacao.json` dele + a
ficha da função.

**Saída:** `trilha_onboarding.json` + a leitura humana da trilha + a mensagem de
boas-vindas.

---

## A ligação com o recrutamento

Este é o ponto central do módulo, e é o que diferencia uma trilha gerada por IA de um
checklist de template:

> **Os gaps que apareceram na avaliação viram os primeiros itens da trilha.**

Cada `gaps_para_onboarding` do `avaliacao.json` vira um item com `origem` apontando para o
critério. Se um candidato entrou com `INDÍCIO` em modelagem dimensional, a trilha dele tem
um item de modelagem que a trilha de outra pessoa na mesma função não tem.

Trilha igual para todo mundo na mesma função é trilha que ignora a pessoa que você acabou
de contratar — e você tem, no `avaliacao.json`, exatamente a informação para personalizar.

Se não houver `avaliacao.json`, gere a trilha padrão da função e escreva:

> `Trilha genérica da função. Com o resultado da avaliação da pessoa, ela pode ser
> personalizada — pergunte se está disponível.`

---

## Estrutura: 5 blocos

Ver `rubricas.md` seção 7. Prazos **sempre relativos à data de início** e também
calculados em data absoluta, pulando fim de semana.

| Bloco | Janela |
|---|---|
| `PRE_INICIO` | D-5 a D-1 |
| `DIA_1` | D+0 |
| `SEMANA_1` | D+1 a D+5 |
| `DIAS_30` | D+6 a D+30 |
| `DIAS_90` | D+31 a D+90 |

---

## `trilha_onboarding.json`

Siga `../../schemas/trilha_onboarding.schema.json`:

```json
{
  "colaborador": { "nome": "", "funcao": "", "area": "", "gestor": "", "data_inicio": "AAAA-MM-DD" },
  "vaga_id": "",
  "blocos": [
    {
      "bloco": "PRE_INICIO",
      "itens": [
        {
          "item_id": "pre-01",
          "titulo": "",
          "descricao": "",
          "tipo": "ACESSO | PESSOA | CONTEUDO | ENTREGA | ADMINISTRATIVO",
          "dono": "quem executa — cargo ou área, nunca 'RH' genérico",
          "prazo_relativo": "D-3",
          "prazo_absoluto": "AAAA-MM-DD",
          "criterio_concluido": "observável, verificável por terceiro",
          "origem": null,
          "notifica_slack": true,
          "canal_slack": "#onboarding-dados",
          "bloqueia": ["dia1-02"]
        }
      ]
    }
  ],
  "pessoas_chave": [
    { "nome": "", "papel": "", "por_que_falar": "", "quando": "SEMANA_1" }
  ],
  "acessos_necessarios": [
    { "sistema": "", "nivel": "", "solicitar_para": "", "prazo": "D-3" }
  ],
  "marcos_de_acompanhamento": [
    { "quando": "D+30", "com_quem": "gestor", "pauta": "" }
  ]
}
```

---

## Regras de geração

**Dono.** Nunca "RH" ou "o time". Sempre um papel específico: "gestor direto",
"TI — service desk", "buddy designado". Item sem dono é item que não acontece.

**Critério de concluído.** Observável e verificável por terceiro. "Participou do
treinamento" é presença; "explicou X para o gestor em 5 minutos" é resultado. Ver a tabela
de errado vs. certo em `rubricas.md` seção 7.

**Dependências.** Use `bloqueia` para deixar explícito o que trava. O clássico: acesso não
liberado em D-3 trava a primeira tarefa real do D+1. Explicitar isso é metade do valor
da trilha.

**Notificação.** Marque `notifica_slack: true` nos itens em que alguém precisa **agir** se
não acontecer. Se tudo notifica, ninguém lê. Regra prática: no máximo 1 notificação por
bloco, mais os marcos.

**Primeira entrega real.** Todo `SEMANA_1` tem pelo menos uma entrega de verdade, por
menor que seja. Onboarding só com conteúdo e reunião produz uma pessoa que na segunda
semana ainda não sabe se está indo bem.

**Volume.** 4 a 8 itens por bloco. Trilha com 40 itens não é acompanhada — vira teatro.

---

## Peça 2 — Leitura humana

Depois do JSON, a tabela para a pessoa:

| Quando | O quê | Quem | Concluído quando |
|---|---|---|---|
| Ter 02/09 (D-3) | Criar acessos: e-mail, VPN, banco leitura | TI — service desk | Colaborador loga nos três |

Destaque, em bloco separado, os itens que vieram da avaliação:

> **Personalizado a partir da entrevista:** 3 itens desta trilha nasceram de lacunas
> identificadas na avaliação de <nome> (critérios c1 e c4). Estão marcados com `origem`.

---

## Peça 3 — Mensagem de boas-vindas

Curta, humana, enviada em D-2. Diz: onde chegar e a que horas, quem recebe, o que levar,
como será o primeiro dia e para quem escrever se algo der errado. **Sem jargão corporativo
e sem "estamos muito animados com sua chegada"** — diga o que a pessoa precisa saber para
não ficar perdida.

---

## Fechamento obrigatório

```
## O QUE FALTA VERIFICAR
## DECISÃO HUMANA NECESSÁRIA
```

Típicos aqui: quem será o buddy, se o equipamento chega a tempo, se o acesso ao sistema
crítico depende de aprovação que leva mais que o prazo previsto.
