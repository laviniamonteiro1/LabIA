# Roadmap de Desenvolvimento - LVQ-1

- [ ] **Fase 1: Preparação de Dados e Estrutura**
  - [x] Criar a hierarquia de pastas `RNA/LVQ1/`.
  - [ ] Criar o script utilitário para gerar o arquivo `treinamento.csv` contendo as 16 amostras de treino.

- [ ] **Fase 2: Motor Algorítmico (`lvq1.py`)**
  - [ ] Implementar a inicialização da matriz de pesos (tamanho 4x6). Uma estratégia comum no LVQ é inicializar os pesos com os valores das primeiras amostras de cada classe para acelerar a convergência.
  - [ ] Implementar o cálculo da distância Euclidiana (seleção do neurônio vencedor).
  - [ ] Implementar a lógica condicional de atualização de pesos (aproximação x afastamento) baseada no rótulo real da amostra.
  - [ ] Implementar o loop de treinamento.

- [ ] **Fase 3: Execução e Automação (`solve_lvq1.py`)**
  - [ ] Carregar os dados de treinamento a partir do `.csv`.
  - [ ] Instanciar e treinar a rede com $\alpha = 0.05$.
  - [ ] Inserir os vetores de teste (Dias 1 a 8) e realizar a inferência.
  - [ ] Imprimir os resultados de forma formatada no terminal.

- [ ] **Fase 4: Documentação Final (`respostas_lvq.md`)**
  - [ ] Documentar os resultados da classificação dos dados de teste no relatório em Markdown.