# Resoluções - Atividade RBF 2

**Instituição:** Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG)  
**Campus:** VIII – Varginha  
**Curso:** Bacharelado em Sistemas de Informação  
**Disciplina:** Laboratório de Inteligência Artificial  
**Professor:** Lázaro Eduardo da Silva  
**Data:** 20/05/2026  
**Aluna:** Lavínia  

---

### **Questão 1**
**Execute 3 treinamentos para cada topologia de rede RBF definida anteriormente ($N_1 = 5$, $N_1 = 10$ e $N_1 = 15$), inicializando a matriz de pesos da camada de saída com valores aleatórios entre 0 e 1. Se for o caso, reinicie o gerador de números aleatórios em cada treinamento de tal forma que os elementos das matrizes de pesos iniciais não sejam os mesmos. Registre os resultados finais desses 3 treinamentos para cada uma das três topologias de rede na tabela de histórico de convergência.**

#### **Resposta 1:**
Abaixo constam os registros de Erro Quadrático Médio (EQM) e número de épocas completadas para todas as 9 simulações executadas:

| Treinamento | Rede 1 ($N_1 = 5$) | Rede 1 ($N_1 = 5$) | Rede 2 ($N_1 = 10$) | Rede 2 ($N_1 = 10$) | Rede 3 ($N_1 = 15$) | Rede 3 ($N_1 = 15$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| | **EQM** | **Épocas** | **EQM** | **Épocas** | **EQM** | **Épocas** |
| **1º (T1)** | `0.00466` | `150000` | `0.00289` | `150000` | `0.00205` | `150000` |
| **2º (T2)** | `0.00466` | `150000` | `0.00289` | `150000` | `0.00205` | `150000` |
| **3º (T3)** | `0.00466` | `150000` | `0.00289` | `150000` | `0.00205` | `150000` |

*Nota técnica:* Todas as redes atingiram o limite de segurança de 150.000 épocas. Isso ocorre porque a precisão estrita de $\epsilon = 10^{-7}$ exige um nível sutil de ajuste que ultrapassa a capacidade de aproximação das arquiteturas propostas, estacionando nos menores erros possíveis de cada espaço dimensional.

---

### **Questão 2**
**Para todos os treinamentos efetuados no item anterior, faça a validação da rede em relação aos valores desejados apresentados na tabela de teste. Forneça para cada treinamento o erro relativo médio (%) entre os valores desejados e os valores fornecidos pela rede em relação a todos os padrões de teste. Obtenha também a respectiva variância (%).**

#### **Resposta 2:**
Os resultados de aproximação contínua da quantidade de gasolina ($y$) para as 15 amostras inéditas de teste foram mapeados na matriz abaixo:

| Amostra | Desejado ($d$) | R1_T1 | R1_T2 | R1_T3 | R2_T1 | R2_T2 | R2_T3 | R3_T1 | R3_T2 | R3_T3 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | 0.5965 | 0.6036 | 0.6036 | 0.6036 | 0.6688 | 0.6688 | 0.6688 | 0.6557 | 0.6557 | 0.6557 |
| **02** | 0.6790 | 0.7596 | 0.7596 | 0.7596 | 0.6772 | 0.6772 | 0.6772 | 0.6835 | 0.6835 | 0.6835 |
| **03** | 0.4662 | 0.4557 | 0.4557 | 0.4557 | 0.4823 | 0.4823 | 0.4823 | 0.4533 | 0.4533 | 0.4533 |
| **04** | 0.5012 | 0.4466 | 0.4466 | 0.4466 | 0.5111 | 0.5111 | 0.5111 | 0.4936 | 0.4936 | 0.4936 |
| **05** | 0.6810 | 0.6921 | 0.6921 | 0.6921 | 0.6729 | 0.6729 | 0.6729 | 0.6782 | 0.6782 | 0.6782 |
| **06** | 0.5643 | 0.5820 | 0.5820 | 0.5820 | 0.5852 | 0.5852 | 0.5852 | 0.5427 | 0.5427 | 0.5427 |
| **07** | 0.5875 | 0.5371 | 0.5371 | 0.5371 | 0.6107 | 0.6107 | 0.6107 | 0.5754 | 0.5754 | 0.5754 |
| **08** | 0.7853 | 0.8293 | 0.8293 | 0.8293 | 0.8114 | 0.8114 | 0.8114 | 0.7741 | 0.7741 | 0.7741 |
| **09** | 0.8506 | 0.9105 | 0.9105 | 0.9105 | 0.7956 | 0.7956 | 0.7956 | 0.8190 | 0.8190 | 0.8190 |
| **10** | 0.6165 | 0.5729 | 0.5729 | 0.5729 | 0.7262 | 0.7262 | 0.7262 | 0.6647 | 0.6647 | 0.6647 |
| **11** | 0.4957 | 0.4666 | 0.4666 | 0.4666 | 0.4892 | 0.4892 | 0.4892 | 0.5263 | 0.5263 | 0.5263 |
| **12** | 0.6625 | 0.6536 | 0.6536 | 0.6536 | 0.6636 | 0.6636 | 0.6636 | 0.5998 | 0.5998 | 0.5998 |
| **13** | 0.4402 | 0.3862 | 0.3862 | 0.3862 | 0.4377 | 0.4377 | 0.4377 | 0.4755 | 0.4755 | 0.4755 |
| **14** | 0.7663 | 0.6448 | 0.6448 | 0.6448 | 0.7398 | 0.7398 | 0.7398 | 0.7540 | 0.7540 | 0.7540 |
| **15** | 0.7893 | 0.8594 | 0.8594 | 0.8594 | 0.8203 | 0.8203 | 0.8203 | 0.7987 | 0.7987 | 0.7987 |
| **ERM (%)**| — | **6.90%** | **6.90%** | **6.90%** | **4.25%** | **4.25%** | **4.25%** | **4.04%** | **4.04%** | **4.04%** |
| **Var (%)**| — | **19.10%**| **19.10%**| **19.10%**| **21.47%**| **21.47%**| **21.47%**| **10.43%**| **10.43%**| **10.43%**|

*Análise matemática dos desvios:* - O Erro Relativo Médio (ERM) foi calculado utilizando a formulação:
$$\text{ERM} = \frac{1}{N} \sum_{i=1}^{N} \left| \frac{d_i - y_i}{d_i} \right| \times 100\%$$
- A Variância da validação seguiu a dispersão dos erros relativos obtidos ponto a ponto.

---

### **Questão 3**
**Para cada uma das topologias apresentadas na tabela acima, considerando ainda o melhor treinamento {T1, T2 ou T3} realizado em cada uma delas, trace o gráfico dos valores de erro quadrático médio (EQM) em função de cada época de treinamento. Imprima os três gráficos numa mesma folha de modo não superpostos.**

#### **Resposta 3:**
Os três gráficos foram devidamente computados e plotados de forma vertical isolada (subplots independentes), utilizando escala logarítmica para o eixo Y a fim de evidenciar a suavização da curva de decréscimo do gradiente. 

O arquivo de imagem resultante foi exportado em alta definição com o nome de **`convergencia_rbf2.png`** e encontra-se salvo na raiz do diretório `rbf/rbf2`, cumprindo a exigência de não superposição espacial.

---

### **Questão 4**
**Por qual motivo os treinamentos $T_1$, $T_2$ e $T_3$ geraram predições e erros finais exatamente iguais para uma mesma topologia de rede, mesmo iniciando com matrizes de pesos aleatórias distintas?**

#### **Resposta 4:**
Este fenômeno expõe uma das propriedades matemáticas mais robustas da arquitetura Radial Basis Function (RBF). 

Ao contrário do Perceptron Multicamadas (PMC), onde o erro possui uma superfície hiperbólica repleta de mínimos locais complexos, a camada de saída de uma rede RBF configura-se como um **combinador estritamente linear**. Dado que o algoritmo *k-means* fixou os centros e as variâncias da camada escondida de forma idêntica e determinística antes do início do ajuste dos pesos, a otimização realizada pela Regra Delta passa a trabalhar sobre uma superfície de erro puramente **convexa** (formato de parábola). 

Em superfícies convexas, existe apenas um único Mínimo Global. Como o treinamento foi estendido por um número massivo de épocas (150.000), o gradiente descendente foi perfeitamente capaz de anular a influência da posição de partida (pesos iniciais aleatórios de $T_1, T_2, T_3$) e convergir exatamente para o mesmo conjunto de coeficientes ótimos globais para aquela distribuição espacial de centros.

---

### **Questão 5**
**Baseado nas análises dos itens acima, indique qual das topologias candidatas {Rede 1, Rede 2 ou Rede 3} e com qual configuração final de treinamento {T1, T2 ou T3} seria a mais adequada para este problema.**

#### **Resposta 5:**
A arquitetura mais adequada para o sistema de injeção eletrônica automotiva é a **Rede 3 ($N_1 = 15$ neurônios ocultos)**, associada a **qualquer uma de suas rodadas de treinamento ($T_1$, $T_2$ ou $T_3$)**, visto que convergiram para o mesmo nível de excelência.

**Justificativa Científica:**
1. **Poder de Aproximação Funcional:** A Rede 3 apresentou o menor Erro Quadrático Médio de treinamento (`0.0020466`), indicando que o acréscimo de neurônios radiais expandiu a capacidade da camada oculta de mapear a forte não-linearidade do motor.
2. **Superioridade na Validação de Teste:** No teste com dados inéditos, a Rede 3 obteve o menor Erro Relativo Médio da simulação, atingindo **`4.04%`** de desvio em comparação com os `4.25%` da Rede 2 e os expressivos `6.90%` de erro da Rede 1.
3. **Estabilidade e Confiabilidade Mecânica:** A Rede 3 demonstrou uma consistência muito maior ao registrar a menor variância de erro do experimento (**`10.43%`** contra `21.47%` da Rede 2). Uma variância baixa indica que o sistema comete desvios homogêneos e previsíveis, evitando picos abruptos de falta ou excesso de injeção de gasolina, o que é crítico para garantir a eficiência de combustão e evitar danos mecânicos ao motor em tempo-real.