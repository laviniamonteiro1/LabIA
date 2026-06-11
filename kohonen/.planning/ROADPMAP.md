# Roadmap de Desenvolvimento - Kohonen

- [ ] **Fase 1: Preparação dos Dados**
  - Criar o script utilitário para estruturar o `treinamento.csv` a partir do apêndice técnico.
  - Criar o vetor com os dados de teste para validação das 12 amostras.

- [ ] **Fase 2: Motor Matemático (`kohonen.py`)**
  - Implementar inicialização aleatória dos pesos de tamanho (16, 3).
  - Implementar cálculo de distância Euclidiana para seleção do Best Matching Unit (BMU / Neurônio Vencedor).
  - Implementar cálculo de vizinhança topológica (Raio = 1).
  - Implementar laço de ajuste de pesos Hebbiano/Mapeado.

- [ ] **Fase 3: Automação e Análise (`solve_kohonen.py`)**
  - Executar o treinamento da rede até a estabilização das coordenadas.
  - Mapear a matriz 4x4 colocando as amostras conhecidas para rotular cada neurônio.
  - Classificar as 12 amostras do roteiro.

- [ ] **Fase 4: Relatório Final (`respostas_kohonen.md`)**
  - Preencher tabelas de ativação e predição.
  - Desenvolver a demonstração matemática da derivada da Norma Euclidiana.