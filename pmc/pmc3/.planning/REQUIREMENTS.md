# Requisitos - PMC 03 (Time Delay Neural Network)

### 1. Objetivo do Problema
- [cite_start]Prever a variação de preço de uma mercadoria no mercado de ações utilizando o histórico apresentado no Apêndice[cite: 2, 3].
- [cite_start]Utilizar a arquitetura Perceptron Multicamadas com topologia "Time Delay" (TDNN)[cite: 4].

### 2. Especificações das Redes
- [cite_start]**Rede 1:** 05 entradas ($p = 05$) com 10 neurônios na camada escondida ($N1 = 10$)[cite: 28].
- [cite_start]**Rede 2:** 10 entradas ($p = 10$) com 15 neurônios na camada escondida ($N1 = 15$)[cite: 29].
- [cite_start]**Rede 3:** 15 entradas ($p = 15$) com 25 neurônios na camada escondida ($N1 = 25$)[cite: 30].

### 3. Parâmetros de Treinamento
- [cite_start]**Algoritmo:** Backpropagation com Momentum[cite: 31].
- [cite_start]**Função de Ativação:** Logística (Sigmoid) para todos os neurônios[cite: 33].
- [cite_start]**Taxa de Aprendizado ($\eta$):** 0.1[cite: 33].
- [cite_start]**Fator de Momentum ($\alpha$):** 0.8[cite: 33].
- [cite_start]**Precisão ($\epsilon$):** $0.5 \times 10^{-6}$[cite: 33].
- [cite_start]**Pesos Iniciais:** Aleatórios entre 0 e 1, reiniciados a cada treinamento[cite: 32].

### 4. Critérios de Validação e Saídas
- [cite_start]Realizar 3 treinamentos (T1, T2, T3) para cada uma das três topologias[cite: 32].
- [cite_start]Validar a rede com as amostras de teste $t = 101$ a $120$[cite: 36, 39].
- [cite_start]Calcular o Erro Relativo Médio e a Variância para cada treinamento[cite: 37, 38].
- [cite_start]Gerar gráficos de EQM e de Valores Desejados vs. Estimados (não superpostos)[cite: 40, 41, 42, 43].
- [cite_start]Investigar os algoritmos Resilient-Propagation (RProp) e Levenberg-Marquardt (LM)[cite: 45, 46, 47].