# Relatório de Atividade: Classificador ADALINE (Válvulas)

**Disciplina:** Lab. Inteligência Artificial  
**Instituição:** CEFET-MG - Campus VIII  
**Algoritmo:** Regra Delta (Minimização do Erro Quadrático Médio)  

---

## 1. Resultados dos Treinamentos (ADALINE)

Foram executados 5 treinamentos para a rede ADALINE com taxa de aprendizado $\eta = 0.0025$ e precisão $\epsilon = 10^{-6}$. Os pesos iniciais foram definidos aleatoriamente entre 0 e 1.

| Treinamento | Vetor de Pesos Final $[w_0, w_1, w_2, w_3, w_4]$ | Épocas |
| :--- | :--- | :---: |
| 1º (T1) | $[-1.46794245, 1.44611668, 1.39317012, -0.47803670, -1.05363922]$ | 912 |
| 2º (T2) | $[-1.46787664, 1.44603125, 1.39304314, -0.47813806, -1.05356127]$ | 910 |
| 3º (T3) | $[-1.46785123, 1.44610468, 1.39312773, -0.47796593, -1.05360844]$ | 921 |
| 4º (T4) | $[-1.46792221, 1.44598594, 1.39299986, -0.47827517, -1.05353938]$ | 863 |
| 5º (T5) | $[-1.46781894, 1.44601601, 1.39300675, -0.47810843, -1.05353626]$ | 884 |

---

## 2. Classificação das Amostras de Teste
Aplicação dos 5 modelos treinados para identificar o destino dos sinais ruidosos (Válvula A: -1 / Válvula B: +1).

| Amostra | x1 | x2 | x3 | x4 | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0.9694 | 0.6909 | 0.4334 | 3.4965 | **-1** | **-1** | **-1** | **-1** | **-1** |
| 2 | 0.5427 | 1.3832 | 0.6390 | 4.0352 | **-1** | **-1** | **-1** | **-1** | **-1** |
| 3 | 0.6081 | -0.9196 | 0.5925 | 0.1016 | **1** | **1** | **1** | **1** | **1** |
| 4 | -0.1618 | 0.4694 | 0.2030 | 3.0117 | **-1** | **-1** | **-1** | **-1** | **-1** |
| 5 | 0.1870 | -0.2578 | 0.6124 | 1.7749 | **-1** | **-1** | **-1** | **-1** | **-1** |
| 6 | 0.4891 | -0.5276 | 0.4378 | 0.6439 | **1** | **1** | **1** | **1** | **1** |
| 7 | 0.3777 | 2.0149 | 0.7423 | 3.3932 | **1** | **1** | **1** | **1** | **1** |
| 8 | 1.1498 | -0.4067 | 0.2469 | 1.5866 | **1** | **1** | **1** | **1** | **1** |
| 9 | 0.9325 | 1.0950 | 1.0359 | 3.3591 | **1** | **1** | **1** | **1** | **1** |
| 10 | 0.5060 | 1.3317 | 0.9222 | 3.7174 | **-1** | **-1** | **-1** | **-1** | **-1** |
| 11 | 0.0497 | -2.0656 | 0.6124 | -0.6585 | **-1** | **-1** | **-1** | **-1** | **-1** |
| 12 | 0.4004 | 3.5369 | 0.9766 | 5.3532 | **1** | **1** | **1** | **1** | **1** |
| 13 | -0.1874 | 1.3343 | 0.5374 | 3.2189 | **-1** | **-1** | **-1** | **-1** | **-1** |
| 14 | 0.5060 | 1.3317 | 0.9222 | 3.7174 | **-1** | **-1** | **-1** | **-1** | **-1** |
| 15 | 1.6375 | -0.7911 | 0.7537 | 0.5515 | **1** | **1** | **1** | **1** | **1** |

---

## 3. Análise Teórica

### Questão: Embora o número de épocas varie, por que os pesos finais são praticamente iguais?
Isso ocorre porque o algorithm Adaline utiliza uma superfície de erro quadrática que possui apenas um único ponto de **mínimo global**. Independentemente de onde os pesos iniciem (dentro da faixa aleatória de 0 a 1), o gradiente descendente da Regra Delta sempre conduzirá o vetor de pesos em direção ao mesmo fundo do "vale" de erro. A variação no número de épocas deve-se apenas à distância inicial entre o ponto de partida aleatório e esse mínimo global, mas a convergência final será sempre para a mesma solução ótima.