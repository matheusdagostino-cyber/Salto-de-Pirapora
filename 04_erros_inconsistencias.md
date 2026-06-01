# AGENTE 04 — ERROS E INCONSISTÊNCIAS
**Concorrência Presencial n.º 001/2026 — Município de Salto de Pirapora/SP**
**Objeto:** estruturação de PPP (concessão administrativa) de manejo de RSU — Lei 11.079/2004.
**Perspectiva:** licitante/proponente (premissa assumida).
**Natureza deste relatório:** varredura técnica integral — detecção de defeitos formais. A *consequência jurídica* de cada achado é tarefa dos agentes de domínio (01, 02, 03, 05). Aqui apenas se *detecta* e descreve.

**Fontes:** `edital_paged.txt` (253 pp.: Edital + Anexos I a XI) · `contrato_paged.txt` (Anexo VIII — Minuta do Contrato, 99 pp.) · `etp_paged.txt` (ETP, 13 pp.). Localização citada por `PG N` dos marcadores de página.

---

## VERIFICAÇÕES ESPECÍFICAS SOLICITADAS — RESULTADO

| Verificação | Resultado |
|---|---|
| **Anexo X (Plano Municipal de RS) está fisicamente anexado?** | **NÃO.** Edital PG 249 traz apenas a folha de rosto "Anexo X – PLANO MUNICIPAL DE RESÍDUOS SÓLIDOS" seguida de página em branco. É **só remissão**; o documento não está incorporado ao corpus. |
| **Entidade reguladora nomeada ou campo aberto?** | **CONTRADITÓRIO.** Edital nomeia a **ARSESP** (PG 9). Minuta de Contrato deixa **campo em aberto `[•]`** (def. 15, PG 9 do contrato; Cláusula 33, PG 60). TR aponta **fiscalização pela Secretaria Municipal** (PG 224 do edital). Três respostas divergentes para a mesma matéria. |
| **Plano de Negócios é só modelo em branco?** | **É MODELO** (Modelo B, Anexo II, PG 105+). Porém o Edital **fornece** uma tabela de CONTRAPRESTAÇÃO de referência (PG 104) e o valor estimado do contrato (item 13, PG 16); não há, contudo, premissas de inadimplência/custo de cobrança da Administração. |
| **Matriz de Riscos (Anexo IX, PG 243–248) completa e legível?** | **Legível, porém com defeito estrutural de diagramação** — ver Tipo 2. A extração separa a coluna RISCO da coluna ALOCAÇÃO em blocos, criando ambiguidade de pareamento risco↔alocação em algumas linhas. |
| **Valores/CAPEX/prazos batem entre Edital, TR, ETP e Contrato?** | **NÃO** — há duas bases de "valor estimado do contrato" em conflito (R$ 558.596.000,00 × R$ 566.135.178,00), contaminando capital social e garantia de execução. Ver Tipo 5. |

---

## TIPO 4 — INCONSISTÊNCIAS ENTRE DOCUMENTOS
*(colocado primeiro por concentrar os defeitos mais graves)*

### 4.1 — Entidade Reguladora: nomeada no Edital, em branco no Contrato, e contrariada pelo TR (GRAVÍSSIMO)
- **Edital, PG 9 (Definições):** "ENTIDADE REGULADORA: é a Agência Reguladora de Serviços Públicos do Estado de São Paulo (**ARSESP**), entidade responsável pela regulação e fiscalização dos SERVIÇOS [...]."
- **Contrato (Anexo VIII), def. 15, PG 9:** "ENTIDADE REGULADORA: é a **[•]**, entidade responsável pela regulação [...] cuja delegação foi autorizada pela Lei Municipal n° **[•]** e pelo convênio firmado com o MUNICÍPIO em **[•]**."
- **Contrato, Cláusula 33, PG 60:** subcláusula com placeholder "**[NOME DA ENTIDADE REGULADORA]**".
- **TR (Anexo IV), PG 224:** "[...] à **Secretaria de Serviços Públicos e Obras do Município de Salto de Pirapora**, ou órgão que vier a substitui-la, será delegada a realização das atividades necessárias à fiscalização da concessão [...]."
- **Defeito:** três definições incompatíveis do regulador no mesmo edital (ARSESP × campo vazio × Secretaria Municipal). Afeta a definição de "NORMAS DE REGULAÇÃO", a taxa de regulação (Contrato Cláusula 33, PG 64) e toda a Cláusula 37 (sanções aplicadas "pela ENTIDADE REGULADORA").
- **Correção:** definir uma única entidade reguladora e replicá-la de forma idêntica em Edital, Contrato e TR; preencher Lei Municipal e dados do convênio na def. 15 do Contrato; eliminar o placeholder duplicado da Cláusula 33.

### 4.2 — Modalidade da licitação divergente: "Concorrência Presencial" × "Concorrência Pública" (GRAVE)
- **Edital:** "Concorrência **Presencial** nº 001/2026" (PG 1197 e capa) e def. de LICITAÇÃO no Edital (PG 11): "é a Concorrência **Presencial** nº 001/2026".
- **Contrato (Anexo VIII), def. 18, PG ref. linha 236:** "LICITAÇÃO: é a Concorrência **Pública** nº [•], objeto do EDITAL".
- **Contrato, capa (PG 1 do contrato):** "CONCORRÊNCIA PÚBLICA N° [•]".
- **Defeito:** o Contrato qualifica a licitação como "Concorrência Pública" enquanto o Edital a institui como "Concorrência Presencial". Discrepância terminológica que pode gerar dúvida sobre a modalidade aplicável (Lei 14.133/2021).
- **Correção:** uniformizar para "Concorrência Presencial nº 001/2026" no Contrato (capa e def. 18) e preencher o número.

### 4.3 — Discrepância terminológica de receitas: "Receitas Acessórias" × "Receitas Extraordinárias" (MÉDIO)
- **Edital, PG ref. linha 7169 (item "7. IDENTIFICAÇÃO DAS RECEITAS ACESSÓRIAS", trecho dos estudos incorporados):** trata de "**Receitas Acessórias** no campo das Concessões e PPPs".
- **Edital, Anexo II / fluxo de caixa, PG 106 (linha 4437):** rubrica "**RECEITAS EXTRAORDINÁRIAS**".
- **Contrato:** usa exclusivamente "**RECEITAS EXTRAORDINÁRIAS**" (Cláusula 26, PG 64; def. relacionada).
- **Defeito:** o mesmo instituto (receitas adicionais não tarifárias) recebe dois rótulos no Edital ("Acessórias" na parte de estudos; "Extraordinárias" no Anexo II e no Contrato). O termo "Receitas Acessórias" não é definido no rol de Definições.
- **Correção:** padronizar para "RECEITAS EXTRAORDINÁRIAS" em todo o Edital ou incluir definição de equivalência.

### 4.4 — "Tarifa" / "modicidade das tarifas" em PPP sem tarifa (MÉDIO)
- **Edital, PG ref. linha 6955:** "não havendo cobrança de **tarifa** ou qualquer tipo de pagamento direto pelos usuários".
- **Edital, PG ref. linha 7181 (citação do art. 11 da Lei 8.987/95):** "com vistas a favorecer a **modicidade das tarifas**".
- **Contrato, Cláusula 36, PG ref. linha 3927:** mecanismo de compartilhamento de ganhos pode dar-se por "**revisão de tarifas ou receitas**".
- **Defeito:** o modelo é concessão administrativa remunerada por CONTRAPRESTAÇÃO do Poder Concedente, sem tarifa de usuário (o próprio Edital o afirma). As menções a "tarifa"/"revisão de tarifas" são resíduos de modelo de concessão comum, incongruentes com a estrutura adotada.
- **Correção:** substituir "tarifa(s)" por "CONTRAPRESTAÇÃO" onde se refira à remuneração deste contrato (ressalvada a transcrição literal do art. 11 da Lei 8.987/95).

### 4.5 — Sistemas de numeração de Anexos divergentes entre Edital e Contrato (BAIXO)
- **Edital:** Anexos em algarismos romanos — Anexo I a XI (PG 105–250).
- **Contrato, Cláusula 3, PG 11:** anexos em **letras** — Anexo A (EDITAL), B (Proposta Comercial), C (Proposta Técnica), D (Atos constitutivos), E (Contrato de Vinculação de Receitas), F (Termo de Recebimento do Aterro).
- **Defeito:** o Edital é, ao mesmo tempo, o instrumento que arrola "Anexo VIII – Minuta do CONTRATO" e o "Anexo A" do próprio Contrato. Convivência de dois sistemas. Não há erro de remissão, mas exige atenção do leitor; o "Contrato de Vinculação de Receitas" (Anexo E do Contrato) não consta da lista de anexos do Edital.
- **Correção:** nota explicativa de que os anexos do Contrato (A–F) são distintos dos anexos do Edital (I–XI); confirmar a existência/anexação do "Contrato de Vinculação de Receitas".

---

## TIPO 5 — INCONSISTÊNCIAS INTERNAS

### 5.1 — Duas bases de "valor estimado do contrato" em conflito; capital social e garantia de execução ancorados na base errada (GRAVÍSSIMO)
Há **dois valores** divergentes para a mesma grandeza:
- **Item 13 (Edital, PG 16):** valor estimado do CONTRATO = **R$ 558.596.000,00**. *(Confere com o somatório da tabela de CONTRAPRESTAÇÃO de referência do Anexo II, PG 104: 11.088.000 + 3×12.240.540 + 26×19.645.630 = 558.596.000.)*
- **Anexo II (Edital, PG 100):** "O somatório total de CONTRAPRESTAÇÕES máximo admitido é de **R$ 566.135.178,00**".

Os percentuais derivados não seguem a mesma base:
| Rubrica | Valor declarado | % declarado | Base correta (item 13 = 558,596 mi) | Base implícita usada |
|---|---|---|---|---|
| Garantia de Proposta (item 72, PG ref. l.1263) | R$ 5.585.960,00 | 1% | 5.585.960,00 ✓ | item 13 (correto) |
| Capital social LICITANTE (qual. econ.-fin., item d, PG ref. l.1953) | R$ 56.613.517,80 | 10% | 55.859.600,00 ✗ | **566.135.178 (Anexo II)** |
| Garantia de Execução (item 208, PG 67) | R$ 28.306.758,90 | 5% | 27.929.800,00 ✗ | **566.135.178 (Anexo II)** |

- **Defeito:** o Edital convive com duas bases (558,596 mi e 566,135 mi). Garantia de proposta usa uma; capital social e garantia de execução usam a outra — apesar de o item 208 dizer expressamente "5% do valor estimado do CONTRATO previsto no **item 13**" (que é 558,596 mi), e a habilitação dizer "10% do valor estimado do CONTRATO previsto no **item 13**". Os valores em reais não fecham com a base que invocam.
- **Correção:** definir um único "valor estimado do CONTRATO" e recalcular 1% / 5% / 10% de forma consistente; corrigir o item 13 ou o Anexo II conforme a base verdadeira.

### 5.2 — Capital social mínimo da SPE não fecha com 5% dos investimentos (GRAVE)
- **Item 204 (Edital, PG 66):** "o capital social subscrito mínimo da CONCESSIONÁRIA (SPE) deverá ser de **R$ 4.715.904,40**, correspondente a 5% (cinco por cento) do valor estimado dos investimentos previsto no **item 14**".
- **Item 14 (Edital, PG 16):** investimentos = **R$ 93.143.449,00**.
- **Cálculo:** 5% de 93.143.449,00 = **R$ 4.657.172,45** ≠ R$ 4.715.904,40. O valor declarado corresponde a 5% de ~R$ 94.318.088, base que não aparece no Edital.
- **Defeito:** o valor em reais do capital social da SPE não corresponde ao percentual sobre o item 14 que o próprio dispositivo invoca.
- **Correção:** recalcular 5% de R$ 93.143.449,00 ou corrigir o valor de investimentos.

### 5.3 — Capital social mínimo da SPE: valor fixo no Edital × "a calcular conforme proposta" no Contrato (MÉDIO)
- **Edital, item 204, PG 66:** capital social subscrito da SPE = valor **fixo** (R$ 4.715.904,40), ancorado em 5% dos investimentos.
- **Contrato, Cláusula 9, subcláusula 9.3, PG 11:** "O capital subscrito mínimo da CONCESSIONÁRIA [...] é de **R$ [• valor a ser calculado de acordo com a proposta vencedora]**".
- **Defeito:** o Edital fixa o capital da SPE independentemente da proposta; o Contrato o trata como variável dependente da proposta vencedora. Critérios incompatíveis para a mesma grandeza.
- **Correção:** alinhar o critério (fixo vs. proporcional à proposta) entre Edital e Contrato.

### 5.4 — Cláusula 33 do Contrato: subcláusula duplicada e contraditória sobre o regulador (MÉDIO)
- **Contrato, Cláusula 33, PG 60:** subcláusula 1 atribui a regulação à "**ENTIDADE REGULADORA**"; logo abaixo, outra subcláusula "1." repete o mesmo texto, mas atribui à "**[NOME DA ENTIDADE REGULADORA]**" (placeholder) e acrescenta "nos termos do instrumento jurídico de delegação firmado com o PODER CONCEDENTE".
- **Defeito:** duplicação de subcláusula (resíduo de template), com numeração interna repetida ("1." aparece duas vezes) e uma versão com campo não preenchido.
- **Correção:** consolidar em uma única subcláusula e remover o placeholder.

---

## TIPO 1 — REFERÊNCIAS CRUZADAS QUEBRADAS

### 1.1 — Remissão a "subcláusula 36.5.2" dentro da Cláusula 37 (MÉDIO)
- **Contrato, Cláusula 37, PG 68:** "Cumprido o prazo estabelecido na nova programação de que trata a **subcláusula 36.5.2** [...]".
- **Defeito:** o trecho está inserido na Cláusula 37 (Infrações e Sanções) e refere-se a conteúdo da própria Cláusula 37 (nova programação do serviço), mas remete à "36.5.2". Provável erro de numeração herdado de versão anterior em que a matéria estava na Cláusula 36.
- **Correção:** ajustar a remissão para a subcláusula correta da Cláusula 37.

### 1.2 — Remissões de habilitação técnica ao Plano de Negócios / CAPEX — verificação (SEM DEFEITO LOCALIZADO)
- A qualificação técnica (Edital, itens 106–119, PG 41–48) **não** remete ao Plano de Negócios para fins de comprovação de CAPEX; baseia-se em atestados de capacidade técnico-operacional (coleta/transporte e operação de aterro) e CAT. As remissões internas verificadas (item 106.h → itens 45 e 51 sobre visita técnica; item 107 → itens 64 e 65 sobre tradução) **conferem**. Registra-se a ausência de defeito para afastar dupla contagem pelos agentes 01/02.

---

## TIPO 2 — ERROS DE REDAÇÃO

### 2.1 — Matriz de Riscos (Anexo IX) com diagramação que dificulta o pareamento risco↔alocação (MÉDIO)
- **Edital, Anexo IX, PG 244–248:** a tabela RISCO/ALOCAÇÃO foi diagramada de modo que, em vários blocos, **vários riscos são listados em sequência e só depois aparecem as respectivas alocações**, também em sequência (ex.: PG 244 lista cinco riscos e, na sequência, cinco alocações "PRIVADO/PÚBLICO"). O pareamento depende de contagem posicional.
- **Defeito:** risco de leitura ambígua; em uma matriz de riscos, o emparelhamento errôneo de uma linha altera a alocação. Conteúdo presente e legível, mas a estrutura tabular não é inequívoca na extração.
- **Correção:** publicar a matriz em formato de tabela com linhas fechadas (cada risco lado a lado com sua alocação) e validar o pareamento.

### 2.2 — "R$ R$" duplicado nos valores monetários (BAIXO)
- **Edital, item 72, PG ref. linha 1263:** "GARANTIA DE PROPOSTA no valor de **R$ R$** 5.585.960,00".
- **Edital, Anexo II, PG 100:** "somatório total de CONTRAPRESTAÇÕES máximo admitido é de **R$ R$** 566.135.178,00".
- **Correção:** remover a duplicação do símbolo "R$".

### 2.3 — Item 14 sem símbolo "R$" no valor (BAIXO)
- **Edital, item 14, PG 16:** "corresponde a **93.143.449,00** (Noventa e três milhões [...])" — falta o "R$" antes do número.
- **Correção:** inserir "R$".

### 2.4 — Repetição "nos termos da nos termos da" (BAIXO)
- **Edital, TR, PG 224:** "serão fiscalizados por entidade reguladora independente, **nos termos da nos termos da** Lei federal nº 11.445, de 5 de janeiro de 2007".
- **Correção:** remover a repetição.

### 2.5 — "NORMAS REGULAÇÃO" sem a preposição (BAIXO)
- **Contrato, Cláusula 33.1, PG 60:** "[...] dos objetivos constantes da legislação em vigor, das **NORMAS REGULAÇÃO** e deste CONTRATO" — falta "DE" (o termo definido é "NORMAS DE REGULAÇÃO").
- **Correção:** corrigir para "NORMAS DE REGULAÇÃO".

### 2.6 — Erros de grafia/concordância pontuais (BAIXO)
- **Edital, PG 138, linha ref. 5747:** "Previsão de **Receito** Corrente Líquida" (correto: "Receita").
- **Edital, qual. econ.-fin., item d, PG ref. l.1957:** "documentos que o **substituía** nos termos desse edital" (correto: "substituam").
- **Contrato, Cláusula 37.2, PG 68:** "prevenir situações que prejudiquem a **continuidades** dos SERVIÇOS" (correto: "continuidade"); "recuperação do prazo **descumprindo**" (correto: "descumprido").
- **Correção:** revisão ortográfica/gramatical.

---

## TIPO 3 — CAMPOS NÃO PREENCHIDOS
*(listagem; sem juízo de valor sobre a indefinição)*

### 3.1 — Contrato (Anexo VIII) — campos materiais em aberto
- **Def. 1 (PG 9): AGENTE DEPOSITÁRIO** — "[●]", CNPJ "[●]", sede "[●]".
- **Def. 15 (PG 9): ENTIDADE REGULADORA** — "[•]", Lei Municipal "[•]", convênio "[•]". (ver 4.1)
- **Def. 3 (PG 9):** coordenadas geográficas do ATERRO — "[•]".
- **Def. 18 (PG ref. l.236): LICITAÇÃO** — "Concorrência Pública nº [•]". (ver 4.2)
- **Preâmbulo (PG 1 do contrato, l.53–79):** CONCORRÊNCIA PÚBLICA "[•]"; CONTRATO N° "[•]"; data "[•]/[•]/[•]"; CNPJ do Município "[•]"; Prefeito "[•]"; CONCESSIONÁRIA "[•]" e CNPJ "[•]"; interveniente anuente / ENTIDADE REGULADORA "[•]".
- **Cláusula 8.1 (PG 11): VALOR DO CONTRATO** — "R$ [• valor a ser calculado de acordo com a proposta vencedora]".
- **Cláusula 9.3 (PG 11):** capital subscrito mínimo — "R$ [• ...]". (ver 5.3)
- **Cláusula 23 (PG 39–40): tabela de CONTRAPRESTAÇÃO MENSAL** — **todos os 30 anos em "[•]"** (totalmente em branco).
- **Cláusula 32.1 (PG 59): GARANTIA DE EXECUÇÃO** — "R$ [•] ([•])".
- **Cláusula 33 (PG 64): taxa de regulação** — "[•]% ([•]) de [•] referente ao exercício anterior", pagamento "até o [•] dia do mês".
- **Cláusula 33.1 (PG 60):** "[NOME DA ENTIDADE REGULADORA]". (ver 5.4)
- **Cláusula 50 (PG ref. l.5730–5732): endereços de COMUNICAÇÕES** — PODER CONCEDENTE "[•]", CONCESSIONÁRIA "[•]", ENTIDADE REGULADORA "[•]".
- **Fecho (PG ref. l.5827):** data "[•] de [•] de [•]"; assinaturas e testemunhas em branco.

### 3.2 — Edital — Anexo I (Modelos de Cartas e Declarações)
- Diversos "[•]" são **campos de preenchimento próprios de modelos** (nº do edital, nome/CNPJ do licitante, banco, valores de fiança, datas). Registrados aqui apenas como existentes: PG ref. linhas 3186, 3258, 3263, 3267, 3301, 3341, 3346, 3384, 3419, 3483, 3525, 3565, 3604, 3641, 3678, 3686, 3725, 3760, 3767, 3795–3808 (carta de fiança garantia de proposta), 3846, 3882, 3921, 3965–4017 (carta de fiança garantia de execução), 4216–4234 (proposta comercial / Fator K).
- **Carta de Fiança (PG ref. l.4005):** "vigorará pelo prazo de **[completar – mínimo 12 meses]**" — campo com instrução embutida.

### 3.3 — Edital — corpo / sítio de publicação
- **PG ref. l.2323:** "divulgada mediante aviso publicado no site **[•]**".

### 3.4 — Edital — Anexo XI (Termo de Recebimento do Aterro), PG 251–253
- Modelo com "[•]" em data, CNPJ, representantes, coordenadas, nº do contrato, datas de vistoria — próprios de modelo a preencher.

### 3.5 — Anexo X (Plano Municipal de RS), PG 249
- **Folha de rosto sem conteúdo** — não é "campo em aberto" em sentido estrito, mas **anexo não incorporado** (ver Verificações Específicas).

---

## TIPO 6 — LACUNAS

### 6.1 — Tabela de CONTRAPRESTAÇÃO do Contrato totalmente em branco (GRAVE)
- **Contrato, Cláusula 23, PG 39–40:** os 30 anos de CONTRAPRESTAÇÃO MENSAL estão em "[•]". Embora a minuta seja preenchida com a proposta vencedora, **não há remissão expressa** que vincule essa tabela ao resultado do julgamento nem à tabela de referência do Edital (Anexo II, PG 104). Lacuna de procedimento de preenchimento.
- **Correção:** inserir cláusula remetendo o preenchimento da tabela à PROPOSTA COMERCIAL vencedora (Anexo B do Contrato).

### 6.2 — Taxa de regulação sem percentual, base de cálculo e vencimento (GRAVE)
- **Contrato, Cláusula 33, PG 64:** "[•]% ([•]) de [•] referente ao exercício anterior [...] até o [•] dia do mês".
- **Defeito:** obrigação pecuniária recorrente da Concessionária sem alíquota, sem base de cálculo definida e sem dia de vencimento. Matéria que deveria estar no Contrato, não remetida a definição posterior.
- **Correção:** fixar percentual, base (ex.: receita operacional líquida) e vencimento.

### 6.3 — Remissão genérica a "NORMAS DE REGULAÇÃO" para matéria contratual (MÉDIO)
- **Contrato, Cláusula 37.1, PG 67 e Cláusula 33:** descumprimento "das obrigações [...] previstas neste CONTRATO, nas **NORMAS DE REGULAÇÃO** e demais normas técnicas" enseja sanção. Como a ENTIDADE REGULADORA está indefinida (4.1) e as "NORMAS DE REGULAÇÃO" são as que ela vier a editar, o conteúdo sancionável depende de norma futura de regulador ainda não nomeado.
- **Correção:** definir o regulador e o núcleo mínimo de obrigações/penalidades diretamente no Contrato, reservando às NORMAS DE REGULAÇÃO apenas o detalhamento.

### 6.4 — Anexo X não incorporado — obrigações sem o documento de referência (MÉDIO)
- **Edital, PG 249:** o Plano Municipal de Resíduos Sólidos, ao qual o objeto e as metas se vinculam, **não está fisicamente no edital** — apenas a folha de rosto. Lacuna documental.
- **Correção:** anexar o Plano Municipal ou indicar o link/ato de publicação oficial.

---

## SÍNTESE DE GRAVIDADE (para a Consolidação — Agente 06)
1. **Entidade Reguladora indefinida/contraditória** (ARSESP × `[•]` × Secretaria Municipal) — 4.1.
2. **Duas bases de valor estimado do contrato** (558,596 mi × 566,135 mi) contaminando capital social e garantia de execução — 5.1.
3. **Capital social da SPE não fecha com 5% dos investimentos** — 5.2.
4. **Tabela de CONTRAPRESTAÇÃO do Contrato em branco e sem vínculo expresso à proposta** — 6.1.
5. **Taxa de regulação sem alíquota/base/vencimento** — 6.2.
6. **Anexo X (Plano Municipal de RS) não anexado** — 6.4.
7. **Modalidade divergente** (Concorrência Presencial × Concorrência Pública) — 4.2.
8. **Cláusula 33 do Contrato duplicada/contraditória** sobre o regulador — 5.4.
