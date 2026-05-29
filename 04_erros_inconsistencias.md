# AGENTE 04 — ERROS E INCONSISTÊNCIAS

**Concorrência Presencial nº 001/2026 — Concessão Administrativa (PPP) de Resíduos Sólidos Urbanos — Salto de Pirapora/SP**
Varredura técnica integral, sem pesquisa jurisprudencial.

Fontes analisadas: `_text_edital.txt` (Edital + Anexos I a XI), `_text_contrato.txt` (Anexo VIII — Minuta do Contrato), `_text_etp.txt` (Estudo Técnico Preliminar).

> **Observação metodológica preliminar:** o presente edital NÃO possui "Apêndice de Definições" autônomo nem anexos numerados como "Apêndice X". As definições estão (i) na **Seção II – Definições** do corpo do Edital (item 7, pp. 6-15) e (ii) na **Cláusula 1 – Definições** do Contrato. Os anexos do Edital usam numeração romana (I a XI); o Contrato usa numeração própria por **letras (A a F)**. Esta dualidade de sistemas de numeração é, por si, fonte de várias inconsistências abaixo. Nenhuma ocorrência literal de "Erro! Fonte de referência não encontrada" foi localizada no texto extraído.

---

## TIPO 1 — INCONSISTÊNCIAS DE VALORES (mesma grandeza, valores diferentes) — *GRAVÍSSIMO*

Esta é a categoria mais grave: há **dois valores conflitantes para o "valor total do CONTRATO / somatório das CONTRAPRESTAÇÕES"**, e as remissões cruzadas usam o valor errado, gerando memórias de cálculo que não fecham.

### 1.1. Valor estimado do CONTRATO: R$ 558.596.000,00 vs. R$ 566.135.178,00
- **Edital, item 13 (p. 16):** "O valor estimado do CONTRATO é de **R$ 558.596.000,00** (Quinhentos e cinquenta e oito milhões, quinhentos e noventa e seis mil reais), correspondente ao somatório das CONTRAPRESTAÇÕES da CONCESSIONÁRIA projetadas para todo o prazo de vigência..."
- **Edital, Anexo II – Diretrizes para Elaboração da Proposta Comercial (p. 100):** "O somatório total de CONTRAPRESTAÇÕES máximo admitido é de R$ R$ **566.135.178,00** (Quinhentos e sessenta e seis milhões, cento e trinta e cinco mil, cento e setenta e oito reais);"
- **Natureza:** a mesma grandeza (somatório das contraprestações = valor do contrato) recebe **dois valores distintos** que divergem em R$ 7,5 milhões. O teto de proposta do Anexo II (566.135.178,00) é maior que o "valor estimado do CONTRATO" do item 13 (558.596.000,00), o que é logicamente incoerente e abre disputa sobre qual é o teto vinculante para desclassificação de propostas.
- **Prova de que o valor "verdadeiro" usado nos cálculos é 566.135.178,00** (ver 1.2 e 1.3): todas as garantias e exigências de capital social foram calculadas sobre 566.135.178,00, e não sobre 558.596.000,00.
- **Correção:** uniformizar o valor estimado do CONTRATO. Se o cálculo correto é 566.135.178,00, corrigir o item 13; caso contrário, recalcular item 208, item d) de qualificação econômica, e o teto do Anexo II.

### 1.2. Garantia de Execução do Contrato: percentual e base não fecham
- **Edital, item 208 (p. 66):** "...GARANTIA DE EXECUÇÃO DO CONTRATO no valor de **R$ 28.306.758,90**..., correspondente a **5% (cinco por cento) do valor estimado do CONTRATO previsto no item 13**."
- **Natureza:** 5% do item 13 (558.596.000,00) = **R$ 27.929.800,00**, e NÃO R$ 28.306.758,90. O valor declarado (28.306.758,90) corresponde a 5% de **566.135.178,00** (o valor do Anexo II, item 1.1). A remissão "previsto no item 13" está, portanto, quebrada/incorreta — aponta para o valor errado.
- **Correção:** corrigir a base (apontar para o valor de 566.135.178,00) ou recalcular o valor da garantia para coerência com o item 13.

### 1.3. Capital social mínimo para qualificação econômica: percentual e base não fecham
- **Edital, item d) de qualificação econômico-financeira (p. ~48):** "capital social de, no mínimo, **R$ 56.613.517,80**..., correspondente a **10% (dez por cento) do valor estimado do CONTRATO previsto no item 13**."
- **Natureza:** 10% do item 13 (558.596.000,00) = **R$ 55.859.600,00**, e NÃO R$ 56.613.517,80. O valor declarado corresponde a 10% de **566.135.178,00**. Remissão ao "item 13" novamente incorreta.
- **Correção:** idem 1.2.

### 1.4. Capital subscrito mínimo da SPE: base divergente do item 14
- **Edital, item 204 (p. 66):** "...o capital social subscrito mínimo da CONCESSIONÁRIA (SPE) deverá ser de **R$ 4.715.904,40**..., correspondente a **5% (cinco por cento) do valor estimado dos investimentos previsto no item 14**..."
- **Edital, item 14 (p. 16):** "O valor estimado dos investimentos... corresponde a **93.143.449,00** (Noventa e três milhões, cento e quarenta e três mil, quatrocentos e quarenta e nove Reais)."
- **Natureza:** 5% de 93.143.449,00 = **R$ 4.657.172,45**, e NÃO R$ 4.715.904,40. O valor declarado (4.715.904,40) corresponde a 5% de **R$ 94.318.088,00** — investimento diferente do informado no item 14. Há, portanto, **dois valores de investimento implícitos** (93.143.449,00 declarado vs. 94.318.088,00 usado no cálculo do capital).
- **Correção:** uniformizar o valor de investimento e recalcular o capital subscrito mínimo.

---

## TIPO 2 — CAMPOS NÃO PREENCHIDOS (placeholders `[•]`, `[●]`, `[___]`)

O **Edital** está, em regra, preenchido (ARSESP, coordenadas, datas, valores). A **Minuta do Contrato (Anexo VIII)**, ao contrário, mantém **dezenas de campos em branco**, vários dos quais **deveriam estar definidos já na fase de CP** porque sua indefinição impede a análise plena do contrato pelos licitantes.

### 2.1. Tabela completa de campos em branco

| # | Documento / Local | Trecho (transcrição) | Tipo de campo | Classificação |
|---|---|---|---|---|
| 1 | Contrato, preâmbulo, l. 53 | "CONCORRÊNCIA PÚBLICA N° [•]" | nº da licitação | Legítimo preencher depois |
| 2 | Contrato, preâmbulo, l. 54 | "CONTRATO N° [•]" | nº do contrato | Legítimo preencher depois |
| 3 | Contrato, preâmbulo, l. 64 | "Aos [•] dias do mês de [•] de [•]" | data de assinatura | Legítimo preencher depois |
| 4 | Contrato, preâmbulo, l. 66 | "inscrita no CNPJ sob nº [•]" (Município) | CNPJ do Município | **Deve estar na CP** (dado público e fixo) |
| 5 | Contrato, preâmbulo, l. 68 | "representado pelo seu Prefeito Municipal, Sr. [•]" | nome do Prefeito | **Deve estar na CP** (autoridade conhecida) |
| 6 | Contrato, preâmbulo, l. 69-73 | "[•], sociedade anônima, inscrita no CNPJ sob nº [•], com sede na [•]... Sr(s). [•]" | identificação da CONCESSIONÁRIA | Legítimo preencher depois |
| 7 | Contrato, preâmbulo, l. 77-81 | "interveniente anuente, a [•], com sede na [•], no Município de [•]... Sr. [•]... ENTIDADE REGULADORA" | identificação da ENTIDADE REGULADORA | **Deve estar na CP** (ver Tipo 4.1 — o Edital já diz ser a ARSESP) |
| 8 | Contrato, Cláusula 1, item 1, l. 97-98 | "AGENTE DEPOSITÁRIO: é a [●], instituição financeira com sede na [●], inscrita no CNPJ sob nº [●]" | identificação do agente depositário | Legítimo preencher depois (definido no fechamento financeiro) |
| 9 | Contrato, Cláusula 1, item 3, l. 125 | "ATERRO SANITÁRIO... localizado nas coordenadas geográficas [•]" | coordenadas do aterro | **Deve estar na CP** (o Edital já as traz: Lat 23°43'06"S / Long 47°36'56"O — ver Tipo 4) |
| 10 | Contrato, Cláusula 1, item 15, l. 223-226 | "ENTIDADE REGULADORA: é a [•]... cuja delegação foi autorizada pela Lei Municipal n° [•] e pelo convênio firmado com o MUNICÍPIO em [•]" | nome, lei e data do convênio | **Deve estar na CP** |
| 11 | Contrato, Cláusula 1, item 19, l. 268 | "LICITAÇÃO: é a Concorrência Pública nº [•]" | nº da licitação | Legítimo preencher depois |
| 12 | Contrato, Cláusula 8, item 1, l. 661-662 | "valor do presente CONTRATO... é de R$ [• valor a ser calculado de acordo com a proposta vencedora]" | valor do contrato | Legítimo preencher depois |
| 13 | Contrato, Cláusula 9, item 3, l. 683-685 | "capital subscrito mínimo da CONCESSIONÁRIA... é de R$ [• valor a ser calculado...]" | capital mínimo | **Deve estar na CP** (o Edital o fixa em R$ 4.715.904,40 — item 204) |
| 14 | Contrato, Cláusula 23, item 1, l. 2435-2500 | Tabela "CONTRAPRESTAÇÃO MENSAL" anos 1 a 30 — todas as 30 células = "[•]" | cronograma de contraprestação | Legítimo preencher depois (decorre da proposta) |
| 15 | Contrato, Cláusula 32, l. 3756 | "valor mínimo de R$ [•] ([•]), equivalente a 5% (cinco por cento) do valor do..." | valor da garantia de execução | **Deve estar na CP** (o Edital o fixa em R$ 28.306.758,90 — item 208) |
| 16 | Contrato, Cláusula 33, l. 3919 | "[NOME DA ENTIDADE REGULADORA]" | nome do regulador | **Deve estar na CP** |
| 17 | Contrato, Cláusula 36/compartilhamento, l. 4032-4037 | "ENTIDADE REGULADORA, [•]% ([•]) de [•] referente ao exercício anterior... até o [•] dia do mês" | percentual e prazo da taxa de regulação | **Deve estar na CP** (parâmetro econômico essencial — ver Tipo 6) |
| 18 | Contrato, Cláusula 50 (Comunicações), l. 6326-6330 | "PODER CONCEDENTE: [•]"; "CONCESSIONÁRIA: [•]"; "ENTIDADE REGULADORA: [•]" | endereços para comunicação | Parcialmente: endereço do Poder Concedente/Regulador **deve estar na CP** |
| 19 | Contrato, fecho, l. 6413 | "Salto de Pirapora, [•] de [•] de [•]." | data | Legítimo preencher depois |
| 20 | Contrato, fecho, l. 6416-6439 | linhas de assinatura "______________" | assinaturas | Legítimo preencher depois |

**Síntese:** os campos das linhas 7, 9, 10, 13, 15, 16, 17 e parcialmente 4, 5 e 18 **deveriam constar preenchidos** na Minuta do Contrato anexa à CP, porque o próprio Edital já contém os respectivos dados (ARSESP, coordenadas, valores). Manter `[•]` na minuta enquanto o Edital traz o valor cria contradição documento↔documento (Tipo 4) e impede o licitante de conhecer com segurança o regime contratual.

---

## TIPO 3 — INCONSISTÊNCIAS ENTRE DOCUMENTOS (Edital ↔ Contrato)

### 3.1. ENTIDADE REGULADORA: definida no Edital, em branco no Contrato — *GRAVE*
- **Edital, Seção II, def. (p. 11):** "ENTIDADE REGULADORA: é a **Agência Reguladora de Serviços Públicos do Estado de São Paulo (ARSESP)**..."
- **Contrato, Cláusula 1, item 15 (l. 223):** "ENTIDADE REGULADORA: é a **[•]**..., cuja delegação foi autorizada pela Lei Municipal n° **[•]** e pelo convênio firmado com o MUNICÍPIO em **[•]**"; e Cláusula 33 (l. 3919): "[NOME DA ENTIDADE REGULADORA]".
- **Natureza:** contradição/lacuna entre documentos: o Edital nomeia a ARSESP, mas a minuta contratual deixa o nome, a lei de delegação e a data do convênio em branco. O licitante não consegue confirmar, pelo Contrato, se o regulador é mesmo a ARSESP nem sob qual instrumento de delegação.
- **Correção:** preencher a Cláusula 1, item 15, e a Cláusula 33 com "ARSESP", indicando a lei municipal de delegação e a data do convênio.

### 3.2. Modalidade da licitação: "Concorrência Presencial" (Edital) vs. "Concorrência Pública" (Contrato) — *GRAVE*
- **Edital (capa, item 15, def. de LICITAÇÃO — p. 12):** "LICITAÇÃO: é a **Concorrência Presencial** nº 001/2026..."
- **Contrato (preâmbulo, l. 53 e Cláusula 1, item 19, l. 268):** "**CONCORRÊNCIA PÚBLICA** N° [•]"; "LICITAÇÃO: é a **Concorrência Pública** nº [•]..."
- **Natureza:** discrepância terminológica sobre a própria modalidade do certame entre o Edital e o Contrato que dele deriva. Sob a Lei 14.133/2021 a modalidade é "concorrência"; a adjetivação "Presencial"/"Pública" diverge entre os instrumentos.
- **Correção:** uniformizar para "Concorrência Presencial nº 001/2026" no Contrato.

### 3.3. Coordenadas do ATERRO SANITÁRIO: preenchidas no Edital, em branco no Contrato
- **Edital, def. (p. 9):** "ATERRO SANITÁRIO... localizado nas coordenadas geográficas Latitude: 23°43'06" S e Longitude: 47°36'56" O..."
- **Contrato, Cláusula 1, item 3 (l. 125):** "...localizado nas coordenadas geográficas **[•]**..."
- **Natureza:** lacuna no Contrato para dado já definido no Edital.
- **Correção:** transcrever as coordenadas no Contrato.

### 3.4. Capital mínimo da SPE e valor da garantia: fixados no Edital, em branco no Contrato
- **Edital:** capital subscrito mínimo R$ 4.715.904,40 (item 204); garantia de execução R$ 28.306.758,90 (item 208).
- **Contrato:** Cláusula 9, item 3 (R$ [•]) e Cláusula 32 (R$ [•]).
- **Natureza:** o Contrato remete a valores que o Edital já fixa, criando risco de divergência futura e impedindo conferência.
- **Correção:** transcrever os valores (e harmonizá-los com a correção do Tipo 1).

### 3.5. Citação legal da Lei de Concessões: "8.987/15" (errada) vs. "8.987/95"
- **Contrato, Cláusula 22, item 3 (l. 2412):** "regras de reajuste e revisão previstas na Lei federal nº **8.987/15** e na Lei federal nº 11.079/2004".
- **Natureza:** erro material grave de remissão legislativa — a Lei de Concessões é a **Lei nº 8.987/1995**. Não existe "Lei 8.987/15". Todas as demais 7 citações no Contrato e as 2 no Edital usam corretamente "8.987/95".
- **Correção:** corrigir para "8.987/95".

### 3.6. Anexos do Contrato (letras A-F) ↔ Anexos do Edital (romanos I-XI) — risco de remissão cruzada
- **Contrato, Cláusula 1, item 30 (l. 340):** "PROPOSTA COMERCIAL... constante do **Anexo B** deste CONTRATO"; item 31 (l. 346): "PROPOSTA TÉCNICA... constante do **Anexo C** deste CONTRATO".
- **Contrato, Cláusula 3 (l. 472-491):** Anexo A (Edital), B (Proposta Comercial), C (Proposta Técnica), D (Atos constitutivos), E (Contrato de Vinculação de Receitas), F (Termo de Recebimento do Aterro).
- **Natureza:** os sistemas de numeração não se correspondem (ex.: o "Anexo VIII" do Edital — a própria minuta — vira parte do "Anexo A" do Contrato; o Termo de Recebimento do Aterro é "Anexo XI" no Edital e "Anexo F" no Contrato). Não há erro de conteúdo, mas a ausência de tabela de equivalência é fonte potencial de confusão. **A Matriz de Riscos (Anexo IX do Edital) não consta da lista de anexos do Contrato (A-F)**, embora seja referida na Cláusula 28, item ... ("matriz de riscos constante do Anexo IX ao EDITAL", l. 3117) — ou seja, o Contrato a trata como anexo do Edital, não como anexo próprio.
- **Correção:** inserir tabela de correspondência Edital↔Contrato e confirmar que a remissão à Matriz de Riscos é sempre "Anexo IX do EDITAL".

---

## TIPO 4 — DISCREPÂNCIAS TERMINOLÓGICAS

### 4.1. "RECEITAS EXTRAORDINÁRIAS" (definida) vs. "Receitas Acessórias" (usada no Termo de Referência)
- **Termo definido — Edital, Seção II (p. 12) e Contrato, Cláusula 1, item 33:** "**RECEITAS EXTRAORDINÁRIAS**: são as receitas alternativas, complementares, acessórias ou oriundas de projetos associados, referidas no artigo 11 da Lei federal nº 8.987/95..."
- **Uso divergente — Edital, Anexo IV – Termo de Referência, item 7 (p. 175):** "**IDENTIFICAÇÃO DAS RECEITAS ACESSÓRIAS**... Estas são chamadas comumente de **Receitas Acessórias**... A possibilidade de geração de **Receitas Acessórias** configura-se em um elemento fundamental..."
- **Natureza:** o conceito definido em maiúsculas é "RECEITAS EXTRAORDINÁRIAS" (14 ocorrências no Contrato, 4 no corpo do Edital), mas o Anexo IV usa "Receitas Acessórias" (3 ocorrências), termo não definido no glossário. Discrepância terminológica para a mesma figura jurídica.
- **Correção:** padronizar para "RECEITAS EXTRAORDINÁRIAS" no Anexo IV, ou incluir nota de equivalência.

### 4.2. "GARANTIA DE ADIMPLEMENTO DA PPP" vs. "GARANTIA DE PAGAMENTO DA PPP" — *MODERADO/GRAVE*
- **Termo definido e dominante — Contrato, Cláusula 1, item 16 (l. 230)** e título da **Cláusula 24**: "**GARANTIA DE ADIMPLEMENTO DA PPP**" (9 ocorrências).
- **Uso divergente — Contrato, Cláusula 1, item 32 (def. de RECEITAS, l. 355):** "...para a constituição e manutenção da **GARANTIA DE PAGAMENTO DA PPP**..." (2 ocorrências).
- **Natureza:** dois nomes diferentes para o mesmo instrumento de garantia, um deles ("PAGAMENTO") sequer está definido. A definição de RECEITAS remete a um termo inexistente no glossário.
- **Correção:** uniformizar para "GARANTIA DE ADIMPLEMENTO DA PPP".

---

## TIPO 5 — REFERÊNCIAS CRUZADAS QUEBRADAS / ERROS DE WORD

### 5.1. "item 0" — remissão de campo Word não resolvida — *GRAVE*
- **Edital, item 155 (l. 2459):** "Na data prevista no aviso mencionado **no item 0**, em sessão pública, serão [abertos os ENVELOPES 3]..."
- **Natureza:** clássico resíduo de campo de referência cruzada do Word que não resolveu (rendeu "0"). O leitor não sabe a qual item o procedimento de abertura do Envelope 3 se reporta.
- **Correção:** substituir "item 0" pelo número correto do item que designa data/hora/local da sessão.

### 5.2. Remissão da Garantia de Execução ao "item 13" com valor que não fecha
- Já tratado em **1.2/1.3** (a remissão "previsto no item 13" aponta para o valor que não corresponde ao percentual declarado).

---

## TIPO 6 — LACUNAS (obrigações/parâmetros sem definição; matéria essencial remetida a campo em branco)

### 6.1. Taxa de regulação / compartilhamento com a ENTIDADE REGULADORA sem percentual nem prazo — *GRAVE*
- **Contrato, Cláusula 36 (Compartilhamento de Ganhos), l. 4032-4037:** "...à ENTIDADE REGULADORA, **[•]% ([•])** de **[•]** referente ao exercício anterior... mediante documento de cobrança, até o **[•]** dia do mês."
- **Natureza:** parâmetro econômico essencial (alíquota da taxa de regulação/compartilhamento, base de cálculo e prazo de recolhimento) integralmente em branco. Trata-se de obrigação pecuniária recorrente da Concessionária sem qualquer quantificação — impede a elaboração do Plano de Negócios e a precificação da proposta.
- **Correção:** fixar percentual, base e dia de vencimento já na CP.

### 6.2. Índice de reajuste não declarado no Edital
- **Contrato, Cláusula 24 (l. 2589) e Cláusula 25 (l. 2837):** reajuste/correção pelo **IPCA-IBGE**.
- **Edital, Seção IX (Reajuste):** menciona a sistemática de reajuste, mas o índice (IPCA) aparece expresso apenas no Contrato.
- **Natureza:** lacuna de coerência — o índice de reajuste, parâmetro central de equilíbrio, deveria estar explícito também no corpo do Edital/Anexo II para orientar as projeções das propostas.
- **Correção:** explicitar o IPCA-IBGE no Edital/Anexo II.

### 6.3. Definição truncada de "DATA DE ENTREGA DOS ENVELOPES 1, 2 e 3"
- **Edital, Seção II, def. (p. 9-10):** "DATA DE ENTREGA DOS ENVELOPES 1, 2 e 3: é até o dia 26 de julho de 2026, **entre as 17 horas**, data e período nos quais deverão ser entregues..."
- **Comparar com Edital, item 5 (l. 205):** "...até o dia 26 de julho de 2026, **entre as 08 horas e 17 horas**."
- **Natureza:** frase truncada na definição ("entre as 17 horas" — falta o início do intervalo "08 horas e"), inconsistente com o item operativo 5. Defeito de redação que afeta segurança quanto ao horário-limite de entrega. *(Nota acessória: 26 de julho de 2026 é domingo; a sessão de abertura é em 27/07/2026, segunda-feira, às 09h — conferir se a entrega física em domingo é intencional.)*
- **Correção:** corrigir a definição para "entre as 08 horas e 17 horas".

---

## TIPO 7 — ERROS DE REDAÇÃO MENORES

### 7.1. Definição de NORMAS DE REGULAÇÃO truncada/agramatical (Contrato)
- **Contrato, Cláusula 1, item 22 (l. 282-287):** "NORMAS DE REGULAÇÃO: são as normas de regulação editadas pela ENTIDADE REGULADORA **ente regulador que porventura venha a substituí-lo** e as normas de referência..."
- **Natureza:** falta a conjunção/preposição ("...pela ENTIDADE REGULADORA **ou pelo** ente regulador que porventura venha a substituí-la..."). Erro de concordância e de coesão que prejudica o sentido jurídico.
- **Correção:** "...editadas pela ENTIDADE REGULADORA ou pelo ente regulador que porventura venha a substituí-la, e as normas de referência...".

### 7.2. Resíduo "DAAE" — copy/paste de outro edital — *GRAVE (revela modelo importado)*
- **Edital, Anexo I – Modelos de Cartas e Declarações (l. 3460):** linha de assinatura "[Assinatura do representante **do DAAE**]".
- **Natureza:** "DAAE" (autarquia de água/esgoto típica de outros municípios, p.ex. Araraquara) não tem relação com Salto de Pirapora nem com o objeto (resíduos sólidos). É resíduo de modelo reaproveitado de outro certame; em todos os demais modelos a assinatura é "[Assinatura do representante legal]".
- **Correção:** substituir por designação correta do órgão municipal (ex.: "representante do MUNICÍPIO / Prefeitura").

### 7.3. "R$ R$" duplicado
- **Edital, Anexo II (l. 4271):** "...máximo admitido é de **R$ R$** 566.135.178,00...".
- **Natureza:** erro de digitação (símbolo de moeda duplicado).
- **Correção:** remover a duplicidade.

### 7.4. Definição de ENTIDADE REGULADORA no Edital fala "neste CONTRATO"
- **Edital, Seção II, def. (p. 11):** "ENTIDADE REGULADORA: é a ARSESP... nos termos definidos no EDITAL e **neste CONTRATO**."
- **Natureza:** dentro do Edital a expressão "neste CONTRATO" é imprópria (o instrumento é o EDITAL). Indica colagem da definição da minuta contratual.
- **Correção:** "...nos termos definidos no EDITAL e no CONTRATO."

### 7.5. Repetição/duplicidade de itens numerados no corpo do Edital
- **Edital, corpo:** a sequência de itens numerados apresenta repetições pontuais (ex.: aparição dupla de "33" e ressurgimentos de "14" e "5" fora de sequência na varredura automática), provavelmente reinícios de listas aninhadas na conversão do PDF.
- **Natureza:** anomalia de numeração a conferir no original; pode ou não ser artefato de extração. Não foram encontradas cláusulas vazias no Contrato (Cláusulas 1 a 52 presentes, tituladas e em sequência contínua).
- **Correção:** revisar a numeração de itens no Word original do Edital.

---

## RESUMO DOS DEFEITOS MAIS GRAVES

1. **Valor do CONTRATO em duplicidade e incoerente** (R$ 558.596.000,00 no item 13 vs. R$ 566.135.178,00 no Anexo II), com **garantia de execução (R$ 28.306.758,90), capital social de qualificação (R$ 56.613.517,80) e capital subscrito da SPE (R$ 4.715.904,40) calculados sobre bases que não fecham com os itens a que remetem** (Tipo 1) — afeta diretamente desclassificação de propostas e dimensionamento de garantias.
2. **ENTIDADE REGULADORA**: o Edital nomeia a ARSESP, mas a Minuta do Contrato deixa nome, lei de delegação, convênio e endereços em branco (Tipo 3.1) — e a taxa de regulação da Cláusula 36 está com percentual/base/prazo totalmente em branco (Tipo 6.1).
3. **Divergência de modalidade** entre Edital ("Concorrência Presencial") e Contrato ("Concorrência Pública") (Tipo 3.2).
4. **Citação legal errada** "Lei 8.987/15" em vez de 8.987/95 (Tipo 3.5).
5. **Termos não uniformes**: "GARANTIA DE ADIMPLEMENTO DA PPP" vs. "GARANTIA DE PAGAMENTO DA PPP" (não definido) e "RECEITAS EXTRAORDINÁRIAS" vs. "Receitas Acessórias" (Tipo 4).
6. **Referência cruzada quebrada "item 0"** no procedimento de abertura do Envelope 3 (Tipo 5.1) e **resíduo "DAAE"** de edital importado (Tipo 7.2).
7. **Numerosos placeholders `[•]` na minuta contratual** que deveriam estar preenchidos por já constarem do Edital (coordenadas, valores, regulador) (Tipo 2).
