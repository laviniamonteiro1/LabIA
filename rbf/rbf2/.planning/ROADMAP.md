# Roadmap de Desenvolvimento - RBF 2

[cite_start]Fluxo de passos sequenciais para a implementação, simulação e geração de gráficos comparativos para o sistema de injeção eletrônica (CEFET-MG)[cite: 37, 38].

## 📅 Data de Entrega: 20/05/2026

---

## 🗺️ Etapas de Execução

### 🟩 Passo 1: Transcrição da Base de Dados (`dados_rbf2.py`)
- [ ] [cite_start]Mapear os 150 registros do Anexo de treinamento em formato matricial NumPy[cite: 77, 78].
- [ ] [cite_start]Mapear os 15 registros da tabela de validação para testes[cite: 73].
- [ ] [cite_start]Estruturar a separação automatizada entre as colunas de entrada ($X$) e os alvos ($D$).

### 🟨 Passo 2: Adaptação da Classe RBF (`rbf2.py`)
- [ ] [cite_start]Modificar o construtor da classe para aceitar parâmetros variáveis de clusters ($N_1 = 5, 10, 15$)[cite: 58, 60].
- [ ] [cite_start]Implementar a seleção dos centros gaussianos a partir do dataset de treino de forma abrangente (visto que o problema agora cobre todo o espaço amostral de aproximação contínua)[cite: 40].
- [ ] [cite_start]Ajustar a inicialização aleatória dos pesos de saída entre 0 e 1, garantindo a reinicialização do gerador (`np.random.seed`) a cada chamada de treino[cite: 66].
- [ ] [cite_start]Fixar os parâmetros de gradiente: $\eta=0.01$ e limite de parada em $\epsilon=10^{-7}$[cite: 67].

### 🟨 Passo 3: Automação e Gráficos (`solve_rbf2.py`)
- [ ] [cite_start]Desenvolver o loop principal para rodar as 3 redes $\times$ 3 treinamentos automaticamente[cite: 66].
- [ ] [cite_start]Armazenar o histórico de EQM das melhores rodadas para plotagem posterior[cite: 74].
- [ ] [cite_start]Calcular ponto a ponto o Erro Relativo Médio (%) e a Variância (%) das predições de teste[cite: 71, 72].
- [ ] [cite_start]Utilizar a biblioteca `matplotlib` para gerar a folha com os 3 gráficos de convergência isolados[cite: 75].

### 🟦 Passo 4: Compilação das Respostas (`respostas_rbf2.md`)
- [ ] [cite_start]Preencher a tabela macro de convergência (EQM × Épocas)[cite: 69].
- [ ] [cite_start]Preencher a matriz de resultados detalhados das 15 amostras de validação[cite: 73].
- [ ] [cite_start]Inserir os cálculos de Erro Relativo Médio e Variância de cada coluna de teste[cite: 73].
- [ ] [cite_start]Redigir a conclusão técnica apontando a melhor topologia com base nos dados estatísticos coletados[cite: 76].