# Copiloto de RH — kit da palestra

Kit prático de uma palestra de IA aplicada a Recursos Humanos. Em ~3 horas, a plateia
constrói um copiloto que atravessa o processo inteiro de gente: do briefing do gestor até
a trilha de onboarding de quem foi contratado.

**Todos os dados aqui são fictícios**, criados para treinamento. Nenhum candidato,
colaborador ou empresa real aparece neste kit.

---

## Comece por aqui

| Você é | Abra |
|---|---|
| Participante | **[`GUIA_AO_VIVO.md`](GUIA_AO_VIVO.md)** |
| Facilitador | [`facilitador/ROTEIRO.md`](facilitador/ROTEIRO.md) |
| Só quer entender a ideia | Continue lendo |

---

## A ideia em três frases

1. Uma **skill** é processo escrito num arquivo de texto: identidade, etapas, rubricas e
   limites. Não é mágica, e quem sabe escrever um procedimento já sabe fazer uma.
2. O copiloto não devolve texto bonito — devolve **dado estruturado**. Por isso ele entra
   num sistema, vira tela, vira notificação, vira acompanhamento.
3. O mesmo artefato que define a vaga e avalia o candidato **monta a trilha de onboarding
   dele**. Os gaps que apareceram na entrevista viram os primeiros itens do onboarding.

---

## O fluxo

```
briefing do gestor ──► [1] ──► vaga.json ─────────────┐
currículos ──────────► [2] ──► matriz_evidencia.json  │  mesmos critérios
transcrição ─────────► [3] ──► avaliacao.json ────────┤  atravessando tudo
contratado + data ───► [4] ──► trilha_onboarding.json ┘ ──► app ──► Slack
```

**Regra que atravessa os quatro módulos:** o copiloto **nunca elimina candidato**. Ele
organiza evidência, mostra o que falta verificar e devolve para uma pessoa decidir. Isso
está escrito em `skill/copiloto-rh/guardrails.md` e é testado ao vivo no Passo 3 do guia.

---

## Estrutura

```
Palestra_academy/
├── GUIA_AO_VIVO.md              ← o guia da plateia, passo a passo
├── skill/copiloto-rh/
│   ├── SKILL.md                 ← identidade, módulos e regras inegociáveis
│   ├── guardrails.md            ← regras de conduta completas
│   ├── rubricas.md              ← escalas, senioridade, pesos, estrutura da trilha
│   ├── 01-perfil-de-vaga.md     ← os quatro módulos, com formato exato de saída
│   ├── 02-matriz-de-evidencia.md
│   ├── 03-avaliacao-entrevista.md
│   ├── 04-trilha-onboarding.md
│   ├── COLAR-NO-CHAT.md         ← base leve para colar (padrão da palestra)
│   └── COLAR-NO-CHAT-TUDO.md    ← skill inteira num arquivo só
├── dados-sinteticos/
│   ├── briefing-gestor.txt      ← áudio de WhatsApp transcrito, bagunçado de propósito
│   ├── candidatos/              ← três currículos com perfis desenhados
│   ├── transcricao-entrevista.txt
│   └── ficha-funcao.md          ← insumo do onboarding
├── schemas/                     ← os quatro contratos JSON
├── gabarito/                    ← saída esperada de cada passo (redigida, não capturada)
├── app/
│   ├── PROMPT_LOVABLE.md        ← prompt do app que consome os JSONs
│   └── gerar-colar-no-chat.py   ← regenera o COLAR-NO-CHAT.md
└── facilitador/ROTEIRO.md       ← tempos, falas-chave, riscos e planos B
```

---

## Como rodar a skill

**Em qualquer LLM, sem instalar nada:** copie `skill/copiloto-rh/COLAR-NO-CHAT.md` inteiro
e cole como primeira mensagem de uma conversa nova. Depois cole o módulo de cada passo,
na hora de usar — o guia diz qual. Se não quiser se preocupar com limite de uso, use
`COLAR-NO-CHAT-TUDO.md`, que já traz os quatro módulos.

**Com Projetos (Claude, Gemini, ou equivalente):** cole o corpo do `SKILL.md` nas instruções
personalizadas e anexe os demais arquivos como conhecimento.

**No Claude Code:** copie a pasta `skill/copiloto-rh` para
`C:\Users\<usuario>\.claude\skills\copiloto-rh`, reinicie e chame `/copiloto-rh`.

Os três caminhos produzem o mesmo resultado. É o mesmo texto.

---

## Manutenção

Ao editar qualquer arquivo de `skill/copiloto-rh/`, regenere o arquivo de colagem:

```bash
python app/gerar-colar-no-chat.py
```

---

## Aviso

Os artefatos gerados por este copiloto contêm dado pessoal de candidato quando usados com
dado real. Em uso de verdade, observe a LGPD: minimize o que é coletado, defina prazo de
retenção, registre quem decidiu o quê, e informe os candidatos de que há apoio de IA no
processo. A decisão é sempre humana e sempre nominal.
