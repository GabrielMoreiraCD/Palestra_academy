# Rubricas — escalas, níveis e pesos

---

## 1. Tipos de critério

Todo critério de vaga é classificado em um destes quatro tipos. O tipo determina como ele
é usado — e nenhum deles autoriza eliminação automática.

| Tipo | Significado | Uso |
|---|---|---|
| `OBRIGATORIO_OBJETIVO` | Requisito verificável e exigido por lei ou contrato (registro profissional, autorização de trabalho, turno inegociável) | Único tipo que pode gerar `REQUISITO NÃO ATENDIDO`, sempre com "confirmar antes de agir" |
| `ESSENCIAL` | Competência central da vaga; sem ela a pessoa não entrega no prazo esperado | Peso alto na matriz. Ausência = lacuna grave, **não** eliminação |
| `IMPORTANTE` | Acelera muito, mas é aprendível no primeiro ciclo | Peso médio. Ausência vira item de trilha de onboarding |
| `DESEJAVEL` | Diferencial real, não requisito | Peso baixo. Nunca justifica preferir alguém sozinho |

**Regra de sanidade:** se o gestor listar mais de 5 `ESSENCIAL`, sinalize. Vaga com nove
essenciais não é vaga, é lista de desejos — e é a causa mais comum de processo que não
fecha. Devolva a pergunta: *"se você só pudesse ter 3 destes no primeiro dia, quais?"*

---

## 2. Escala de evidência (por critério, por candidato)

| Status | Definição operacional |
|---|---|
| `EVIDÊNCIA` | Tem o quê + onde + escala/resultado, e dá para aprofundar em conversa |
| `INDÍCIO` | Citado, mas falta escala, contexto ou resultado |
| `AUSENTE` | Não aparece no material |
| `CONTRADIÇÃO` | Fontes divergem |

**Teste prático para separar `EVIDÊNCIA` de `INDÍCIO`:** dá para fazer uma segunda
pergunta específica sobre aquilo, usando um número ou nome que a própria pessoa deu?
Se sim, é `EVIDÊNCIA`. Se a única pergunta possível é "me fala mais", é `INDÍCIO`.

---

## 3. Cobertura de evidência

Métrica única permitida na fase de triagem. Mede **documentação**, não pessoa.

```
cobertura = (nº de critérios ESSENCIAL com status EVIDÊNCIA) / (nº total de critérios ESSENCIAL)
```

Sempre reportada com a etiqueta:

> `Isto não é recomendação de contratação nem de corte. Mede quanto de cada critério está
> documentado no material recebido, não a qualidade da pessoa.`

Cobertura baixa costuma significar **currículo mal escrito**, não pessoa fraca. Diga isso
quando for o caso.

---

## 4. Níveis de senioridade — comportamentos observáveis

Use comportamento, não tempo de casa. "5 anos de experiência" não é critério; é proxy.

| | **Júnior** | **Pleno** | **Sênior** |
|---|---|---|---|
| **Escopo** | Executa tarefa definida por outro | Recebe problema, define a tarefa | Recebe contexto ambíguo, define o problema |
| **Autonomia** | Pergunta antes de decidir | Decide dentro do combinado, escala exceção | Decide e assume trade-off; muda o combinado quando precisa |
| **Erro** | Detectado por outra pessoa | Detecta o próprio erro | Cria o mecanismo que evita a classe do erro |
| **Impacto** | A própria entrega | A entrega do time | O jeito do time trabalhar |
| **Comunicação** | Reporta o que fez | Explica por que fez assim | Convence quem discorda e ajusta quando está errado |
| **Pergunta reveladora** | "Me conta um problema que você resolveu" | "Me conta uma decisão que você tomou sozinho e o trade-off" | "Me conta uma vez que você mudou de opinião por causa de um dado" |

**Sinal de atenção na avaliação:** a pessoa descreve *o que a equipe fez* em vez do que
*ela* fez. Não é mentira — é imprecisão comum. Vira pergunta: "nessa parte, o que foi você
especificamente?"

---

## 5. Avaliação pós-entrevista (por critério)

Nunca some numa nota final. Cada critério recebe um destes quatro:

| Resultado | Definição |
|---|---|
| `SUPERA` | Demonstrou além do pedido, com exemplo concreto e verificável |
| `ATENDE` | Demonstrou o que a vaga pede, com exemplo |
| `NÃO_DEMONSTRADO` | Não apareceu na conversa — **não** é "não tem", é "não perguntamos direito" |
| `PREOCUPAÇÃO` | Apareceu algo que contradiz o critério — sempre com o trecho literal |

`NÃO_DEMONSTRADO` é responsabilidade do processo, não do candidato. Se um critério
`ESSENCIAL` ficou `NÃO_DEMONSTRADO`, a saída correta é **outra pergunta ou outra etapa**,
não uma conclusão.

---

## 6. Desafio técnico

Regras para gerar:

- Nasce das lacunas reais da entrevista, nunca de template genérico
- Tempo declarado no enunciado, teto de **4 horas**; se não couber, reduza o escopo
- Usa contexto realista da empresa, **sem dado real e sem trabalho aproveitável** —
  desafio não pode ser entrega de graça
- O enunciado diz **como será avaliado**, com os critérios visíveis para o candidato
- Sempre existe alternativa para quem não pode dedicar as horas (conversa técnica guiada
  de 60 min sobre um projeto que a pessoa já fez) — isso corrige viés contra quem tem
  filho pequeno, segundo emprego ou deslocamento longo

---

## 7. Trilha de onboarding — estrutura padrão

Cinco blocos. Todo item tem **dono**, **prazo relativo à data de início** e **critério de
concluído** (observável, não "participou de").

| Bloco | Janela | Conteúdo |
|---|---|---|
| `PRE_INICIO` | D-5 a D-1 | Acessos, equipamento, contrato, mensagem de boas-vindas, aviso ao time |
| `DIA_1` | D+0 | Pessoas-chave, ferramentas essenciais, primeira tarefa pequena e real |
| `SEMANA_1` | D+1 a D+5 | Contexto do negócio, ritos do time, uma entrega de verdade por menor que seja |
| `DIAS_30` | D+6 a D+30 | Autonomia na rotina, fechar os gaps de competência vindos da avaliação |
| `DIAS_90` | D+31 a D+90 | Entrega própria de ponta a ponta, conversa de expectativa e feedback |

**Regra de origem:** todo critério que ficou `NÃO_DEMONSTRADO` ou `INDÍCIO` na avaliação
vira item nos blocos `SEMANA_1` ou `DIAS_30`, com o campo `origem` apontando para o
critério. É isso que liga o recrutamento ao onboarding.

**Critério de concluído — errado vs. certo:**

| Errado | Certo |
|---|---|
| "Conhecer o time" | "Teve conversa de 30 min com cada pessoa da lista e registrou uma anotação sobre o que cada uma faz" |
| "Entender o produto" | "Explicou em 5 min, para o gestor, como o dado entra e onde ele é consumido" |
| "Treinamento de LGPD" | "Concluiu o módulo e o certificado está anexado" |
