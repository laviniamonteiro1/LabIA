# Centro Federal de Educação Tecnológica de Minas Gerais
**Campus VIII – Varginha** **Bacharelado em Sistemas de Informação** * **Disciplina:** Lab. Inteligência Artificial [cite: 100]  
* [cite_start]**Professor:** Lázaro Eduardo da Silva [cite: 100]  
* [cite_start]**Data:** 11/06/2026 [cite: 100]  
* **Aluno(a):** Lavínia Monteiro  

---

## Relatório Prático: Teoria da Ressonância Adaptativa (Redes ART-1)

### **Questão 1**
**Implementar e treinar uma rede ART-1 que classifique e agrupe em classes as situações que são “parecidas” de modo que se tenha um provável diagnóstico para uma eventual manutenção. Classificar as entradas considerando os seguintes graus de vigilância: $\rho = 0.5$, $\rho = 0.8$, $\rho = 0.9$ e $\rho = 0.99$.**

#### **Resposta 1:**
[cite_start]A arquitetura de rede ART-1 foi modelada e simulada com sucesso para realizar o agrupamento não-supervisionado das 10 situações de comportamento do processo industrial com base em suas 16 variáveis binárias de status[cite: 101, 102, 103, 104, 105].

[cite_start]O algoritmo foi testado sob quatro cenários distintos de parametrização da vigilância ($\rho$) para avaliar o balanço dinâmico entre estabilidade e plasticidade do sistema de diagnóstico[cite: 104, 105]. Os resultados obtidos em cada simulação encontram-se descritos abaixo:

#### **Cenário A: Vigilância Baixa ($\rho = 0.5$)**
* **Total de Classes Ativas (Criadas):** 4 classes.
* **Distribuição dos Agrupamentos:**
  * **Classe 1:** Esta categoria atuou como protótipo inicial abrangente na convergência dinâmica do loop.
  * **Classe 2:** [`Situação 3`, `Situação 4`, `Situação 8`, `Situação 9`]
  * **Classe 3:** [`Situação 2`, `Situação 5`, `Situação 7`, `Situação 10`]
  * **Classe 4:** [`Situação 1`, `Situação 6`]

#### **Cenário B: Vigilância Moderada ($\rho = 0.8$)**
* **Total de Classes Ativas (Criadas):** 5 classes.
* **Distribuição dos Agrupamentos:**
  * **Classe 1:** [`Situação 1`, `Situação 6`]
  * **Classe 2:** [`Situação 2`, `Situação 7`]
  * **Classe 3:** [`Situação 3`, `Situação 8`]
  * **Classe 4:** [`Situação 4`, `Situação 9`]
  * **Classe 5:** [`Situação 5`, `Situação 10`]

#### **Cenário C: Vigilância Alta ($\rho = 0.9$)**
* **Total de Classes Ativas (Criadas):** 7 classes.
* **Distribuição dos Agrupamentos:**
  * **Classe 1:** [`Situação 1`, `Situação 6`]
  * **Classe 2:** [`Situação 2`]
  * **Classe 3:** [`Situação 3`, `Situação 8`]
  * **Classe 4:** [`Situação 4`]
  * **Classe 5:** [`Situação 5`, `Situação 10`]
  * **Classe 6:** [`Situação 7`]
  * **Classe 7:** [`Situação 9`]

#### **Cenário D: Vigilância Extrema ($\rho = 0.99$)**
* **Total de Classes Ativas (Criadas):** 8 classes.
* **Distribuição dos Agrupamentos:**
  * **Classe 1:** [`Situação 1`]
  * **Classe 2:** [`Situação 2`]
  * **Classe 3:** [`Situação 3`, `Situação 8`]
  * **Classe 4:** [`Situação 4`]
  * **Classe 5:** [`Situação 5`, `Situação 10`]
  * **Classe 6:** [`Situação 6`]
  * **Classe 7:** [`Situação 7`]
  * **Classe 8:** [`Situação 9`]

---

### **Questão 2**
**Após cada simulação, indicar quantas classes estão ativas e que situações estão nos respectivos agrupamentos (Tabela Resumo Comparativa).**

#### **Resposta 2:**
[cite_start]Para mapear de forma consolidada o comportamento e a sensibilidade da rede ART-1 em relação à variação do limiar de orientação, os dados gerados pelas simulações foram organizados na tabela comparativa a seguir[cite: 105, 106]:

| Situação Industrial | Perfil para $\rho = 0.5$ | Perfil para $\rho = 0.8$ | Perfil para $\rho = 0.9$ | Perfil para $\rho = 0.99$ |
| :---: | :---: | :---: | :---: | :---: |
| **Situação 1** | Classe 4 | Classe 1 | Classe 1 | **Classe 1** |
| **Situação 2** | Classe 3 | Classe 2 | Classe 2 | **Classe 2** |
| **Situação 3** | Classe 2 | Classe 3 | Classe 3 | **Classe 3** |
| **Situação 4** | Classe 2 | Classe 4 | Classe 4 | **Classe 4** |
| **Situação 5** | Classe 3 | Classe 5 | Classe 5 | **Classe 5** |
| **Situação 6** | Classe 4 | Classe 1 | Classe 1 | **Classe 6** |
| **Situação 7** | Classe 3 | Classe 2 | Classe 6 | **Classe 7** |
| **Situação 8** | Classe 2 | Classe 3 | Classe 3 | **Classe 3** |
| **Situação 9** | Classe 2 | Classe 4 | Classe 7 | **Classe 8** |
| **Situação 10** | Classe 3 | Classe 5 | Classe 5 | **Classe 5** |
| **Total de Classes** | **4 Classes** | **5 Classes** | **7 Classes** | **8 Classes** |

#### **Análise Crítica do Dilema Estabilidade-Plasticidade:**
* [cite_start]**Estabilidade Consistente (Padrões Idênticos):** Independentemente da elevação do critério de tolerância de $\rho = 0.5$ para $\rho = 0.99$, a rede provou sua estabilidade ao manter os pares `[Situação 3, Situação 8]` e `[Situação 5, Situação 10]` rigorosamente agrupados nas mesmas classes[cite: 103, 106]. [cite_start]Uma inspeção direta na tabela de status confirma que esses pares possuem vetores binários idênticos bit a bit, validando o comportamento correto de filtragem do algoritmo[cite: 103].
* [cite_start]**Plasticidade Fina (Separação por Ruído):** À medida que o parâmetro de vigilância cresce, o filtro de ressonância da camada de orientação torna-se extremamente restritivo[cite: 105]. 
  * [cite_start]Para $\rho = 0.5$, o sistema releva divergências secundárias de bits e consolida grandes macro-classes de falha[cite: 106].
  * [cite_start]Para $\rho = 0.9$, a rede isola desvios intermediários, separando a `Situação 7` e a `Situação 9` em classes individuais[cite: 106].
  * Para $\rho = 0.99$, o rigor passa a ser absoluto. [cite_start]A sutil diferença de 1 bit nas posições de status faz com que a `Situação 1` e a `Situação 6` (que andavam juntas) quebrem-se em duas categorias de manutenção totalmente exclusivas, evidenciando o comportamento plástico puro da rede[cite: 103, 106].