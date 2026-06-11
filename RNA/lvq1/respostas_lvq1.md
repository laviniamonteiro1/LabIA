# Centro Federal de Educação Tecnológica de Minas Gerais
**Campus VIII – Varginha** **Bacharelado em Sistemas de Informação** * **Disciplina:** Lab. Inteligência Artificial  
* **Professor:** Lázaro Eduardo da Silva  
* **Data:** 11/06/2026  
* **Aluno(a):** Lavínia Monteiro  

---

## Relatório Prático: Classificação de Padrões Supervisionados (Redes LVQ-1)

### **Questão 1**
**Implementar e treinar uma LVQ-1 que detecte as possíveis similaridades e regularidades entre todos os vetores pertencentes a cada uma das classes, objetivando a classificação futura de perfis de potência de outros dias (amostras). Para as simulações, considerar uma taxa de aprendizagem $\alpha = 0.05$.**

#### **Resposta 1:**
A rede baseada no algoritmo de Quantização Vetorial por Aprendizado (LVQ-1) foi modelada e simulada com sucesso conforme as diretrizes do experimento.

* **Inicialização Estratégica:** A matriz de conexões de pesos $W$ (com dimensão $4 \times 6$) foi inicializada de forma determinística utilizando os vetores representativos das primeiras amostras indexadas de cada uma das 4 classes do conjunto de treinamento. Essa abordagem garante o posicionamento prévio dos neurônios competidores dentro de suas bacias de atração originais, acelerando de forma significativa a convergência da rede.
* **Dinâmica Supervisionada de Treinamento:** A rede executou 1000 épocas de treinamento sob amostragem estocástica (*shuffle*) dos padrões. A cada iteração, a distância Euclidiana determinou o neurônio vencedor (Best Matching Unit - BMU). O ajuste fino das fronteiras de decisão (hiperplanos lineares) seguiu estritamente o critério supervisionado de punição ou recompensa baseado no acerto da classe predita em relação ao alvo real:
  * **Quando a classificação está Correta ($C_w = C_x$):** O vetor protótipo é puxado para mais perto da amostra, refinando a bacia de atração:
    $$W_j(t+1) = W_j(t) + \alpha(x - W_j(t))$$
  * **Quando a classificação está Incorreta ($C_w \neq C_x$):** O vetor protótipo é repelido para longe da amostra para delimitar a margem de erro:
    $$W_j(t+1) = W_j(t) - \alpha(x - W_j(t))$$

---

### **Questão 2**
**Após o treinamento da rede, utilize a mesma para a classificação do perfil de potência para os dias apresentados na tabela a seguir (Dados de Teste).**

#### **Resposta 2:**
Após a convergência da matriz de pesos, as 8 amostras de curvas de carga inéditas foram submetidas à camada competitiva treinada. O mapeamento exato gerado pelo terminal do script `solve_lvq1.py` preenche a tabela de validação abaixo:

| Dia | 7 horas | 8 horas | 9 horas | 10 horas | 11 horas | 12 horas | Classe Atribuída |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 2.9817 | 1.5656 | 4.8391 | 1.4311 | 4.1916 | 6.9718 | **Classe 4** |
| **2** | 1.5537 | 2.2615 | 1.3169 | 2.5873 | 1.7570 | 5.0958 | **Classe 3** |
| **3** | 1.2240 | 0.2445 | 1.3595 | 5.4192 | 3.2027 | 2.5675 | **Classe 2** |
| **4** | 2.5828 | 1.5146 | 2.1119 | 1.2859 | 2.3414 | 1.8695 | **Classe 1** |
| **5** | 2.4168 | 1.4857 | 1.8959 | 1.3013 | 2.4500 | 1.7868 | **Classe 1** |
| **6** | 1.0604 | 0.2276 | 1.2806 | 5.4732 | 3.2133 | 2.4839 | **Classe 2** |
| **7** | 1.5246 | 2.4254 | 1.1353 | 2.5325 | 1.7569 | 5.2640 | **Classe 3** |
| **8** | 3.0565 | 1.6259 | 4.7743 | 1.3654 | 4.2904 | 6.9808 | **Classe 4** |

**Análise das Assinaturas de Demanda Identificadas:**
1. **Classe 1 (Perfil Residencial de Início de Turno):** Mapeou os dias **4 e 5**. Apresenta consumo moderadamente alto no início da manhã (7h $\approx 2.4$ a $2.5$) com decréscimo e estabilização linear ao se aproximar do meio-dia (12h $\approx 1.7$ a $1.8$).
2. **Classe 2 (Perfil Industrial de Pico Matutino):** Mapeou os dias **3 e 6**. Apresenta consumo inicial muito baixo, mas sofre uma elevação crítica e abrupta de carga pontualmente às 10h da manhã (ultrapassando $5.4$), estabilizando-se em patamar médio logo após.
3. **Classe 3 (Perfil Comercial de Rampa de Saída):** Mapeou os dias **2 e 7**. Exibe comportamento de consumo controlado durante a manhã, iniciando uma rampa de aceleração severa nas últimas faixas horárias registradas (12h $\approx 5.0$ a $5.2$).
4. **Classe 4 (Perfil Crítico de Alta Carga Contínua):** Mapeou os dias **1 e 8**. Representa cenários de consumo extremo em quase todas as faixas horárias, com alta demanda em 9h ($\approx 4.7$ a $4.8$) e atingindo os níveis mais altos do experimento ao meio-dia, com consumo próximo de $7.0$ unidades de potência.

---

### **Questão 3**
**Demonstrar matemática e textualmente o comportamento da função de erro ou do ajuste de pesos de uma rede LVQ-1, justificando por que ela pertence à categoria de redes com aprendizado supervisionado competitivo.**

#### **Resposta 3:**
A rede LVQ-1 classifica-se como uma arquitetura de **aprendizado supervisionado competitivo** porque seu algoritmo combina o mecanismo de concorrência por distância (típico de redes não-supervisionadas como o SOM/Kohonen) com um sinal de correção baseado na presença de um supervisor externo que fornece o rótulo real dos padrões.

**A dinâmica competitiva-supervisionada desdobra-se matematicamente em duas etapas consecutivas:**

1. **A Fase Competitiva (Não-Supervisionada):**
Dado um padrão de entrada $x \in \mathbb{R}^d$, todos os neurônios da camada de saída competem entre si. O neurônio vencedor $j$ (Best Matching Unit) é selecionado puramente pela menor distância Euclidiana em relação aos seus vetores de pesos, sem nenhuma interferência das classes nesta etapa:
$$j = \arg\min_{i} \|x - W_i\| = \arg\min_{i} \sqrt{\sum_{k=1}^{d} (x_k - w_{ik})^2}$$

2. **A Fase Supervisionada (Correção por Feedback):**
Uma vez definido o índice do neurônio vencedor $j$, o algoritmo invoca a informação de supervisão. Seja $C(W_j)$ a classe associada ao neurônio competitivo vencedor e $C(x)$ a classe real do padrão apresentado. Duas regras analíticas de ajuste podem ocorrer:

* **Caso 1: Recompensa por Classificação Correta ($C(W_j) = C(x)$)**
Se o neurônio vencedor pertence à classe real do dado, o gradiente induz uma alteração positiva. O peso é deslocado em direção ao padrão de entrada, forçando o protótipo da classe a se mover para o centro de massa geométrico do seu cluster:
$$\Delta W_j = +\alpha(x - W_j)$$
$$W_j(t+1) = W_j(t) + \alpha(x - W_j(t))$$

* **Caso 2: Punição por Classificação Incorreta ($C(W_j) \neq C(x)$)**
Se o neurônio vencedor pertence a uma classe incorreta, o sinal do gradiente é invertido. O algoritmo "empurra" o vetor de pesos para longe do padrão de entrada. Esse mecanismo reconfigura o hiperplano de separação, estreitando a bacia de atração da classe errada naquela região e abrindo espaço para a convergência correta:
$$\Delta W_j = -\alpha(x - W_j)$$
$$W_j(t+1) = W_j(t) - \alpha(x - W_j(t))$$

Os neurônios que perderam a competição não sofrem nenhum tipo de alteração em seus pesos durante a iteração ($\Delta W_i = 0, \forall i \neq j$). 

Esta combinação híbrida faz com que a rede LVQ-1 consiga desenhar fronteiras de decisão complexas e lineares por partes no espaço de características, otimizando diretamente a taxa de acerto de classificação por meio da realimentação supervisionada de suas bacias atratoras.