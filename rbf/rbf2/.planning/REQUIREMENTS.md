# Requisitos do Projeto - Atividade RBF 2

[cite_start]Mapeamento de especificações, restrições e metas para a implementação da rede Radial Basis Function (RBF) voltada à aproximação funcional de um sistema de injeção eletrônica automotiva[cite: 38, 40].

## 1. Mapeamento de Dados e Arquitetura
- [cite_start]**Entradas ($x_1, x_2, x_3$):** Três grandezas físicas contínuas que determinam o comportamento do motor.
- [cite_start]**Saída Desejada ($y$):** Quantidade real/contínua de gasolina a ser injetada em tempo-real (Problema de Aproximação Funcional)[cite: 38, 40, 42].
- **Volumetria do Dataset (Anexo):**
  - [cite_start]**Treinamento:** 150 amostras completas fornecidas no Anexo[cite: 64, 77, 78].
  - [cite_start]**Teste (Validação):** 15 amostras de teste pré-definidas na tabela de validação[cite: 70, 73].

## 2. Topologias Candidatas da Camada Oculta
[cite_start]Devem ser avaliadas e contrastadas três variações no número de neurônios da camada oculta ($N_1$)[cite: 41, 60]:
- [cite_start]**Rede 1:** RBF com $N_1 = 5$ neurônios radiais[cite: 61].
- [cite_start]**Rede 2:** RBF com $N_1 = 10$ neurônios radiais[cite: 62].
- [cite_start]**Rede 3:** RBF com $N_1 = 15$ neurônios radiais[cite: 63].

## 3. Restrições do Processo de Treinamento
- [cite_start]**Bateria de Testes:** Executar rigorosamente **3 treinamentos independentes (T1, T2, T3)** para cada uma das três topologias[cite: 66].
- [cite_start]**Inicialização de Pesos:** A matriz de pesos da camada de saída deve ser inicializada com valores aleatórios entre 0 e 1[cite: 66].
- [cite_start]**Garantia de Independência:** O gerador de números aleatórios deve ser reiniciado/reconfigurado a cada rodada para assegurar que os pesos iniciais de T1, T2 e T3 sejam estritamente diferentes[cite: 66].
- **Hiperparâmetros de Saída (Regra Delta):**
  - [cite_start]Taxa de Aprendizado ($\eta$): `0.01`[cite: 67].
  - [cite_start]Critério de Parada (Precisão $\epsilon$): `10^-7` ($1.0 \times 10^{-7}$)[cite: 67].

## 4. Métricas de Validação e Saídas do Relatório
- [cite_start]**Métricas por Treinamento:** Coletar o Erro Quadrático Médio (EQM) final e o número total de épocas de cada uma das 9 rodadas[cite: 68, 69].
- [cite_start]**Desempenho de Teste:** Calcular o **Erro Relativo Médio (%)** e a **Variância (%)** para cada um dos 3 treinamentos das 3 redes sobre as 15 amostras inéditas[cite: 71, 72, 73].
- [cite_start]**Análise Gráfica:** Plotar a curva de evolução do EQM em função das épocas para o *melhor* treinamento de cada topologia[cite: 74]. [cite_start]Os 3 gráficos devem ser impressos de forma não superposta[cite: 75].
- [cite_start]**Tomada de Decisão:** Indicar textualmente qual arquitetura e rodada específica ($T_x$) entregou o comportamento mais adequado para o sistema de injeção[cite: 76].