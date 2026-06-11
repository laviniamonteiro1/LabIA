# Roadmap de Desenvolvimento - ART-1

- [x] **Fase 1: Preparação de Dados e Estrutura**
  - Criar a hierarquia de pastas `RNA/art/`.
  - Criar o script utilitário para gerar o arquivo `treinamento.csv` contendo a matriz de 10x16 do apêndice.

- [ ] **Fase 2: Motor Algorítmico (`art.py`)**
  - Implementar a classe `ART1` com vetores de pesos *bottom-up* ($W$) e *top-down* ($T$).
  - Implementar a função de escolha de categoria (ativação F2).
  - Implementar o subsistema de orientação (Teste de Vigilância).
  - Implementar o ajuste de pesos após o estado de ressonância.

- [ ] **Fase 3: Execução e Automação (`solve_art.py`)**
  - Carregar os dados binários do CSV.
  - Criar um loop principal que instancie a rede 4 vezes, uma para cada nível de vigilância exigido ($\rho = 0.5, 0.8, 0.9, 0.99$).
  - Formatar a saída no terminal agrupando as situações em suas respectivas classes.

- [ ] **Fase 4: Documentação Final (`respostas_art.md`)**
  - Consolidar as respostas das quatro simulações em tabelas e listas organizadas em Markdown.