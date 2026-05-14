# Roadmap de Execução - PMC 03

- [ ] **Fase 1: Preparação da Estrutura**
    - Criar diretórios `pmc3` e `.planning`.
    - [cite_start]Gerar arquivos CSV de treinamento ($t=1..100$) e teste ($t=101..120$) a partir do Anexo[cite: 39, 49].

- [ ] **Fase 2: Desenvolvimento da Lógica TDNN**
    - [cite_start]Implementar a função de "janela deslizante" no `pmc3.py` para criar as entradas baseadas em $p$ atrasos[cite: 13, 14, 15].
    - [cite_start]Ajustar a classe PMC para suportar o fator de momentum de 0.8[cite: 33].

- [ ] **Fase 3: Execução dos Treinamentos**
    - Rodar os 3 ciclos de treino para a Rede 1 (5 entradas).
    - Rodar os 3 ciclos de treino para a Rede 2 (10 entradas).
    - Rodar os 3 ciclos de treino para a Rede 3 (15 entradas).
    - [cite_start]Registrar épocas e EQM final em `respostas_pmc3.md`[cite: 35].

- [ ] **Fase 4: Validação e Gráficos**
    - [cite_start]Calcular erro relativo médio e variância para o conjunto de teste[cite: 37, 38].
    - [cite_start]Plotar gráficos comparativos e de estimação[cite: 41, 43].

- [ ] **Fase 5: Conclusão e Teoria**
    - [cite_start]Redigir análise sobre a melhor topologia encontrada[cite: 44].
    - [cite_start]Adicionar comentários sobre RProp e LM[cite: 46, 47].
    - Realizar commit final: `14/05 - Atividade 3 - PMC03`.