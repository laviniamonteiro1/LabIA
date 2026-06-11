# Requisitos do Sistema - Rede de Kohonen (SOM)

## 1. Descrição do Problema
Análise de imperfeições no composto de borracha para fabricação de pneus com base em 3 grandezas físicas (x1, x2, x3). O objetivo é agrupar as amostras e identificar as assinaturas topológicas das classes de falha A, B e C.

## 2. Especificações da Arquitetura
* **Camada de Entrada:** 3 neurônios (correspondendo às variáveis x1, x2, x3).
* **Grid Topológico:** Bidimensional com dimensões 4x4 (Total de 16 neurônios na camada de saída).
* **Taxa de Aprendizado (eta):** Fixa em 0.001.
* **Vizinhança (Raio):** Igual a 1 (Métrica de distância topológica no grid).

## 3. Restrições do Dataset (Apêndice)
* **Amostras 001 a 020:** Pertencem à Classe A.
* **Amostras 021 a 060:** Pertencem à Classe B.
* **Amostras 061 a 120:** Pertencem à Classe C.

## 4. Entregáveis Exigidos
1. Mapa de ativação do grid indicando quais neurônios respondem a quais classes.
2. Predição/Classificação de 12 amostras de teste inéditas.
3. Demonstração matemática da regra de atualização de pesos via minimização do Erro Quadrático.