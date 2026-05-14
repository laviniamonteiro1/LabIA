# Relatório de Respostas - Atividade PMC 2

### 1. Treinamento Backpropagation Padrão
O treinamento foi executado com matrizes de pesos iniciais aleatórias entre 0 e 1, utilizando a função de ativação logística (sigmoid).
- **Taxa de Aprendizado ($\eta$):** 0.1
- **Precisão ($\epsilon$):** $10^{-6}$
- **Resultado:** Convergência atingida em **1034 épocas**.

### 2. Treinamento Backpropagation com Momentum
O treinamento utilizou as mesmas matrizes de pesos iniciais do item anterior para garantir a paridade na comparação.
- **Taxa de Aprendizado ($\eta$):** 0.1
- **Fator de Momentum ($\alpha$):** 0.9
- **Precisão ($\epsilon$):** $10^{-6}$
- **Resultado:** Convergência atingida em **265 épocas**.

### 3. Comparativo de Desempenho e Gráficos
Os gráficos do Erro Quadrático Médio (EQM) foram gerados de forma não superposta para análise da evolução do aprendizado.

| Método | Épocas | Tempo de Processamento |
| :--- | :--- | :--- |
| **Backpropagation Padrão** | 1034 | 12.1095s |
| **Backpropagation com Momentum** | 265 | 2.5256s |

*O arquivo visual correspondente foi salvo como `comparativo_momentum.png`.*

### 4. Pós-processamento e Validação
Foi implementada a rotina de pós-processamento utilizando o critério de **arredondamento simétrico**:
- Se $y \geq 0.5$, então $y = 1$.
- Se $y < 0.5$, então $y = 0$.

**Resultados da Validação:**
- **Conjunto de Teste:** 18 padrões aplicados.
- **Taxa de Acerto Final:** **100.00%**.
- **Conclusão:** A rede classificou corretamente todos os conservantes (Tipos A, B e C) após o treinamento.