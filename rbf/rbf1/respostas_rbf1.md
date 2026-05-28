# Resoluções - Atividade RBF 1

**Instituição:** Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG)  
**Campus:** VIII – Varginha  
**Curso:** Bacharelado em Sistemas de Informação  
**Disciplina:** Laboratório de Inteligência Artificial  
**Professor:** Lázaro Eduardo da Silva  
**Data:** 20/05/2026  
**Aluna:** Lavínia Monteiro

---

### **Questão 1**
**Execute o treinamento da camada escondida através do algoritmo “k-means”. Em se tratando de um problema de classificação de padrões, compute os centers dos dois clusters levando-se em consideração apenas aqueles padrões com presença de radiação. Após o treinamento, forneça os valores das coordenadas do centro de cada cluster e sua respectiva variância.**

#### **Resposta 1:**
O algoritmo *k-means* foi aplicado exclusivamente sobre as amostras da base de treinamento que apresentavam status positivo de radiação ($d = 1$). Os resultados calculados para as coordenadas centrais e as variâncias correspondentes de cada agrupamento foram:

| Cluster | Centro ($x_1, x_2$) | Variância ($\sigma^2$) |
| :---: | :--- | :--- |
| **1** | `[0.16483333, 0.61211667]` | `0.029806` |
| **2** | `[0.39896923, 0.15713077]` | `0.038460` |

---

### **Questão 2**
**Após o treinamento da camada intermediária execute o treinamento da camada de saída usando a regra delta generalizada. Utilize uma taxa de aprendizado $\eta = 0.01$ e precisão de $\epsilon = 10^{-7}$. No final da convergência forneça os valores dos pesos referente ao neurônio da camada de saída.**

#### **Resposta 2:**
A camada de saída foi otimizada utilizando o algoritmo da Regra Delta com o critério de parada corrigido para monitorar a variação do erro quadrado médio entre as épocas ($\Delta \text{EQM} < 10^{-7}$). 

Graças a essa implementação, a rede identificou o platô de estagnação matemática da arquitetura (causado pelo mapeamento restrito dos centros) e encerrou o processo de forma eficiente ao atingir a convergência com apenas **328 épocas**, eliminando o processamento redundante. Os valores finais dos pesos obtidos foram:

| Peso | Valor Final |
| :--- | :--- |
| **$W_{21,0}$ (Bias)** | `-1.001838` |
| **$W_{21,1}$ (Cluster 1)** | `2.374704` |
| **$W_{21,2}$ (Cluster 2)** | `2.696316` |

---

### **Questão 3**
**Dado que o problema se configura como um típico processo de classificação de padrões, implemente a rotina que faz o pós-processamento das saídas fornecidas pela rede (números reais) para números inteiros. Utilize a função sinal, ou seja, função utilizada apenas no pós-processamento do conjunto de teste.**

#### **Resposta 3:**
A rotina de pós-processamento foi desenvolvida de forma isolada para atuar apenas na etapa de teste. Ela mapeia as respostas contínuas ($y \in \mathbb{R}$) geradas pela saída da RBF in valores discretos e inteiros ($-1$ ou $1$) usando a função sinal matemática como critério de corte:

$$y_{\text{pós}} = \text{sgn}(y) = \begin{cases} 1, & \text{se } y \ge 0 \\ -1, & \text{se } y < 0 \end{cases}$$

O código que executa essa operação no script foi padronizado utilizando a função `np.where()` do NumPy para garantir eficiência de vetorização.

---

### **Questão 4**
**Faça a validação da rede aplicando o conjunto de teste fornecido na tabela abaixo. Forneça a taxa de acerto (%) entre os valores desejados e os valores fornecidos pela rede (após o pós-processamento) em relação a todos os padrões de teste.**

#### **Resposta 4:**
A validação do modelo foi realizada aplicando as 10 amostras inéditas separadas para o teste. O comportamento real observado no console após a convergência otimizada foi:

| Amostra | $x_1$ | $x_2$ | Desejado ($d$) | Saída Real ($y$) | Saída Pós ($y_{\text{pós}}$) | Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 0.8705 | 0.9329 | -1 | -1.0017 | -1 | **Acerto** |
| **2** | 0.0388 | 0.2703 | 1 | -0.3229 | -1 | *Erro* |
| **3** | 0.8236 | 0.4458 | -1 | -0.9133 | -1 | **Acerto** |
| **4** | 0.7075 | 0.1502 | 1 | -0.2197 | -1 | *Erro* |
| **5** | 0.9587 | 0.8663 | -1 | -1.0018 | -1 | **Acerto** |
| **6** | 0.6115 | 0.9365 | -1 | -0.9870 | -1 | **Acerto** |
| **7** | 0.3534 | 0.3646 | 1 | 0.9659 | 1 | **Acerto** |
| **8** | 0.3268 | 0.2766 | 1 | 1.3226 | 1 | **Acerto** |
| **9** | 0.6129 | 0.4518 | -1 | -0.4677 | -1 | **Acerto** |
| **10** | 0.9948 | 0.4962 | -1 | -0.9958 | -1 | **Acerto** |

**Taxa de Acerto Final (%):** **80.00%** (8 acertos em 10 padrões).

---

### **Questão 5**
**Se for o caso, explique quais estratégias poderemos adotar para tentar aumentar a taxa de acerto desta RBF.**

#### **Resposta 5:**
O erro de classificação observado nas amostras 2 e 4 do teste, bem como a impossibilidade do EQM de treino atingir o zero absoluto, decorrem diretamente da restrição imposta à camada intermediária. Calcular centros de cluster olhando exclusivamente para dados da classe de radiação ($d=1$) impede que os neurônios gaussianos capturem o comportamento estatístico, a dispersão e as fronteiras da classe de ausência de radiação ($d=-1$).

Para solucionar essa deficiência e buscar uma taxa de acerto de até 100%, recomendam-se as seguintes melhorias na arquitetura:

1. **Clusterização Global Não-Supervisionada:** Aplicar o algoritmo *k-means* em toda a base de treinamento (mesclando os dados com $d=1$ e $d=-1$). Isso garante que os centros gerados fiquem bem distribuídos e representem satisfatoriamente as densidades de ambas as classes no espaço bidimensional.
2. **Separação de Centros por Classe Independente:** Alocar centros fixos individuais para cada categoria (ex: mapear 2 centros rodando o *k-means* no subconjunto $1$ e outros 2 centros no subconjunto $-1$), concatenando as respostas para compor uma camada oculta mista com 4 neurônios radiais.
3. **Métrica de Variância por Cobertura Global:** Modificar o cálculo da variância local ($\sigma^2$) de cada cluster por uma métrica baseada no espalhamento total entre os centros obtidos ($\sigma = \frac{d_{\text{max}}}{\sqrt{2K}}$, onde $d_{\text{max}}$ é a distância máxima entre os centros e $K$ o número de clusters). Isso melhora a suavidade e a sobreposição das curvas gaussianas, expandindo a capacidade de generalização da rede.