# Requisitos do Projeto: Classificador Perceptron (Óleo)

## 1. Descrição do Problema
O objetivo é automatizar a classificação de pureza de determinado óleo proveniente de um processo de destilação fracionada de petróleo. O óleo deve ser classificado em duas classes:
* **Classe C1**: Convenção valor **-1**.
* **Classe C2**: Convenção valor **+1**.

A classificação é baseada em três grandezas físico-químicas: **x1, x2 e x3**.

## 2. Arquitetura da Rede
O neurônio constituinte do perceptron possui as seguintes características:
* **Entradas**: $x_1, x_2, x_3$ e $x_0$ (bias).
* **Valor do Bias ($x_0$)**: $-1$.
* **Pesos**: $w_0$ (limiar de ativação $\theta$), $w_1, w_2, w_3$.
* **Função de Ativação**: $g(.)$ (degrau bipolar).
* **Algoritmo de Aprendizado**: Regra de Hebb supervisionada.
* **Taxa de Aprendizado ($\eta$)**: $0.01$.

## 3. Atividades Propostas

### 3.1. Treinamento da Rede
Executar **5 processos de treinamento** independentes. 
* **Inicialização**: Vetores de pesos iniciais com valores aleatórios entre **0 e 1**.
* **Variabilidade**: Reiniciar o gerador de números aleatórios em cada treinamento para garantir que os pesos iniciais sejam distintos.

#### Tabela de Registro de Treinamentos
| Treinamento | $w_0$ inicial | $w_1$ inicial | $w_2$ inicial | $w_3$ inicial | $w_0$ final | $w_1$ final | $w_2$ final | $w_3$ final | Épocas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1º (T1) | | | | | | | | | |
| 2º (T2) | | | | | | | | | |
| 3º (T3) | | | | | | | | | |
| 4º (T4) | | | | | | | | | |
| 5º (T5) | | | | | | | | | |

### 3.2. Classificação de Amostras
Após concluir os treinamentos, aplicar os modelos resultantes para classificar as amostras abaixo:

| Amostra | $x_1$ | $x_2$ | $x_3$ | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | -0.3565 | 0.0620 | 5.9891 | | | | | |
| 2 | -0.7842 | 1.1267 | 5.5912 | | | | | |
| 3 | 0.3012 | 0.5611 | 5.8234 | | | | | |
| 4 | 0.7757 | 1.0648 | 8.0677 | | | | | |
| 5 | 0.1570 | 0.8028 | 6.3040 | | | | | |
| 6 | -0.7014 | 1.0316 | 3.6005 | | | | | |
| 7 | 0.3748 | 0.1536 | 6.1537 | | | | | |
| 8 | -0.6920 | 0.9404 | 4.4058 | | | | | |
| 9 | -1.3970 | 0.7141 | 4.9263 | | | | | |
| 10 | -1.8842 | -0.2805 | 1.2548 | | | | | |

## 4. Questões Analíticas
1. Explique por que o número de épocas de treinamento varia a cada vez que executamos o treinamento do perceptron.
2. Qual a principal limitação do perceptron quando aplicado em problemas de classificação de padrões?