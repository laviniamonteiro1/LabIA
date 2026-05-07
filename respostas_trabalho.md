# Relatório de Atividade: Classificador Perceptron (Óleo)

**Disciplina:** Lab. Inteligência Artificial  
**Instituição:** CEFET-MG - Campus VIII  
**Algoritmo:** Regra de Hebb Supervisionada  

---

## 1 e 2 . Resultados dos Treinamentos
Foram realizados 5 processos de treinamento com inicialização de pesos aleatória (entre 0 e 1) e taxa de aprendizagem $\eta = 0.01$.

| Treinamento | Vetor de Pesos Inicial $[w_0, w_1, w_2, w_3]$ | Vetor de Pesos Final $[w_0, w_1, w_2, w_3]$ | Épocas |
| :--- | :--- | :--- | :---: |
| 1º (T1) | $[0.3745, 0.9507, 0.7320, 0.5987]$ | $[-3.1655, 1.6028, 2.5471, -0.7529]$ | 407 |
| 2º (T2) | $[0.8231, 0.0261, 0.2108, 0.6184]$ | $[-2.8769, 1.4151, 2.3711, -0.6705]$ | 398 |
| 3º (T3) | $[0.0338, 0.4891, 0.8461, 0.4114]$ | $[-3.0862, 1.5745, 2.4837, -0.7374]$ | 359 |
| 4º (T4) | $[0.1067, 0.6843, 0.5350, 0.3692]$ | $[-3.0933, 1.5669, 2.4888, -0.7368]$ | 320 |
| 5º (T5) | $[0.2752, 0.6392, 0.6239, 0.7780]$ | $[-2.9048, 1.4265, 2.3974, -0.6775]$ | 427 |

## 3. Classificação Automática
Abaixo, a tabela com as classes preditas para as 10 amostras de teste usando os pesos obtidos nos treinamentos acima:

| Amostra | x1 | x2 | x3 | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | -0.3565 | 0.0620 | 5.9891 | -1 | -1 | -1 | -1 | -1 |
| 2 | -0.7842 | 1.1267 | 5.5912 | 1 | 1 | 1 | 1 | 1 |
| 3 | 0.3012 | 0.5611 | 5.8234 | 1 | 1 | 1 | 1 | 1 |
| 4 | 0.7757 | 1.0648 | 8.0677 | 1 | 1 | 1 | 1 | 1 |
| 5 | 0.1570 | 0.8028 | 6.3040 | 1 | 1 | 1 | 1 | 1 |
| 6 | -0.7014 | 1.0316 | 3.6005 | 1 | 1 | 1 | 1 | 1 |
| 7 | 0.3748 | 0.1536 | 6.1537 | -1 | -1 | -1 | -1 | -1 |
| 8 | -0.6920 | 0.9404 | 4.4058 | 1 | 1 | 1 | 1 | 1 |
| 9 | -1.3970 | 0.7141 | 4.9263 | -1 | -1 | -1 | -1 | -1 |
| 10 | -1.8842 | -0.2805 | 1.2548 | -1 | -1 | -1 | -1 | -1 |

---
### 4. Por que o número de épocas varia a cada execução?
O número de épocas varia porque o vetor de pesos é inicializado com valores aleatórios no início de cada treinamento. Como o algoritmo começa em pontos diferentes do espaço de busca, a distância necessária para os pesos atingirem o hiperplano de separação ideal (onde o erro é zero) muda a cada vez. Se os pesos iniciais estiverem "mais perto" da solução, a convergência ocorre em menos épocas.

### 5. Qual a principal limitação do perceptron?
A principal limitação do Perceptron de camada única é que ele só consegue resolver problemas que são **linearmente separáveis**. Isso significa que ele só funciona se for possível separar as classes com uma linha reta (em 2D) ou um hiperplano plano (em 3D ou mais). Se os dados possuírem uma distribuição não-linear complexa, o algoritmo nunca atingirá o erro zero.