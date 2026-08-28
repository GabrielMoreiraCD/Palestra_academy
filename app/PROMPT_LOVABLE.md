# Prompt do app — cole no Lovable, bolt.new ou v0

> Gere o app **antes da palestra**, não no palco. Deixe publicado e com um
> `trilha_onboarding.json` de teste já importado. No palco, importe o JSON gerado ao vivo.
>
> Escopo deliberadamente pequeno: o app existe para mostrar que o JSON **entra em sistema**.
> Não é o produto.

---

## Prompt principal (copiar tudo abaixo)

```
Construa um app web de acompanhamento de recrutamento e onboarding chamado "Copiloto RH".
Português do Brasil. Sem backend e sem login: persista tudo em localStorage.

## Conceito

O app não gera conteúdo. Ele CONSOME arquivos JSON produzidos por um copiloto de IA e os
transforma em telas de acompanhamento. Existem quatro tipos de JSON: vaga, matriz de
evidência, avaliação de entrevista e trilha de onboarding.

## Navegação

Barra lateral com quatro seções: Vagas, Candidatos, Avaliações, Onboarding.
Botão "Importar JSON" sempre visível no topo.

## Importar JSON

Modal com uma textarea grande, um botão "Colar exemplo" e um botão "Importar".
Ao importar, detecte o tipo pelo formato:
- tem "criterios" e "vaga_id"       -> vaga
- tem "candidatos" e "aviso"        -> matriz de evidência
- tem "resultados" e "candidato_id" -> avaliação
- tem "blocos" e "colaborador"      -> trilha de onboarding
Se o JSON for inválido, mostre o erro de parse em vermelho, sem quebrar a tela.

## Tela: Vagas

Lista de cartões de vaga com título, área, gestor, senioridade e nº de candidatos.
Ao clicar, abre o detalhe:
- O campo "problema_a_resolver" em destaque, no topo, com fonte maior. É o mais importante.
- Tabela de critérios com etiqueta colorida por tipo:
  ESSENCIAL = âmbar, IMPORTANTE = azul, DESEJAVEL = cinza, OBRIGATORIO_OBJETIVO = roxo.
  Colunas: nome, tipo, comportamento observável, como verificar.
- Bloco "Critérios não incorporados" com fundo vermelho claro, mostrando texto original,
  motivo e alternativa proposta. Se a lista estiver vazia, não mostre o bloco.
- Bloco "Lacunas do briefing" como lista de pendências.
- Campos nulos (faixa salarial, modelo de trabalho) aparecem como "não informado" em
  itálico cinza. Nunca esconda um campo nulo: a ausência é informação.

## Tela: Candidatos (matriz de evidência)

Tabela cruzada: uma linha por critério, uma coluna por candidato.
Cada célula é uma etiqueta:
  EVIDENCIA = verde, INDICIO = âmbar, AUSENTE = cinza, CONTRADICAO = vermelho.
Ao passar o mouse sobre a célula, um tooltip mostra o trecho citado e a fonte.
Ao clicar na célula, abre um painel lateral com trecho, observação e pergunta sugerida.

No topo da tela, uma faixa fixa cinza com este texto, sempre visível:
  "Esta matriz não recomenda contratação nem eliminação. Decisão humana obrigatória."

Abaixo do nome de cada candidato, a cobertura (ex.: "4/5 essenciais documentados") e, em
letra menor, "mede documentação, não a pessoa".

IMPORTANTE: não exista nenhum botão de eliminar, rejeitar, descartar ou ordenar candidatos
por qualidade. Ordenação permitida: apenas alfabética ou por cobertura, e quando ordenar
por cobertura, mostre a faixa de aviso acima da tabela.

## Tela: Avaliações

Uma avaliação por candidato, com abas: Critérios, Contradições, Sinais fracos,
Problemas do processo.

Aba Critérios: um cartão por critério com a etiqueta de resultado
  (SUPERA = verde, ATENDE = azul, NAO_DEMONSTRADO = cinza, PREOCUPACAO = âmbar),
os trechos citados em blockquote com o minuto, a leitura e o campo "o que ainda não
sabemos" em destaque.
Quando o resultado for NAO_DEMONSTRADO, mostre o aviso: "falha do roteiro, não do
candidato".

Aba Problemas do processo: fundo levemente vermelho. Cada item com ocorrência, problema e
ação. Esta aba avalia a entrevista, não o candidato — deixe isso escrito no topo.

No rodapé da avaliação, o bloco de decisão:
- Botões: "Avançar" / "Não avançar" / "Aguardando"
- Um campo de texto OBRIGATÓRIO: "Quem está decidindo"
- O botão de salvar fica desabilitado enquanto o nome estiver vazio
- Ao salvar, grave decisão, nome e data/hora, e mostre acima do bloco:
  "Decidido por <nome> em <data e hora>"
- Depois de decidido, o registro fica visível e não pode ser apagado, apenas alterado —
  e cada alteração vira uma nova linha no histórico

## Tela: Onboarding

Lista de colaboradores em onboarding: nome, função, data de início, barra de progresso
(itens concluídos / total) e dias desde o início.

Ao clicar, abre a trilha:
- Os cinco blocos (PRE_INICIO, DIA_1, SEMANA_1, DIAS_30, DIAS_90) como seções recolhíveis
- Cada item mostra: caixa de seleção, título, dono, prazo relativo e absoluto, e o
  critério de concluído em letra menor
- Item com "origem.tipo" igual a "avaliacao_entrevista" recebe uma etiqueta roxa
  "personalizado" e, no tooltip, o texto de "origem.referencia"
- Item com prazo vencido e não concluído fica com a data em vermelho
- Item com "bloqueia" não vazio mostra um ícone de corrente e, no tooltip, quais itens ele
  trava
- Um filtro no topo: "Todos" / "Só personalizados" / "Atrasados"

Ao marcar um item como concluído, grave o horário e mostre uma notificação de sucesso.
Se o item tiver "notifica_slack": true, dispare o webhook (ver abaixo) e mostre no aviso:
"notificação enviada para <canal>".

Painel lateral direito da trilha com: pessoas-chave, acessos necessários (destacando em
vermelho os que têm campo "risco" preenchido) e marcos de acompanhamento.

## Configuração do Slack

Uma tela de Configurações com um campo para a URL do Webhook do Slack, salvo em
localStorage. Um botão "Enviar mensagem de teste".

Ao disparar, faça POST com corpo:
{ "text": "<nome> concluiu: <título do item> (<bloco>) — trilha de <função>" }

Se a URL não estiver preenchida, não quebre: mostre no aviso
"webhook não configurado — a notificação seria enviada para <canal>".
Trate erro de rede sem derrubar a tela.

## Visual

Limpo e denso, estilo ferramenta interna. Tipografia sem serifa, cantos levemente
arredondados, sem gradiente e sem ilustração. Modo claro e escuro. Tabelas com scroll
horizontal próprio quando não couberem.

## Dados de exemplo

Já venha carregado com uma vaga, três candidatos e uma trilha, para o app nunca abrir
vazio. O botão "Colar exemplo" do modal de importação preenche a textarea com um JSON de
trilha válido.
```

---

## Ajustes prováveis depois da primeira geração

Peça um de cada vez, e teste entre eles:

1. `"O bloco de decisão precisa exigir o nome de quem decide. O botão salvar fica
   desabilitado enquanto estiver vazio."` — é o detalhe que sustenta a fala sobre
   rastreabilidade
2. `"Na tela de candidatos, remova qualquer botão de eliminar ou rejeitar, se existir."`
3. `"Os itens com origem em avaliação de entrevista precisam de etiqueta visível."` — é o
   que você vai apontar no palco
4. `"Adicione o disparo do webhook do Slack ao marcar item concluído."`

---

## Roteiro dos 3 minutos no palco

1. Abrir o app já publicado, na tela de Onboarding vazia
2. Importar JSON → colar o `trilha_onboarding.json` gerado ao vivo no Passo 5
3. A trilha aparece: cinco blocos, prazos, donos
4. Filtrar por **"Só personalizados"** → sobram os itens que vieram da avaliação da
   entrevista. **É o momento da demonstração inteira.** Diga em voz alta: *"esses quatro
   itens só existem porque a entrevista aconteceu"*
5. Marcar "Azure na prática" como concluído → notificação → Slack
6. Ir em Avaliações, tentar salvar uma decisão sem preencher o nome → o botão não deixa

---

## Plano B

Se a geração falhar ou a internet cair: tenha **capturas de tela** das seis etapas acima
salvas em `app/prints/`. Passe as imagens e narre. A mensagem é a mesma — o JSON vira
tela — e ninguém na plateia perde nada.

Grave também um vídeo de 90 segundos percorrendo o roteiro. Vale mais que qualquer
tentativa de recuperar uma geração no palco.
