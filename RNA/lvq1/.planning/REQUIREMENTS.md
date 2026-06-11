# Requisitos do Sistema - Rede LVQ-1 (Learning Vector Quantization)

## 1. Descrição do Problema
O objetivo é classificar curvas de demanda (perfis de potência elétrica) com base nas medições realizadas das 7h às 12h. A classificação nas primeiras horas permite o planejamento operacional do sistema elétrico para o restante do dia.

## 2. Especificações da Arquitetura
* **Vetor de Entrada (x):** 6 dimensões (representando a potência medida em 6 horários: 7h, 8h, 9h, 10h, 11h, 12h).
* **Camada Competitiva (Saída):** 4 neurônios, correspondendo exatamente às 4 classes (perfis) de demanda pré-definidas.
* **Taxa de Aprendizagem ($\alpha$):** 0.05.
* **Algoritmo:** LVQ-1 (Aprendizado Supervisionado Competitivo).

## 3. Dinâmica de Atualização dos Pesos (LVQ-1)
Para cada amostra de treinamento, a rede encontra o neurônio vencedor (menor distância Euclidiana). A atualização depende da classe do vencedor ($C_w$) e da classe real da amostra ($C_x$):
* **Se a classificação for correta ($C_w = C_x$):** O peso é "puxado" na direção da amostra (reforço positivo).
  $$W_{nova} = W_{atual} + \alpha (x - W_{atual})$$
* **Se a classificação for incorreta ($C_w \neq C_x$):** O peso é "empurrado" para longe da amostra (punição).
  $$W_{nova} = W_{atual} - \alpha (x - W_{atual})$$

## 4. Entregáveis Exigidos
1. Treinamento da rede LVQ-1 com as 16 amostras fornecidas.
2. Classificação de 8 amostras (dias) inéditas (Dados de Teste) para determinação de suas respectivas classes.