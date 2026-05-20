# Roadmap de Desenvolvimento - RBF 1

Cronograma de etapas para a implementação e entrega da atividade de Redes Neurais RBF para o CEFET-MG.

## 📅 Data de Entrega: 20/05/2026

---

## 🗺️ Etapas de Implementação

### 🟩 Passo 1: Preparação da Camada de Dados (`dados_rbf1.py`)
- [ ] Transcrever as 40 amostras de treinamento (Apêndice) para matrizes NumPy.
- [ ] Transcrever as 10 amostras de teste (Validação) para matrizes NumPy.
- [ ] Implementar a lógica de filtragem para isolar apenas os dados onde $d = 1$ para o *k-means*.

### 🟨 Passo 2: Construção do Motor RBF (`rbf1.py`)
- [ ] Implementar o algoritmo *k-means* clássico fixado para 2 clusters.
- [ ] Implementar o cálculo da variância matemática ($\sigma^2$) de cada cluster formado.
- [ ] Desenvolver a função de ativação com Base Radial Gaussiana.
- [ ] Desenvolver a Regra Delta Generalizada para ajustar os pesos de saída com $\eta=0.01$ e parada em $\epsilon=10^{-7}$.

### 🟨 Passo 3: Execução e Coleta (`solve_rbf1.py`)
- [ ] Rodar o treinamento da camada escondida e imprimir Centros e Variâncias.
- [ ] Executar o treinamento da camada de saída e capturar os pesos finais ($W$).
- [ ] Processar o conjunto de teste, aplicar a Função Sinal e computar a Taxa de Acerto (%).

### 🟦 Passo 4: Relatório e Submissão (`respostas_rbf1.md`)
- [ ] Preencher as tabelas de clusters e pesos no Markdown.
- [ ] Preencher a tabela final de mapeamento das 10 amostras de teste.
- [ ] Escrever a análise de estratégias para o aumento da taxa de acerto se aplicável.
- [ ] Subir as atualizações para o GitHub com a mensagem padronizada de commit.