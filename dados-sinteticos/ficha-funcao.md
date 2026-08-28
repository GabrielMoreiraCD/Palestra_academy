# Ficha da função — Analista de Dados Pleno

Área: Planejamento e Dados
Gestor direto: Rogério Bastos (Gerente de Planejamento e Dados)
Modelo de trabalho: híbrido, 2 dias presenciais (terça e quinta)
Local: escritório São Paulo — unidade Berrini

> Documento de referência para geração de trilha de onboarding. Dados fictícios,
> criados para fins de treinamento.

---

## O que a área faz

Centraliza a produção de indicadores e relatórios para Comercial, Operações, Supply e
Diretoria. Hoje são 3 pessoas: 1 gerente, 1 analista pleno, 1 analista júnior.

Rituais fixos:

| Rito | Quando | Quem participa |
|---|---|---|
| Daily da área | seg a sex, 9h15, 15 min | time de dados |
| Priorização com as áreas | quinzenal, terça, 14h | gerente + representante de cada área |
| Revisão de indicadores | mensal, primeira sexta | time + diretoria |
| Retro da área | mensal, última sexta | time de dados |

---

## Sistemas e acessos

| Sistema | Nível para esta função | Solicitar para | Prazo típico |
|---|---|---|---|
| E-mail corporativo e Teams | padrão | TI — service desk | 1 dia |
| VPN | padrão | TI — service desk | 1 dia |
| Azure DevOps (repositórios) | contribuidor | TI — service desk | 2 dias |
| Data Warehouse — Azure Synapse | leitura + escrita em camada `stg` | Governança de Dados | **5 dias úteis, exige aprovação do gestor da área dona do dado** |
| Power BI — workspace Planejamento | membro | Gerente da área | 1 dia |
| ERP (leitura de faturamento) | consulta | Controladoria | 3 dias |
| Slack — canais da área | `#dados-planejamento`, `#onboarding-dados` | Gerente da área | imediato |

> **Atenção conhecida:** o acesso ao Synapse é o gargalo histórico da área. Já aconteceu
> de colaborador passar a primeira semana inteira sem conseguir consultar o banco.

---

## Pessoas-chave

| Nome | Papel | Por que conversar |
|---|---|---|
| Rogério Bastos | Gerente de Planejamento e Dados | Gestor direto. Define prioridade e expectativa dos 90 dias |
| Denise Aoki | Analista de Dados Pleno (time) | Conhece o modelo de vendas atual e todas as gambiarras dele |
| Thiago Lemes | Analista de Dados Júnior (time) | Toca a fila de pedidos do dia a dia |
| Cláudia Ferrari | Diretora Comercial | Maior demandante da área. Entender o que ela precisa muda a priorização |
| Marcos Beltrão | Coordenador de Governança de Dados | Aprova acesso, define padrão de nomenclatura e política de dado sensível |
| Sandra Kubo | Business Partner de RH | Ponto de contato para tudo administrativo |

---

## Treinamentos obrigatórios (compliance)

| Treinamento | Prazo | Onde |
|---|---|---|
| Código de conduta | até D+5 | Plataforma interna de treinamento |
| LGPD e tratamento de dado pessoal | até D+10 | Plataforma interna |
| Segurança da informação | até D+10 | Plataforma interna |
| Política de uso de IA generativa | até D+15 | Plataforma interna |

---

## Contexto que a pessoa precisa entender no primeiro mês

1. **O modelo de vendas atual e por que ele é ruim.** É o projeto principal dos 90 dias.
   Denise é a fonte.
2. **Como a fila de pedidos funciona hoje** — e por que "quem grita mais alto" é o
   critério de priorização atual. Thiago vive isso.
3. **A diferença entre pedido e pergunta.** Metade do retrabalho da área vem de entregar
   exatamente o que foi pedido.
4. **Quais relatórios existem e quem realmente abre cada um.** Nunca foi medido.

---

## O que se espera em 90 dias

- Fila de pedidos com critério de priorização definido e público
- Modelo dimensional de vendas redesenhado (desenho aprovado; implementação pode seguir)
- Interlocução direta com pelo menos duas áreas demandantes, sem passar pelo gerente

---

## Equipamento

Notebook, monitor adicional e headset. Pedido feito pelo gestor à TI, **prazo de 7 dias
úteis** — precisa ser disparado antes da data de início.
