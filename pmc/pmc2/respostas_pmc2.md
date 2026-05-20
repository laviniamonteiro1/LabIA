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

---

### 5. Análise Teórica: Convergência em Superfícies de Erro Complexas
Diferentemente de arquiteturas lineares como o Adaline ou redes RBF (que possuem superfícies de erro estritamente convexas e com um único mínimo global garantido), o Perceptron Multicamadas (PMC) opera sobre uma **superfície de erro não-convexa e de alta complexidade topológica**.

A inserção de múltiplas camadas ocultas combinadas com funções de ativação não-lineares (sigmoides) transforma o cálculo do custo do Backpropagation em um terreno irregular e caótico. Em vez de uma descida limpa em direção a um único centro, o algoritmo enfrenta:
1. **Múltiplos Mínimos Locais:** "Vales" falsos onde o gradiente se anula ($\nabla E = 0$), fazendo com que a rede possa estacionar em soluções sub-ótimas se inicializada em uma coordenada desfavorável.
2. **Pontos de Sela e Platôs:** Extensas regiões planas onde as derivadas da sigmoide aproximam-se de zero (fenômeno da saturação do neurônio), tornando o ajuste dos pesos extremamente lento.

Essa complexidade topográfica justifica a expressiva diferença de desempenho observada nos testes deste relatório. Enquanto o Backpropagation Padrão tendeu a gastar **1034 épocas** para contornar essas irregularidades da superfície, a incorporação do **Termo de Momento ($\alpha = 0.9$)** funcionou como uma força de inércia mecânica. Ao acumular a energia dos gradientes passados, o Momentum permitiu que a rede superasse os pequenos obstáculos e platôs intermediários do problema dos conservantes, acelerando a descida e atingindo o ponto ótimo global em apenas **265 épocas**.