# Roadmap de Execução - PMC 2 (Classificação de Conservantes)

- **Configuração de Ambiente:** Variáveis de ambiente (PATH) corrigidas para reconhecer o comando `python` e bibliotecas (`numpy`, `pandas`, `matplotlib`) instaladas via `uv`.
- **Execução do Algoritmo 1:** Backpropagation Padrão ($\eta = 0.1$, $\epsilon = 10^{-6}$) finalizado com convergência em 1034 épocas.
- **Execução do Algoritmo 2:** Backpropagation com Momentum ($\alpha = 0.9$, $\eta = 0.1$, $\epsilon = 10^{-6}$) finalizado com convergência em 265 épocas.
- **Geração de Resultados:** Gráficos de EQM não superpostos salvos em `comparativo_momentum.png` e tempos de processamento medidos.
- **Validação Final:** Teste com 18 amostras utilizando arredondamento simétrico concluído com 100% de acerto.
- **Entrega:** Documentação dos resultados e `git push` para o repositório remoto.