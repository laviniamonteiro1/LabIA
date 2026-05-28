# Centro Federal de Educação Tecnológica de Minas Gerais
**Campus VIII – Varginha** **Bacharelado em Sistemas de Informação** * **Disciplina:** Lab. Inteligência Artificial  
* **Professor:** Lázaro Eduardo da Silva  
* **Data:** 28/05/2026  
* **Aluno(a):** Lavínia Monteiro  

---

## Relatório Prático: Memória Associativa com Rede de Hopfield

### 1. Configuração e Topologia da Rede
Este trabalho apresenta a implementação e análise de uma Rede Neural de Hopfield atuando como memória associativa bipolar para a recuperação de caracteres numéricos ($1, 2, 3 \text{ e } 4$) corrompidos por ruído em um canal de comunicação. 

A rede foi configurada com as seguintes especificações matemáticas e computacionais:
* **Dimensão do Espaço de Estados:** $N = 45$ neurônios, correspondendo à discretização das imagens em matrizes de $9 \times 5$ pixels.
* **Codificação Bipolar:** Pixels brancos mapeados como $-1$ e pixels escuros (configurando os números) mapeados como $+1$.
* **Cálculo da Matriz de Pesos ($W$):** Computada em uma única etapa determinística através da Regra de Hebb (Regra do Produto Externo) para os 4 padrões estáveis:

$$W = \frac{1}{N} \sum_{\mu=1}^{4} \mathbf{\xi}^{\mu} (\mathbf{\xi}^{\mu})^T$$

* **Auto-realimentação:** A diagonal principal foi zerada ($w_{ii} = 0$) para garantir estabilidade energética e forçar a convergência estrita em direção aos mínimos locais fixados.
* **Função de Ativação e Dinâmica:** Aproximação de ganho infinito para a Tangente Hiperbólica, operando computacionalmente como a função sinal ($\text{sgn}(u)$) com dinâmica de **atualização assíncrona** estocástica (um neurônio por vez, com índices permutados aleatoriamente a cada época).

---

### 2. Resultados das 12 Situações de Transmissão (20% de Ruído)
A rede foi submetida à bateria de testes proposta, aplicando 20% de ruído estocástico (inversão aleatória de exatamente 9 pixels) para cada um dos 4 caracteres armazenados, repetindo-se o teste 3 vezes por padrão. O comportamento real observado no terminal foi o seguinte:

#### **A. Simulações do Número 1**
* **Situação de Teste #1:** **SUCESSO.** A imagem ruidosa manteve-se dentro da bacia de atração do caractere original, convergindo perfeitamente para o formato estável do número 1.
* **Situação de Teste #2:** **SUCESSO.** Restauração fiel e completa de todos os 45 bits.
* **Situação de Teste #3:** **SUCESSO.** Convergência nominal atingida em poucas iterações.

#### **B. Simulações do Número 2**
* **Situação de Teste #1:** **FALHA.** O ruído aleatório aplicado inverteu pixels críticos da estrutura do número 2, empurrando o vetor de entrada para fora de sua bacia de atração original. Devido à forte correlação espacial, a dinâmica assíncrona deslizou para o fundo do vale do **Número 1**, estabilizando-se incorretamente nele.
* **Situação de Teste #2:** **SUCESSO.** Recuperação estável e correta do padrão original do número 2.
* **Situação de Teste #3:** **SUCESSO.** Reconstrução integral da geometria do caractere.

#### **C. Simulações do Número 3**
* **Situação de Teste #1:** **SUCESSO.** Restauração limpa e sem artefatos espúrios.
* **Situação de Teste #2:** **SUCESSO.** Convergência estável para a bacia de atração correta.
* **Situação de Teste #3:** **SUCESSO.** Eliminação completa das distorções da transmissão.

#### **D. Simulações do Número 4**
* **Situação de Teste #1:** **SUCESSO.** O preenchimento das colunas e da barra central foi restaurado com exatidão.
* **Situação de Teste #2:** **FALHA.** O ruído estocástico deformou as hastes verticais do número 4. Pela proximidade geométrica das distribuições binárias, a rede decresceu sua energia em direção à bacia do **Número 3**, fixando-se estavelmente na topologia deste caractere intruso.
* **Situação de Teste #3:** **SUCESSO.** Recuperação nominal bem-sucedida.

#### **Análise Crítica dos Resultados:**
A rede obteve uma taxa de eficácia global de **83,33%** (10 acertos em 12 transmissões). As duas falhas observadas evidenciam uma característica real da Rede de Hopfield: caracteres numéricos renderizados em matrizes de baixa resolução ($9 \times 5$) compartilham muitos pixels sobrepostos na mesma coordenada (não são ortogonais). Quando o ruído atinge justamente os bits que diferenciam um número do outro, o estado da rede cruza a fronteira divisória (hiperplano) da bacia de atração e converge para o vizinho mais próximo.

---

### 3. Impacto do Aumento Excessivo do Nível de Ruído
O funcionamento da Rede de Hopfield baseia-se no conceito físico de superfícies de energia regidas por uma Função de Lyapunov. O ato de treinar a rede por produto externo equivale a escavar "vales" profundos na superfície energética, onde o fundo de cada vale representa um padrão memorizado. A recuperação consiste em soltar o vetor ruidoso na superfície e permitir que ele deslize até estacionar no fundo estável.

Quando aumentamos o nível de ruído substancialmente para além dos 20% estipulados, o sistema passa a sofrer quatro fenômenos degradantes:

1. **Transposição de Barreiras Energéticas:** Um ruído severo altera tantos bits simultaneamente que reposiciona o vetor de entrada a uma distância de Hamming muito distante da origem. O ponto de partida é jogado diretamente dentro do raio de captação (bacia de atração) de outro número estável, resultando em falsos positivos sistemáticos durante a filtragem.
2. **Aprisionamento em Estados Espúrios (Mínimos Locais):** A regra Hebbiana clássica introduz naturalmente "falsos vales" na função de energia que não pertencem aos dados de treino. Eles surgem como combinações lineares lineares ímpares dos padrões originais. Sob ruído massivo, a rede perde a capacidade de alcançar as memórias reais e fica aprisionada nesses estados espúrios, devolvendo padrões bizarros que mesclam fragmentos e texturas de números misturados.
3. **Inversão de Estados (Padrões Complementares):** Dada a simetria matemática da dinâmica de rede ($W \cdot s$), se um padrão $V$ possui uma energia mínima estável, o seu oposto perfeito $-V$ (a imagem com cores invertidas em formato negativo fotográfico) também possui exatamente o mesmo nível mínimo de energia. Se a taxa de ruído ultrapassar a barreira crítica de 50%, a rede interpretará o vetor como estando mais próximo do inverso e convergirá estavelmente para o negativo do número original.
4. **Colapso por Saturação de Capacidade Cruzada (*Crosstalk*):** A capacidade teórica de armazenamento estável de uma Rede de Hopfield para padrões perfeitamente ortogonais é de $C \approx 0.14 \times N$. Para $N = 45$, o teto estrito seria de aproximadamente 6 padrões. No entanto, para matrizes altamente correlacionadas e não-ortogonais (como dígitos textuais), a interferência mútua eleva drasticamente o ruído de fundo interno da própria matriz de pesos. O excesso de ruído externo destrói as cristas que separam os vales, fazendo com que as bacias de atração entrem em colapso e impossibilitem qualquer tipo de recuperação estável.