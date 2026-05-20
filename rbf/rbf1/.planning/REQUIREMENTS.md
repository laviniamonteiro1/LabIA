# Requisitos do Projeto - Atividade RBF 1

Mapeamento de especificações e restrições técnicas para o desenvolvimento da rede Radial Basis Function (RBF) aplicado à detecção de radiação em compostos nucleares.

## 1. Dados e Arquitetura do Problema
- **Entradas ($x_1, x_2$):** Duas variáveis contínuas que representam a concentração medidada de componentes do composto nuclear.
- **Saída Desejada ($d$):** Valores discretos indicando o status de radiação:
  - `1`: Presença de radiação.
  - `-1`: Ausência de radiação.
- **Volumetria de Amostras:**
  - **Treinamento:** 40 padrões contidos no Apêndice.
  - **Teste (Validação):** 10 padrões contidos na tabela de validação.

## 2. Camada Intermediária (Escondida)
- **Algoritmo de Agrupamento:** *k-means* para determinação dos centros.
- **Filtro de Amostras:** Computar os centros de **apenas 2 clusters**, utilizando exclusivamente os padrões associados à classe com **presença de radiação ($d = 1$)**.
- **Saídas Esperadas:** Coordenadas dos centros e suas respectivas variâncias ($\sigma^2$) para preenchimento da tabela de relatórios.

## 3. Camada de Saída e Otimização
- **Algoritmo de Aprendizado:** Regra Delta Generalizada (Gradiente Descendente Linear).
- **Hiperparâmetros Estritos:**
  - Taxa de Aprendizado ($\eta$): `0.01`.
  - Critério de Parada (Precisão $\epsilon$): `10^-7` ($1.0 \times 10^{-7}$).
- **Parâmetros a Coletar:** Valores finais dos pesos do neurônio de saída ($W_{21,0}$, $W_{21,1}$, $W_{21,2}$).

## 4. Pós-Processamento e Validação
- **Função de Pós-Processamento:** Função Sinal ($\text{sgn}(y)$) para converter saídas reais da rede em valores discretos ($-1$ ou $1$).
- **Restrição de Uso:** Aplicar a função sinal apenas durante a etapa de teste.
- **Métrica de Avaliação:** Taxa de Acerto percentual (%) calculada sobre o conjunto de teste de 10 amostras.