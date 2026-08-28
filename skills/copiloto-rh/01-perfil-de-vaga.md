# Módulo 1 — Briefing do gestor → perfil de vaga

**Entrada:** qualquer coisa que o gestor mandou. Áudio transcrito, mensagem de WhatsApp,
e-mail de três linhas, conversa de corredor anotada. Normalmente bagunçado, incompleto e
com desejos misturados a requisitos. Isso é o normal, não é problema.

**Saída:** quatro peças, nesta ordem.

---

## Peça 1 — Leitura do briefing

Antes de qualquer coisa, devolva o que você entendeu, separando três colunas:

| O gestor disse | Tipo | Como isso vira critério |
|---|---|---|
| trecho literal do briefing | `REQUISITO` / `DESEJO` / `SINTOMA` / `NÃO_UTILIZÁVEL` | o critério observável correspondente |

- `REQUISITO` — competência ou condição concreta
- `DESEJO` — preferência sem definição observável ainda ("proativo", "mão na massa")
- `SINTOMA` — descrição de dor, não de perfil ("o time tá afogado", "sempre atrasa")
- `NÃO_UTILIZÁVEL` — característica protegida ou proxy (ver `guardrails.md` seção 4).
  Não incorpore. Escreva o motivo e proponha o equivalente observável.

**`SINTOMA` é a peça mais valiosa do briefing.** "O time tá afogado com pedido de relatório"
não descreve uma pessoa — descreve o problema que a contratação precisa resolver. Traduza
para o comportamento que resolve aquilo, e mostre a tradução.

---

## Peça 2 — `vaga.json`

Siga `../../schemas/vaga.schema.json`. Estrutura:

```json
{
  "vaga_id": "kebab-case-do-titulo",
  "titulo": "",
  "area": "",
  "gestor": "",
  "senioridade": "junior | pleno | senior",
  "problema_a_resolver": "1-2 frases, vindas dos SINTOMAS do briefing",
  "entregas_esperadas_90_dias": ["", ""],
  "criterios": [
    {
      "id": "c1",
      "nome": "",
      "tipo": "OBRIGATORIO_OBJETIVO | ESSENCIAL | IMPORTANTE | DESEJAVEL",
      "comportamento_observavel": "o que a pessoa faz quando tem isso",
      "como_verificar": "pergunta de entrevista, exercício, ou pedido de exemplo",
      "origem_briefing": "trecho literal que gerou este critério, ou 'inferido — confirmar'"
    }
  ],
  "criterios_recusados": [
    { "texto_original": "", "motivo": "", "alternativa_proposta": "" }
  ],
  "faixa_salarial": null,
  "modelo_trabalho": null,
  "lacunas_do_briefing": [""]
}
```

Regras:

- Máximo **5** critérios `ESSENCIAL`. Se o briefing sugerir mais, escolha os 5 mais
  ligados ao `problema_a_resolver`, mova o resto para `IMPORTANTE` e **diga que fez isso**.
- Todo critério tem `comportamento_observavel`. "Conhecimento em SQL" não é comportamento.
  "Escreve consulta com junção e agregação sobre tabela que nunca viu, e explica o
  resultado" é.
- Campo que o briefing não informou fica `null`. **Nunca preencha por conta própria.**
- `origem_briefing` é obrigatório. Critério que você inferiu recebe `"inferido — confirmar"`.
  Isso deixa visível o que é do gestor e o que é seu.

---

## Peça 3 — Roteiro de entrevista

Estrutura fixa, 50 minutos:

| Bloco | Tempo | Conteúdo |
|---|---|---|
| Abertura | 5 min | Contexto da vaga e do problema. Como a conversa vai funcionar. |
| Trajetória | 10 min | Linha do tempo, com as perguntas de esclarecimento das lacunas |
| Núcleo | 25 min | 2 a 3 perguntas por critério `ESSENCIAL`, em profundidade |
| Perguntas da pessoa | 7 min | O que ela pergunta é sinal — registre |
| Fechamento | 3 min | Próximos passos e prazo, com data |

Cada pergunta do núcleo vem em trio:

```
Critério: <id + nome>
Pergunta: <aberta, sobre situação real vivida — nunca hipotética>
Sondagem: <a pergunta seguinte, que separa "eu fiz" de "meu time fez">
Sinal de que atende: <o que aparece na resposta de quem realmente tem isso>
```

Proibido: pergunta hipotética ("o que você faria se..."), pergunta de personalidade
("qual seu maior defeito"), quebra-cabeça, e qualquer pergunta sobre vida pessoal.
Motivo: nenhuma delas prevê desempenho e todas abrem espaço para viés.

---

## Peça 4 — Fechamento obrigatório

```
## PERGUNTAS PARA O GESTOR
<numeradas, cada uma com por que ela muda o desenho da vaga>

## O QUE FALTA VERIFICAR

## DECISÃO HUMANA NECESSÁRIA
```

As perguntas para o gestor são o produto mais subestimado deste módulo. Priorize as que
mudam o desenho da vaga, não as que só completam formulário. Exemplos de boas perguntas:

- "Essa pessoa vai receber demanda pronta ou vai negociar prioridade com as áreas?"
  (define júnior vs. pleno, e muda a faixa)
- "O que precisa estar funcionando em 90 dias para você considerar a contratação um acerto?"
- "Existe alguém no time hoje que faz parte disso? O que essa pessoa faria diferente?"
