# Centro Federal de Educação Tecnológica de Minas Gerais
**Campus VIII – Varginha** **Bacharelado em Sistemas de Informação** * **Disciplina:** Lab. Inteligência Artificial  
* **Professor:** Lázaro Eduardo da Silva  
* **Data:** 28/05/2026  
* **Aluno(a):** Lavínia Monteiro  

---

## Relatório Prático: Redes Auto-Organizáveis (Mapas de Kohonen - SOM)

### **Questão 1**
**De posse dos resultados advindos do treinamento da rede, efetuou-se uma análise neste conjunto e verificou-se que as amostras 1-20, 21-60 e 61-120 possuem particularidades em comum, podendo ser então consideradas três classes distintas, denominadas de classe A, B e C, respectivamente. Portanto, têm-se as seguintes questões: Indique quem são os conjuntos de neurônios representados no grid que fornecem respostas relativas às classes A, B e C.**

#### **Resposta 1:**
Com base no mapeamento topológico obtido após o treinamento estabilizado do grid bidimensional $4 \times 4$, os neurônios da camada de saída organizaram-se geometricamente por afinidade de características espaciais das falhas de borracha. 

A distribuição regionalizada de cada conjunto de neurônios dominantes ficou configurada da seguinte forma:

* **Conjunto de Neurônios da Classe A:** Formado pelos neurônios **01, 02, 03, 04 e 05**. Esta classe ocupou majoritariamente a primeira linha do grid e a extremidade inicial da segunda linha.
* **Conjunto de Neurônios da Classe B:** Formado pelos neurônios **10, 11, 12, 13, 14, 15 e 16**. Esta classe consolidou-se densamente na metade inferior do grid (terceira e quarta linhas).
* **Conjunto de Neurônios da Classe C / Fronteira:** Durante o processo estocástico de treinamento e o mapeamento dos dados carregados, as transições geraram uma faixa de **neurônios inativos (06, 07, 08 e 09)**, atuando como uma zona de isolamento topológico espacial (fronteira de separação) entre os clusters das classes adjacentes.

**Visualização Geométrica do Grid (4x4):**
>   [A]     [A]      [A]      [A]  
>   [A]   [Vazio]  [Vazio]  [Vazio]  
> [Vazio]   [B]      [B]      [B]  
>   [B]     [B]      [B]      [B]  

---

### **Questão 2**
**Para as amostras da tabela abaixo indique a que classes as mesmas pertencem:**

| Amostra | $x_1$ | $x_2$ | $x_3$ | Classe |
| :---: | :---: | :---: | :---: | :--- |
| **1** | 0.2471 | 0.1778 | 0.2905 | |
| **2** | 0.8240 | 0.2223 | 0.7041 | |
| **3** | 0.4960 | 0.7231 | 0.5866 | |
| **4** | 0.2923 | 0.2041 | 0.2234 | |
| **5** | 0.8118 | 0.2668 | 0.7484 | |
| **6** | 0.4837 | 0.8200 | 0.4792 | |
| **7** | 0.3248 | 0.2629 | 0.2375 | |
| **8** | 0.7209 | 0.2116 | 0.7821 | |
| **9** | 0.5259 | 0.6522 | 0.5957 | |
| **10** | 0.2075 | 0.1669 | 0.1745 | |
| **11** | 0.7830 | 0.3171 | 0.7888 | |
| **12** | 0.5393 | 0.7510 | 0.5682 | |

#### **Resposta 2:**
A classificação foi efetuada através do cálculo de menor distância Euclidiana entre o vetor de entrada inédito e as coordenadas de pesos dos 16 neurônios do grid (critério do Best Matching Unit - BMU). O mapeamento final das 12 amostras industriais fornecidas resultou na seguinte distribuição de categorias:

| Amostra | $x_1$ | $x_2$ | $x_3$ | BMU Vencedor | Classe Atribuída |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | 0.2471 | 0.1778 | 0.2905 | **03** | **Classe A** |
| **02** | 0.8240 | 0.2223 | 0.7041 | **15** | **Classe B** |
| **03** | 0.4960 | 0.7231 | 0.5866 | **11** | **Classe B** |
| **04** | 0.2923 | 0.2041 | 0.2234 | **04** | **Classe A** |
| **05** | 0.8118 | 0.2668 | 0.7484 | **16** | **Classe B** |
| **06** | 0.4837 | 0.8200 | 0.4792 | **11** | **Classe B** |
| **07** | 0.3248 | 0.2629 | 0.2375 | **03** | **Classe A** |
| **08** | 0.7209 | 0.2116 | 0.7821 | **13** | **Classe B** |
| **09** | 0.5259 | 0.6522 | 0.5957 | **11** | **Classe B** |
| **10** | 0.2075 | 0.1669 | 0.1745 | **03** | **Classe A** |
| **11** | 0.7830 | 0.3171 | 0.7888 | **12** | **Classe B** |
| **12** | 0.5393 | 0.7510 | 0.5682 | **11** | **Classe B** |

---

### **Questão 3**
**Demonstrar que a regra de alteração de pesos “Norma Euclidiana” para um padrão $x$ é obtida a partir da minimização da função erro quadrático:**

$$E = \frac{1}{2} \sum_{i=1}^{d} (x_i - w_{ji})^2$$

**onde $j$ é o índice do neurônio vencedor.**

#### **Resposta 3:**
Para demonstrar analiticamente a regra de Kohonen, aplica-se o algoritmo do gradiente descendente sobre a função de custo $E$. O objetivo é calcular o vetor de derivadas parciais em relação a cada peso $w_{ji}$ conectado ao neurônio vencedor $j$:

$$\frac{\partial E}{\partial w_{ji}} = \frac{\partial}{\partial w_{ji}} \left[ \frac{1}{2} \sum_{i=1}^{d} (x_i - w_{ji})^2 \right]$$

Isolando a componente específica da soma para a $i$-ésima dimensão do vetor e aplicando a regra da cadeia para derivadas de funções compostas:

$$\frac{\partial E}{\partial w_{ji}} = \frac{1}{2} \cdot 2 \cdot (x_i - w_{ji})^{2-1} \cdot \frac{\partial}{\partial w_{ji}}(x_i - w_{ji})$$

Como $x_i$ é uma constante em relação a $w_{ji}$, a derivada interna do parêntese resulta em $-1$:

$$\frac{\partial E}{\partial w_{ji}} = (x_i - w_{ji}) \cdot (-1)$$

$$\frac{\partial E}{\partial w_{ji}} = -(x_i - w_{ji})$$

A filosofia de ajuste por gradiente descendente estipula que o deslocamento corretivo do peso ($\Delta w_{ji}$) deve caminhar no sentido inverso ao vetor gradiente, sendo ponderado pela taxa de aprendizado do sistema ($\eta$):

$$\Delta w_{ji} = -\eta \cdot \left( \frac{\partial E}{\partial w_{ji}} \right)$$

Substituindo o termo derivado obtido anteriormente:

$$\Delta w_{ji} = -\eta \cdot [-(x_i - w_{ji})]$$

$$\Delta w_{ji} = \eta(x_i - w_{ji})$$

Sabendo que o novo peso no tempo seguinte $(t+1)$ é definido pelo estado atual acrescido do ajuste calculado:

$$w_{ji}(t+1) = w_{ji}(t) + \Delta w_{ji}$$

$$w_{ji}(t+1) = w_{ji}(t) + \eta(x_i - w_{ji}(t))$$

Fica **demonstrado** que a regra clássica de atualização competitiva de pesos dos Mapas Auto-Organizáveis de Kohonen é a expressão analítica direta resultante da minimização matemática contínua da função de erro quadrático baseada na norma Euclidiana.