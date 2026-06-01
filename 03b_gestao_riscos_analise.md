# 03B — Gestão Comercial e Riscos: Análise Crítica e Jurisprudência (Fase 2)
## Concorrência Presencial 001/2026 — Salto de Pirapora/SP — Concessão Administrativa (PPP) de RSU

**Perspectiva declarada:** licitante/proponente (premissa assumida, conforme CLAUDE.md).
**Lex specialis do contrato:** Leis n.º 8.987/1995, 11.079/2004 e 11.445/2007; a Lei n.º 14.133/2021 rege o procedimento licitatório.
**Fronteiras:** este agente é dono da matriz de riscos, gestão comercial, cofaturamento/interface com prestadora de água e bloqueios de reequilíbrio. Modelagem tarifária/estrutural de reequilíbrio → Agente 01; inconsistências formais → Agente 04 (consumidas, não recaçadas); escopo técnico/penalidades → Agente 05.

---

## NOTA METODOLÓGICA SOBRE A VERIFICAÇÃO JURISPRUDENCIAL (regra inviolável do CLAUDE.md)

- **Portal do TCU (pesquisa.apps.tcu.gov.br): NÃO confirmado.** A tentativa de abrir o inteiro teor do "Acórdão 2135/2023-TCU-Plenário" (resultado retornado por busca) devolveu apenas a página genérica de pesquisa textual, sem o conteúdo do acórdão. **Aplico o fallback de portal indisponível:** não cito esse número de acórdão de memória; registro os achados apenas com ancoragem legal/doutrinária e com a *orientação consolidada* do TCU (esta sim documentada na base oficial "Licitações e Contratos | TCU", verificada).
- **Portal do STJ (scon.stj.jus.br): não acessado diretamente.** A orientação sobre álea ordinária/variação cambial foi localizada em fontes secundárias (blog Zênite — que retornou HTTP 503 na segunda tentativa — e doutrina). **Não cito número de REsp** por não ter confirmado o número no portal oficial; registro a *tese consolidada* do STJ sem o número.
- **ANA (gov.br/ana): confirmado.** NR 13/2025 (aprovada em nov./2025) e tomadas de subsídio sobre modelo de contrato de cofaturamento (2025) verificadas — relevantes apenas para afastar a aplicabilidade do tema a esta modelagem (ver Tema 3).
- Onde escrevo "não localizei precedente específico", é declaração de lacuna, não de inexistência.

---

## TEMA 1 — GESTÃO COMERCIAL / FATURAMENTO

### Observação crítica
Não há gestão comercial de usuário nesta modelagem: a remuneração é 100% contraprestação pública (Contrato, Cláusula 22.1; Edital, TR, PG 167). A "gestão comercial" relevante para o proponente é a **gestão do fluxo de recebível público**: emissão de NF → vencimento em 20 dias (Cláusula 23.3–4) → débito automático da Conta Vinculada pelo Agente Depositário (Cláusula 23.4.2) → acionamento da Garantia de Adimplemento (Cláusulas 23.4.5 e 24).

Três fragilidades a precificar:
1. **Agente Depositário não identificado** — campo "[●]" (Contrato, Definições item 1; Agente 04, item 3.1). O proponente não conhece a instituição financeira que custodiará as contas, sua solidez nem o custo da estrutura — embora o risco de contraprestação dependa diretamente da higidez desse agente.
2. **Tabela de contraprestação dos 30 anos em branco** ("[•]", Cláusula 23.1) **sem cláusula que a vincule expressamente à Proposta Comercial vencedora** (Agente 04, item 6.1). É lacuna procedimental: o quê remunera a SPE não está formalmente ancorado no resultado do certame dentro da minuta.
3. **Vencimento da NF condicionado à manifestação da Entidade Reguladora** sobre os Indicadores (Cláusula 23.3 — emissão "até o 10.º dia da comunicação da ENTIDADE REGULADORA"). Como o regulador está indefinido (ver Tema 7.2), o gatilho temporal da própria emissão da NF depende de ato de terceiro ainda não constituído — risco de fluxo de caixa.

### Contra-argumento provável do Poder Concedente
Que a estrutura Conta Vinculada + Conta Garantia + Agente Depositário é desenho-padrão de PPP (art. 8.º da Lei n.º 11.079/2004) e que os campos "[•]" são naturais de minuta, a serem preenchidos na assinatura; que o vínculo tabela↔proposta é implícito (a contraprestação "é aquela constante da PROPOSTA COMERCIAL", Edital item 226).

### Ancoragem normativa
- *Dispositivo expresso* para a estrutura de garantia: art. 8.º da Lei n.º 11.079/2004.
- *Construção interpretativa* para o vício de não vinculação expressa tabela↔proposta e para o risco do gatilho de NF dependente de regulador indefinido (sustenta pedido de esclarecimento/saneamento da minuta com base na vinculação ao instrumento convocatório — art. 5.º e art. 92 da Lei n.º 14.133/2021).

---

## TEMA 2 — CUSTOS DE COBRANÇA / PLANO DE NEGÓCIOS

### Observação crítica
Inexistem custos de cobrança ao usuário (sem tarifa). O ponto crítico não é o custo de cobrança, mas a **ausência de Plano de Negócios de referência da Administração**: o PN é modelo a preencher pela licitante (Modelo B, Anexo II, PG 106), sem premissas numéricas oficiais (inadimplência da fonte de custeio, evolução de população/geração efetivamente tabelada, CAPEX desagregado). Consequências a precificar:
1. **Risco de assimetria informacional e de isonomia das propostas.** Sem projeção oficial de geração (e sem balança no aterro — Agente 05, item 1.4), cada licitante adota sua própria base, comprometendo a comparabilidade — e a TIR do PN (que ancora todo o reequilíbrio, Cláusula 28.2) é fixada sobre base não verificável pela Administração.
2. **Custo de regulação (0,5% do faturamento, Edital item 234) sobre faturamento incerto** — a base de cálculo é o "faturamento diretamente obtido com a prestação", conceito ambíguo num modelo sem tarifa (o "faturamento" é a própria contraprestação?). E no Contrato a taxa de regulação está em "[•]%" (Agente 04, item 6.2) — divergência alíquota Edital × Contrato e obrigação pecuniária recorrente sem base fechada.
3. **Tributos sobre receita** (ISS 2%, PIS 1,65%, COFINS 7,60%, ICMS; Edital, TR, PG 167) — a incidência de ICMS sobre serviço de manejo de RSU é juridicamente discutível e, se mal premissada, distorce a proposta; sua criação/alteração após a proposta é risco público (Matriz, risco 30), mas a premissa inicial é risco privado.

### Contra-argumento provável do Poder Concedente
PN-modelo é prática usual em PPP para preservar a liberdade de modelagem do proponente; a TIR do vencedor passa a ser o parâmetro objetivo do reequilíbrio. A ausência de premissas seria, então, "neutra".

### Ancoragem normativa
- *Construção interpretativa*: a ausência de estudos/projeções suficientes para a formulação isonômica das propostas tensiona o dever de planejamento e de disponibilização de elementos técnicos (art. 18 da Lei n.º 14.133/2021) e o art. 10, § 4.º, da Lei n.º 11.079/2004 (estimativa do impacto orçamentário-financeiro). A orientação consolidada do TCU exige estudos prévios suficientes que sustentem a estimativa de custos e a alocação de riscos (base oficial "Licitações e Contratos | TCU" — *verificada*: a maior parcela de risco transferida ao privado eleva o preço das propostas, exigindo justificativa técnica da alocação).

---

## TEMA 3 — COFATURAMENTO / INTERFACE COM PRESTADORA DE ÁGUA

### Observação crítica
**Tema inexistente nesta modelagem.** A remuneração é integralmente por contraprestação pública (Cláusula 22.1); não há tarifa ao usuário, logo não há cofaturamento na conta de água, convênio de compartilhamento de dados, contrapartida à prestadora nem fallback de dado de consumo (confirmado pela extração 03a, Tema 3). O custeio é tarefa do **Município**, via TMRSU (Leis municipais n.º 1.589/2022, LC n.º 17/25 e n.º 2.075/2025) + outras fontes orçamentárias (Cláusula 22.1.1). **A arrecadação/cobrança é do Município, não da Concessionária.**

Nota de contexto regulatório (não força tema inexistente, apenas situa): a ANA aprovou a **NR 13/2025 (nov./2025)**, com capítulo de cofaturamento de resíduos sólidos na fatura de água/esgoto (art. 5.6 e seguintes da NR 1/ANA, Res. 79/2021, na linha consolidada pela NR 13/2025), e conduziu tomadas de subsídio sobre modelo de contrato de cofaturamento em 2025. **Nada disso incide aqui**, porque o cofaturamento pressupõe arrecadação tarifária junto ao usuário — exatamente o que esta concessão administrativa não tem. Registro, porém, uma **consequência indireta**: se, no futuro, o Município migrar a TMRSU para cobrança via cofaturamento na conta de água (mecanismo da Lei n.º 11.445/2007), isso afeta a *robustez da fonte de custeio* da contraprestação, mas é risco do Poder Concedente, não da Concessionária — coerente com a alocação ao público do "descumprimento pelo Poder Concedente, incl. inadimplemento da contraprestação" (Matriz, risco 16).

### Contra-argumento provável do Poder Concedente
Concorda com a inaplicabilidade; sustenta que a fonte de custeio (TMRSU) e a forma de arrecadação são matéria exclusiva do Município e não oponíveis pela Concessionária.

### Ancoragem normativa
- *Dispositivo expresso* da inaplicabilidade: Cláusula 22.1 e 22.1.1 do Contrato; Edital, TR, PG 167.
- *Dispositivo expresso* (contexto regulatório, não incidente): NR 13/2025-ANA e art. 5.6 a 5.6.3 da NR 1/ANA (Res. 79/2021); art. 35 da Lei n.º 11.445/2007 (cobrança por taxa/tarifa de RSU).

---

## TEMA 4 — INADIMPLÊNCIA (sobre quem recai?)

### Observação crítica — recai sobre a CONCESSIONÁRIA o risco residual de garantia insuficiente
A inadimplência relevante é a do **Poder Concedente** frente à Concessionária (não há inadimplência de usuário). A Matriz aloca ao público o "inadimplemento do pagamento da CONTRAPRESTAÇÃO" (risco 16) — alocação correta e consistente com a Cláusula 23.5 (juros + multa de 2% + IPCA por atraso). Porém, há **gap de cobertura a precificar**:

1. **Dimensionamento do colchão de liquidez (3 meses).** O Saldo Mínimo da Conta Garantia = 3× a média das contraprestações (Cláusulas 24.3–24.4). O procedimento de saque é célere (purgação em 5 dias úteis, transferência em 1 dia útil — Cláusulas 24.6–24.8). **Mas:** se o inadimplemento se prolongar e a Conta Garantia não for reconstituída pelo Município (porque a TMRSU arrecadou abaixo do necessário), a garantia de 3 meses se esgota e o risco passa, de fato, à Concessionária — que só tem a faculdade de suspender investimentos/atividades não essenciais após 90 dias (Cláusula 23.6) e, em última análise, a rescisão. **A continuidade do serviço público de RSU (princípio cogente) inibe a paralisação**, de modo que, na prática, a Concessionária tende a financiar o serviço enquanto litiga. Este é o **risco mais crítico a precificar** nesta PPP.
2. **Robustez da fonte de custeio não comprovada.** A TMRSU é declarada "fonte relevante, sem caráter exclusivo" (Cláusula 22.1.1), mas o edital **não traz estudo de suficiência arrecadatória da TMRSU** (capacidade de pagamento, histórico de arrecadação, inadimplência da taxa municipal). O proponente não consegue medir a probabilidade de esgotamento da garantia.
3. **"Fator Incremental" inexiste** (confirmado em 03a, Tema 4.3): o que há é o Fator K (multiplicador de oferta — critério de julgamento) e o Fator de Avaliação (FA — redutor por desempenho na fórmula de reajuste, Cláusula 25). Nenhum deles protege contra inadimplência da fonte pública. **Não há gap "início sem Fator Incremental vs. inadimplência projetada"**, porque não há cobrança a usuário — o tema da spec não se materializa nesta modelagem; o gap relevante é o do item 1 acima (esgotamento da garantia de 3 meses).

### Contra-argumento provável do Poder Concedente
A garantia de 3 meses + reconstituição automática + juros/multa + suspensão após 90 dias + rescisão compõem cadeia robusta e padrão de PPP (art. 8.º da Lei n.º 11.079/2004); o risco de arrecadação da TMRSU é da Administração e está alocado ao público (risco 16); a vinculação de receitas (Contrato de Vinculação de Receitas) reforça a garantia.

### Ancoragem normativa
- *Dispositivo expresso*: alocação correta ao público do inadimplemento (Matriz, risco 16); art. 8.º da Lei n.º 11.079/2004 (garantias da PPP).
- *Construção interpretativa* (achado a precificar): a insuficiência do dimensionamento (3 meses) frente à ausência de estudo de capacidade de pagamento e à indisponibilidade do serviço público; sustenta pedido de esclarecimento sobre suficiência da TMRSU e eventual reforço de garantia (contragarantia da União/Estado, fundo garantidor, ou ampliação do Saldo Mínimo). Doutrina: Maurício Portugal Ribeiro, *Concessões e PPPs* (a efetividade da garantia da PPP é condição de bancabilidade; garantia subdimensionada ou de liquidez incerta eleva o custo de capital e deve ser precificada).

---

## TEMA 5 — CONFRONTO MATRIZ DE RISCOS × CONTRATO (risco a risco relevante)

Regra de fechamento do sistema: Cláusula 27.3 (desequilíbrio = sofrer efeito de risco **não** alocado à parte) + Cláusula 27.4 (quem assumiu o risco não tem reequilíbrio) + Cláusula 28.2 (apuração pela TIR do PN). A coerência interna depende, portanto, de a Matriz (Anexo IX) estar **completa e inequívoca** — e ela tem defeito de diagramação (pareamento posicional risco↔alocação; Agente 04, item 2.1), o que é grave porque um erro de pareamento inverte a alocação e, por arrasto, o direito a reequilíbrio.

| # | Risco (Matriz) | Alocação | Consistência com o Contrato / observação crítica |
|---|---|---|---|
| 1 | Erros/omissões nos projetos do Aterro/CTR pela Concessionária | PRIVADO | Consistente (Cláusula 27.4). Projetos são da Concessionária. |
| 2 | Mudança de projeto a pedido do Poder Concedente | PÚBLICO | Consistente; reflete modificação unilateral (risco 38) e enseja reequilíbrio. |
| 4–7 | Atrasos do Poder Concedente (OS, extinção de contratos atuais, bens reversíveis, desapropriações) | PÚBLICO | Consistente e favorável; conecta-se ao Período de Transição (Cláusula 12). |
| 11 | Paralisação do Aterro / intercorrência na destinação final | PRIVADO | **Atenção:** alocação genérica ao privado, mas o aterro é **bem do Poder Concedente** recebido com ressalva de vícios ocultos (risco 17). Sobreposição com risco 17/35 (passivo/vício anterior = público). Fronteira de prova recai sobre a Concessionária (Agente 05, item 2.4). Precificar contingência geotécnica/ambiental. |
| 13 | Roubos/furtos/avarias nos bens reversíveis **(exceto Galpão da Cooperativa)** | PRIVADO | **Lacuna deliberada:** o Galpão da Cooperativa fica **fora** da cobertura — não é alocado nem ao público nem ao privado. Quem arca? Provavelmente a cooperativa (sem capacidade financeira), frustrando a reversibilidade do bem. Achado a esclarecer. |
| 14 | Responsabilidade civil/ambiental pela execução | PRIVADO | Consistente, ressalvados passivos anteriores (risco 15/35 = público). |
| 16 | Descumprimento do Poder Concedente, incl. inadimplemento da contraprestação | PÚBLICO | Consistente com Cláusulas 23.5–23.6 e 24. Ver Tema 4 (gap de garantia). |
| 17/35 | Vícios ocultos / passivos ambientais anteriores à assunção | PÚBLICO | Favorável, **mas ônus de prova do "oculto e anterior" é da Concessionária**; sem balança histórica nem laudo geotécnico anexo, a prova é difícil (Agente 05). |
| 21 | Variação da demanda de RSU **até ±5%** | PRIVADO | Ver Tema 7.4 — **a variação acima de ±5% não está alocada (lacuna)**. |
| 22 | Não obtenção do retorno econômico previsto | PRIVADO | Consistente com Cláusula 26.10/26.11 e 27.4; é a álea empresarial ordinária. |
| 23/24 | Variação de custos de insumos/mão de obra | PRIVADO | Consistente — mas atenção: o **reajuste paramétrico** (Cláusula 25: dissídio 48% + IPCA 42% + diesel 10%) já recompõe parte desses custos; logo a alocação "privada" da variação de custos convive com recomposição parcial por índice. Coexistência não é contradição (reajuste ≠ reequilíbrio), mas o proponente deve mapear o **risco de base** (cesta de índices que não acompanha a estrutura real de custos). |
| 30/39 | Tributos (exceto IR) após a proposta | PÚBLICO | Consistente; IR permanece privado (álea ordinária). |
| 31 | Variação cambial | PRIVADO | Consistente com a jurisprudência (ver Tema 7.5); **sem cláusula de reequilíbrio** — risco a precificar se houver CAPEX importado (equipamentos de CTR/biossecagem). |
| 32/33 | Embargo/nova licença por não observância ambiental da Concessionária | PRIVADO | Consistente. |
| 34 | Demora do órgão ambiental, cumpridas as exigências | PÚBLICO | **Atenção à fronteira com o risco 8** (atraso de licença imputável à Concessionária = privado). Entre "morosidade do órgão" (público) e "ato imputável à Concessionária" (privado) há **zona cinzenta** — disputa provável de reequilíbrio. Mitigado pela Cláusula 30.4.1 (não penalização por demora não imputável). |
| 36/37 | Alteração legislativa/normas de regulação **específicas** | PÚBLICO | **Ponto sensível:** só a alteração de **caráter específico** é pública. Alteração **geral** (que atinja todos os setores) fica, a contrario, com o privado. Como o **regulador está indefinido** (ARSESP no Edital × "[•]" no Contrato × Secretaria Municipal no TR — Agente 04, item 4.1), o conjunto futuro de "Normas de Regulação" e seu caráter (específico/geral) é incerto — ver Tema 7.1. |
| 40 | Fato do príncipe/força maior **não seguráveis** | PÚBLICO | **Alocação condicionada à existência de seguro de mercado**: força maior segurável vira risco privado (deve ser segurada). Transfere ao privado o custo de seguros e o risco de indisponibilidade/encarecimento de apólice. |
| 42 | Manifestações sociais — quando não cobertas por seguro a preço razoável | PÚBLICO | Mesma lógica condicional do risco 40 (segurabilidade como divisor). |
| 43 | Decisão administrativa/judicial/arbitral que impeça o recebimento/reajuste da contraprestação | PÚBLICO | Consistente e favorável — protege o recebível público contra bloqueio judicial. |

### Riscos que deveriam estar na Matriz e NÃO estão (lacunas de cobertura)
1. **Variação de demanda acima de ±5%** (positiva ou negativa) — sem alocação expressa (ver Tema 7.4).
2. **Insuficiência arrecadatória da TMRSU / esgotamento da Garantia de Adimplemento** — não há risco específico para a hipótese de a fonte de custeio falhar de forma estrutural (apenas o genérico risco 16 de "inadimplemento", que pressupõe culpa, não falência arrecadatória). Ver Tema 4.
3. **Risco regulatório de indefinição do regulador** — a criação/escolha tardia do regulador, o conteúdo das futuras Normas de Regulação e a homologação de reajustes/revisões dependem de ato de terceiro inexistente; não há risco específico (ver Tema 7.1).
4. **Atraso na operação da CTR por morosidade de licenciamento não imputável** — a zona cinzenta entre riscos 8 e 34 não está fechada para o caso específico da CTR de biossecagem (licenciamento "de maior complexidade", 12–24 meses; Agente 05, item 5.2).
5. **Risco do Galpão da Cooperativa** — expressamente **excluído** da cobertura (risco 13), sem realocação — lacuna deliberada.

### Há cláusula de reequilíbrio que contradiga a alocação?
Não há contradição direta: as Cláusulas 27.3–27.4 amarram o reequilíbrio à Matriz. **Mas há tensão** entre a alocação privada da variação de custos (riscos 23/24) e a existência de reajuste paramétrico (Cláusula 25) — que recompõe parcialmente esses custos. Não é contradição jurídica (reajuste e reequilíbrio são institutos distintos), porém o proponente deve precificar o *basis risk* da cesta de índices.

### Riscos que dependem de ato de terceiro
- **Regulador (homologação de reajuste — Cláusula 25; revisões — Cláusulas 28–29; vencimento da NF — Cláusula 23.3):** terceiro **indefinido**. Risco transversal (ver Tema 7.1).
- **Município (arrecadação da TMRSU; reconstituição da Conta Garantia):** terceiro = o próprio Poder Concedente, mas em função arrecadatória distinta da contratual (ver Tema 4).
- **Agente Depositário (execução do fluxo de pagamento):** terceiro **indefinido** ("[●]").

---

## TEMA 6 — CLÁUSULAS DE BLOQUEIO DE REEQUILÍBRIO × Lei n.º 11.079/2004

### Observação crítica
O sistema de bloqueio é triplo: (i) geral, pela Matriz (Cláusula 27.4); (ii) específico das Receitas Extraordinárias, declaradas "aleatórias" (Cláusulas 26.10–26.11); (iii) implícito (câmbio, IR, demanda até 5%). Pontos a atacar/precificar:

1. **Receitas Extraordinárias "aleatórias" com bloqueio total (Cláusulas 26.10–26.11).** A Concessionária responde integralmente pela frustração das receitas extraordinárias por ela projetadas, sem reequilíbrio nem indenização de investimentos. **É compatível com a Lei n.º 11.079/2004** (repartição objetiva de riscos, art. 5.º, III) — desde que essas receitas sejam *facultativas e estimadas pela própria SPE*. O risco para o proponente é **modelagem**: se incluir receita de CDR/recicláveis/biogás na proposta para reduzir o Fator K, e ela não se confirmar, perde sem reequilíbrio — e o Contrato sequer nomeia CDR/biogás como fonte (lista exemplificativa, Agente 01, Tema 3.6). **Recomenda-se precificar receita extraordinária com forte desconto/probabilidade.**
2. **Compartilhamento assimétrico de ganhos (Cláusula 36.4 e 26.8).** 2% da receita líquida extraordinária vai ao Município (reduz contraprestação), mas ganhos de eficiência operacional e de financiamento da Concessionária são **excluídos** do compartilhamento. Assimetria favorável ao proponente — mas o TCU pode questionar se o compartilhamento de ganhos é suficiente (modicidade da contraprestação).
3. **Bloqueio por câmbio e por IR** sem cláusula de escape: alinhado à jurisprudência de álea ordinária (ver Tema 7.5).
4. **Apuração pela TIR do PN (Cláusula 28.2)** — como não há PN-referência, a TIR é a do vencedor; o bloqueio de reequilíbrio fica ancorado num parâmetro autodeclarado e não verificado pela Administração (ver Tema 2).

### Contra-argumento provável do Poder Concedente
A repartição objetiva de riscos e o tratamento das receitas extraordinárias como álea da SPE são expressamente autorizados (art. 5.º, III, da Lei n.º 11.079/2004; art. 11 da Lei n.º 8.987/1995); o reajuste paramétrico e as revisões ordinária/extraordinária preservam o equilíbrio (Cláusula 22.3) nos limites da Matriz.

### Ancoragem normativa
- *Dispositivo expresso*: art. 5.º, III, da Lei n.º 11.079/2004 (repartição objetiva de riscos, inclusive caso fortuito/força maior/fato do príncipe/álea econômica extraordinária); art. 11 da Lei n.º 8.987/1995 (receitas alternativas/acessórias para favorecer a modicidade).
- *Orientação consolidada do TCU (base oficial "Licitações e Contratos | TCU" — verificada):* materializado o risco assumido pela parte na matriz, não cabe reequilíbrio; o equilíbrio considera-se mantido quando cumpridas as condições do contrato e da matriz. **(Sem citação de número de acórdão — portal do TCU não confirmado; ver Nota Metodológica.)**
- *Doutrina:* Egon Bockmann Moreira, *Direito das Concessões de Serviço Público* (a álea ordinária é do concessionário; a matriz objetiva a repartição e estabiliza o contrato); Marcos Nóbrega, *Direito da Infraestrutura* (eficiência da alocação: cada risco ao agente que melhor o gerencia/precifica).

---

## TEMA 7 — RISCOS ESPECIAIS

### 7.1 Risco regulatório — regulador indefinido (achado central)
**Observação crítica.** A Matriz aloca corretamente ao público a alteração de Normas de Regulação **específicas** (risco 37). Porém há **contradição tríplice de identificação do regulador**: ARSESP (Edital, PG 10) × "[•]" (Contrato, Definição 15 e Cláusula 37.1) × Secretaria Municipal (TR, PG 224) — Agente 04, item 4.1. Consequências a precificar:
- O regulador **homologa o reajuste** (Cláusula 25), **conduz as revisões** (Cláusulas 28–29, com prazo de 90 dias) e **destrava o vencimento da NF** (Cláusula 23.3). Todos esses atos críticos dependem de um ente **indefinido**.
- A taxa de regulação (0,5% no Edital × "[•]%" no Contrato) também depende dessa definição.
- Se vier a ser a ARSESP, há corpo técnico e Normas de Regulação maduras; se for a Secretaria Municipal, há risco de captura/conflito (o ente que afere o FA que reduz a contraprestação atua por delegação do pagador — Agente 05, Bloco 4) e de imaturidade regulatória.

**Contra-argumento provável.** A indefinição é mera pendência de minuta; a Lei n.º 11.445/2007 (art. 23 e art. 8.º, com redação da Lei n.º 14.026/2020) e a adesão às normas de referência da ANA suprem o vácuo; o reequilíbrio por alteração de norma específica está garantido (risco 37 + Cláusula 33.11).

**Ancoragem.** *Dispositivo expresso* da alocação (risco 37; Cláusula 33.11). *Construção interpretativa* do vício: a indefinição do regulador, combinada à dependência de seus atos para reajuste/revisão/pagamento, viola a segurança jurídica e a vinculação ao instrumento convocatório (art. 5.º da Lei n.º 14.133/2021) e o dever de o edital definir a entidade reguladora (art. 23, II, "g", da Lei n.º 11.445/2007 c/c art. 11, III, da Lei n.º 11.079/2004 — regulação como condição da PPP). Pedido de esclarecimento/impugnação recomendado.

### 7.2 Saída de município / escala
**Não aplicável.** Concessão de um único município (Salto de Pirapora), sem consórcio intermunicipal (03a, Tema 7.2). Registro a *consequência de escala*: 45.262 hab. e ~925 t/mês são base modesta; a viabilidade da CTR de biossecagem/CDR depende fortemente de **receita extraordinária de resíduos de outros municípios/geradores privados** (Cláusula 26.3) — receita "aleatória" sem reequilíbrio (Tema 6). Risco de escala a precificar, embora não seja "saída de município".

### 7.3 Risco ambiental / licenciamento
**Observação crítica.** Alocação majoritariamente coerente (privado para atos imputáveis; público para passivos anteriores e morosidade do órgão). Dois pontos a precificar: (a) **zona cinzenta entre riscos 8 e 34** para a CTR (atraso imputável × morosidade do órgão), mitigada — não eliminada — pela Cláusula 30.4.1; (b) **ônus de prova do passivo "oculto e anterior"** sobre a Concessionária, sem laudo geotécnico/balança anexados (Agente 05, itens 2.4 e 5.2); (c) **custo de encerramento/pós-encerramento do aterro não dimensionado** e dever de reverter com 5 anos de vida útil (Agente 05, item 5.3) — provisão a precificar.

**Contra-argumento provável.** A alocação ao público da demora não imputável (risco 34) e dos passivos anteriores (risco 35) e a proteção da Cláusula 30.4.1 já cobrem o concessionário diligente.

**Ancoragem.** *Dispositivo expresso* (riscos 8, 32–35; Cláusula 30.4.1). *Construção interpretativa* da zona cinzenta CTR e do ônus de prova.

### 7.4 Risco de demanda — banda de ±5% e lacuna acima de 5%
**Observação crítica.** Numa PPP por contraprestação (não por tonelada), a demanda impacta sobretudo **custo operacional**, não receita. A banda de ±5% (risco 21) aloca ao privado a flutuação ordinária — coerente. **Porém a variação acima de ±5% não está alocada** (lacuna; 03a, Tema 7.4). Efeitos opostos conforme o sinal:
- **Demanda >+5%** (mais resíduos): custo operacional sobe sem aumento de contraprestação — perda do privado, **sem reequilíbrio expresso** (a lacuna joga para a regra geral 27.3, que **permitiria** reequilíbrio por ser risco "não alocado à parte"). Há, portanto, **ambiguidade interpretativa favorável a um pleito**, mas insegura.
- **Demanda <-5%** (menos resíduos): custo cai — ganho do privado.
Agravante: a base de demanda é **estimada sem balança** (Agente 05, item 1.4), tornando a banda de ±5% medida sobre número não auditável.

**Contra-argumento provável.** A variação acima de 5% recairia na revisão extraordinária (Cláusula 28) por se tratar de evento não alocado (27.3); logo "não há lacuna, há regra geral". Alternativamente, que a contraprestação por disponibilidade neutraliza a demanda.

**Ancoragem.** *Dispositivo expresso* da banda (risco 21) e da regra geral (Cláusula 27.3). *Construção interpretativa* (lacuna): pedido de esclarecimento sobre o tratamento da variação >±5% e sobre a fixação da linha de base após instalação da balança.

### 7.5 Risco cambial
**Observação crítica.** Câmbio é risco privado (risco 31) sem cláusula de escape, e o reajuste é em índices domésticos (Cláusula 25). Se a CTR exigir equipamentos importados, há exposição cambial não recomposta — a precificar.

**Contra-argumento provável.** Variação cambial é álea ordinária do negócio; sua alocação ao privado é a regra.

**Ancoragem.** *Dispositivo expresso* (risco 31). *Jurisprudência consolidada do STJ* (verificada em fontes secundárias/doutrina; **número de REsp não confirmado no portal oficial — não citado**, conforme Nota Metodológica): a oscilação cambial dentro da flutuação normal de mercado é **risco ordinário**, não autorizando reequilíbrio pela teoria da imprevisão; o mesmo se aplica a dissídio coletivo (risco 41 da Matriz). Doutrina: Egon Bockmann Moreira, *Direito das Concessões de Serviço Público* (álea ordinária).

### 7.6 Economias rurais
**Não há tratamento tarifário** (sem tarifa); risco rural é operacional (dimensionamento de coleta porta a porta em 280,5 km², cobertura rural atual 2×/semana), não comercial. A precificar como custo, não como risco de receita (03a, Tema 8; Agente 05, item 7.2 — transição sem entrega obrigatória de base cadastral georreferenciada).

---

## SÍNTESE — RISCOS MAIS CRÍTICOS A PRECIFICAR/ALOCAR + STATUS JURISPRUDENCIAL

1. **Suficiência da fonte de custeio (TMRSU) e da Garantia de Adimplemento (3 meses).** É o risco nuclear: inadimplemento da contraprestação está alocado ao público (risco 16), mas a garantia de 3 meses pode esgotar-se se a arrecadação municipal falhar estruturalmente — e a indisponibilidade do serviço de RSU inibe a paralisação, forçando a SPE a financiar o serviço. Não há estudo de capacidade de pagamento. Precificar custo de capital mais alto e pedir reforço de garantia.
2. **Regulador indefinido** (ARSESP × "[•]" × Secretaria Municipal): seus atos destravam reajuste, revisões e o próprio vencimento da NF. Risco transversal e impugnável.
3. **Receitas extraordinárias "aleatórias" com bloqueio total** (Cláusulas 26.10–26.11) + escala municipal modesta: a viabilidade da CTR depende de receita (CDR/recicláveis/outros municípios) que, se frustrada, não gera reequilíbrio. Precificar com forte desconto.
4. **Lacuna da demanda acima de ±5%** e base de demanda estimada sem balança — ambiguidade que tanto pode fundar pleito (regra geral 27.3) quanto frustrar-se.
5. **Aterro de terceiro: ônus de prova de passivo oculto sobre a SPE; reversão com 5 anos de vida útil e provisão de encerramento não dimensionada.**
6. **Câmbio e IR como riscos privados sem escape** (alinhado à jurisprudência de álea ordinária) — relevante se houver CAPEX importado.
7. **Galpão da Cooperativa excluído da cobertura de risco** (risco 13) — lacuna a esclarecer.

**Status da verificação jurisprudencial (regras invioláveis do CLAUDE.md):**
- **TCU:** orientação **consolidada** confirmada na base oficial "Licitações e Contratos | TCU" (alocação eficiente de riscos; reequilíbrio vedado para risco assumido na matriz; matriz deve ser clara/exaustiva sob pena de vício). **NÃO cito número de acórdão**: o portal pesquisa.apps.tcu.gov.br não pôde ser confirmado (devolveu página genérica) — fallback aplicado, sem citação de memória.
- **STJ:** tese **consolidada** sobre álea ordinária (câmbio e dissídio dentro da flutuação normal = risco do contratado, sem reequilíbrio) localizada em fontes secundárias/doutrina; **número de REsp não confirmado no portal oficial — não citado.**
- **ANA:** NR 13/2025 e tomadas de subsídio sobre cofaturamento (2025) **confirmadas** — registradas apenas para **afastar** a aplicabilidade do cofaturamento a esta modelagem (sem tarifa ao usuário).
- **Não localizei precedente específico** (com número confirmável) sobre matriz de riscos de PPP de resíduos com remuneração por contraprestação pública; os achados ficam ancorados nos dispositivos expressos das Leis n.º 11.079/2004, 8.987/1995 e 11.445/2007 e na doutrina (Maurício Portugal Ribeiro; Marcos Nóbrega; Egon Bockmann Moreira).
