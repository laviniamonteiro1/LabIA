# Resoluções - Atividade RBF 2

**Instituição:** Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG)  
**Campus:** VIII – Varginha  
**Curso:** Bacharelado em Sistemas de Informação  
**Disciplina:** Laboratório de Inteligência Artificial  
**Professor:** Lázaro Eduardo da Silva  
**Data:** 20/05/2026  
**Aluna:** Lavínia Monteiro

---

### **Questão 1**
**Execute 3 treinamentos para cada topologia de rede RBF definida anteriormente ($N_1 = 5$, $N_1 = 10$ e $N_1 = 15$), inicializando a matriz de pesos da camada de saída com valores aleatórios entre 0 e 1. Se for o caso, reinicie o gerador de números aleatórios em cada treinamento de tal forma que os elementos das matrizes de pesos iniciais não sejam os mesmos. Registre os resultados finais desses 3 treinamentos para cada uma das três topologias de rede na tabela de histórico de convergência.**

#### **Resposta 1:**
Abaixo constam os registros reais de Erro Quadrático Médio (EQM) e o número exato de épocas completadas obtidos no terminal após a execução do script de automação:

| Treinamento | Rede 1 ($N_1 = 5$) | Rede 1 ($N_1 = 5$) | Rede 2 ($N_1 = 10$) | Rede 2 ($N_1 = 10$) | Rede 3 ($N_1 = 15$) | Rede 3 ($N_1 = 15$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| | **EQM** | **Épocas** | **EQM** | **Épocas** | **EQM** | **Épocas** |
| **1º (T1)** | `0.00466` | `127` | `0.00290` | `346` | `0.00206` | `881` |
| **2º (T2)** | `0.00466` | `96` | `0.00290` | `358` | `0.00206` | `645` |
| **3º (T3)** | `0.00466` | `124` | `0.00290` | `342` | `0.00206` | `643` |

*Nota técnica:* Graças à implementação do critério de parada corrigido com base na variação infinitesimal do erro entre as épocas ($\Delta \text{EQM} < 10^{-7}$), as redes alcançaram a convergência real sem a necessidade de exaurir o teto de 150.000 épocas. O algoritmo detectou com precisão o momento em que as matrizes de pesos atingiram estabilidade em seus respectivos platôs energéticos, encerrando os ciclos antecipadamente.

---

### **Questão 2**
**Para todos os treinamentos efetuados no item anterior, faça a validação da rede em relação aos valores desejados apresentados na tabela de teste. Forneça para cada treinamento o erro relativo médio (%) entre os valores desejados e os valores fornecidos pela rede em relação a todos os padrões de teste. Obtenha também a respectiva variância (%).**

#### **Resposta 2:**
Os resultados de aproximação contínua obtidos na validação para as 15 amostras inéditas do conjunto de teste foram mapeados na tabela abaixo com os valores exatos fornecidos pelo console:

| Amostra | Desejado ($d$) | R1_T1 | R1_T2 | R1_T3 | R2_T1 | R2_T2 | R2_T3 | R3_T1 | R3_T2 | R3_T3 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | 0.5965 | 0.6030 | 0.6031 | 0.6030 | 0.6716 | 0.6715 | 0.6715 | 0.6594 | 0.6594 | 0.6594 |
| **02** | 0.6790 | 0.7601 | 0.7601 | 0.7602 | 0.6777 | 0.6777 | 0.6777 | 0.6840 | 0.6840 | 0.6840 |
| **03** | 0.4662 | 0.4543 | 0.4550 | 0.4543 | 0.4805 | 0.4805 | 0.4805 | 0.4564 | 0.4564 | 0.4564 |
| **04** | 0.5012 | 0.4455 | 0.4462 | 0.4455 | 0.5117 | 0.5117 | 0.5117 | 0.4989 | 0.4989 | 0.4989 |
| **05** | 0.6810 | 0.6955 | 0.6954 | 0.6955 | 0.6765 | 0.6765 | 0.6765 | 0.6781 | 0.6781 | 0.6781 |
| **06** | 0.5643 | 0.5835 | 0.5824 | 0.5836 | 0.5882 | 0.5882 | 0.5882 | 0.5465 | 0.5465 | 0.5467 |
| **07** | 0.5875 | 0.5371 | 0.5369 | 0.5371 | 0.6142 | 0.6142 | 0.6142 | 0.5888 | 0.5888 | 0.5888 |
| **08** | 0.7853 | 0.8300 | 0.8306 | 0.8300 | 0.8155 | 0.8155 | 0.8155 | 0.8134 | 0.8134 | 0.8134 |
| **09** | 0.8506 | 0.9109 | 0.9115 | 0.9108 | 0.7886 | 0.7887 | 0.7887 | 0.8134 | 0.8134 | 0.8134 |
| **10** | 0.6165 | 0.5739 | 0.5728 | 0.5739 | 0.7308 | 0.7308 | 0.7308 | 0.6690 | 0.6691 | 0.6693 |
| **11** | 0.4957 | 0.4684 | 0.4682 | 0.4684 | 0.4907 | 0.4907 | 0.4907 | 0.5203 | 0.5203 | 0.5203 |
| **12** | 0.6625 | 0.6553 | 0.6544 | 0.6554 | 0.6661 | 0.6661 | 0.6661 | 0.5986 | 0.5987 | 0.5988 |
| **13** | 0.4402 | 0.3852 | 0.3862 | 0.3852 | 0.4387 | 0.4387 | 0.4387 | 0.4763 | 0.4762 | 0.4762 |
| **14** | 0.7663 | 0.6445 | 0.6442 | 0.6445 | 0.7420 | 0.7420 | 0.7420 | 0.7589 | 0.7589 | 0.7588 |
| **15** | 0.7893 | 0.8619 | 0.8622 | 0.8619 | 0.8210 | 0.8210 | 0.8210 | 0.7961 | 0.7961 | 0.7961 |
| **ERM (%)**| — | **6.98%** | **6.97%** | **6.98%** | **4.41%** | **4.41%** | **4.41%** | **3.75%** | **3.75%** | **3.75%** |
| **Var (%)**| — | **19.23%**| **19.11%**| **19.24%**| **23.93%**| **23.93%**| **23.91%**| **13.00%**| **13.01%**| **13.01%**|

---

### **Quest/ao 3**
**Para cada uma das topologias apresentadas na tabela acima, considerando ainda o melhor treinamento {T1, T2 ou T3} realizado em cada uma delas, trace o gráfico dos valores de erro quadrático médio (EQM) em função de cada época de treinamento. Imprima os três gráficos numa mesma folha de modo não superpostos.**

#### **Resposta 3:**
Os gráficos de evolução de erro foram processados e renderizados com sucesso de forma vertical isolada. O arquivo final de imagem de alta definição foi exportado automaticamente com o nome **`convergencia_rbf2.png`** no diretório do projeto. O uso da escala logarítmica no eixo Y permitiu avaliar de forma limpa o decréscimo estável do gradiente ao longo das épocas de treino executadas antes do disparo da parada de estabilização delta.

---

### **Questão 4**
**Por qual motivo os treinamentos $T_1$, $T_2$ e $T_3$ geraram predições e erros finais extremamente próximos para uma mesma topologia de rede, mas com sutis variações nas últimas casas decimais?**

#### **Resposta 4:**
A forte similaridade das respostas decorre da natureza convexa da superfície de erro na camada de saída de uma Rede RBF. Como os centros e as variâncias Gaussianas são fixados de forma idêntica pelo algoritmo *k-means* antes do início do ajuste dos pesos lineares, a Regra Delta opera buscando um único Mínimo Global (formato parabólico), o que anula a maior parte da influência de partida das sementes de pesos aleatórios.

Por outro lado, o motivo de os valores **não terem sido 100% idênticos** até a última casa decimal vincula-se diretamente ao novo critério de parada por variação ($\Delta \text{EQM} < 10^{-7}$). 

Como o treinamento agora é interrompido de forma inteligente assim que o aprendizado entra em um platô infinitesimal, a otimização cessa ciclos antes de atingir o centro geométrico absoluto e infinito do mínimo global. Consequentemente, pequenas flutuações e resquícios das trajetórias individuais iniciadas pelos diferentes pesos aleatórios de $T_1$, $T_2$ e $T_3$ são preservados nas frações de ponto flutuante, refletindo-se nas pequenas variações de desvios e predições observadas na tabela.

---

### **Questão 5**
**Baseado nas análises dos itens acima, indique qual das topologias candidatas {Rede 1, Rede 2 ou Rede 3} e com qual configuração final de treinamento {T1, T2 ou T3} seria a mais adequada para este problema.**

#### **Resposta 5:**
A arquitetura mais adequada para o sistema prático de aproximação do fluxo de injeção eletrônica automotiva é a **Rede 3 ($N_1 = 15$ neurônios ocultos)**, associada a **qualquer um dos seus três treinamentos ($T_1$, $T_2$ ou $T_3$)**, já que todos consolidaram o mesmo patamar estatístico de excelência na inferência contínua.

**Justificativa Científica:**
1. **Poder de Minimização do Erro:** A expansão da dimensão do espaço oculto para 15 neurônios de base radial conferiu ao modelo a flexibilidade matemática necessária para se moldar às curvas não-lineares severas do motor, alcançando o menor EQM de treino registrado (`0.00206`).
2. **Capacidade Superior de Generalização:** No teste com dados inéditos, a Rede 3 superou as demais arquiteturas ao cravar o menor Erro Relativo Médio (ERM) do experimento, estabelecendo um desvio de apenas **`3.75%`** em relação aos alvos desejados, contra `4.41%` da Rede 2 e `6.98%` da Rede 1.
3. **Equilíbrio de Dispersão:** Além do menor erro médio, a Rede 3 demonstrou alto controle de consistência operacional ao estabilizar a sua variância de erro em **`13.00%`**, um ganho de segurança expressivo comparado à dispersão desregulada de `23.93%` apresentada pela Rede 2. Esse comportamento uniforme é vital em engenharia automotiva para mitigar picos erráticos de dosagem de combustível.