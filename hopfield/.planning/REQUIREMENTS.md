# Requisitos do Projeto - Rede de Hopfield como Memória Associativa

## 1. Descrição do Problema
Implementação de um sistema de recuperação de imagens digitais corrompidas por ruído em um link de transmissão utilizando uma Rede Neural de Hopfield como memória associativa binária/bipolar.

## 2. Requisitos Funcionais (RF)
* **RF01 - Dimensionalidade da Rede:** A rede deve possuir exatamente 45 neurônios, correspondendo à discretização das imagens em vetores de 45 bits (malha de 9x5 pixels).
* **RF02 - Codificação de Estados:** O sistema deve mapear pixels brancos como `-1` e pixels escuros/pretos como `+1`.
* **RF03 - Armazenamento de Padrões:** A matriz de pesos $W$ deve ser calculada de forma determinística utilizando a Regra de Hebb (Regra do Produto Externo) para 4 padrões fundamentais.
* **RF04 - Estabilidade Geométrica:** A diagonal principal da matriz de pesos deve ser zerada ($w_{ii} = 0$) para eliminar a auto-realimentação e garantir a convergência para mínimos estáveis de energia.
* **RF05 - Função de Ativação:** Utilizar a aproximação da Tangente Hiperbólica com ganho alto, operando como a função sinal ($\text{sgn}(u)$) para garantir saídas bipolares $\{-1, 1\}$.
* **RF06 - Dinâmica de Atualização:** Implementar o modo de atualização assíncrono (um neurônio por vez em ordem aleatória) para evitar oscilações cíclicas infinitas.
* **RF07 - Injeção de Ruído:** Criar um mecanismo para corromper aleatoriamente cerca de 20% dos bits de um padrão estável antes de submetê-lo à recuperação.
* **RF08 - Bateria de Testes:** Executar a simulação de 12 cenários distintos (3 testes de ruído estocástico para cada um dos 4 padrões originais).

## 3. Requisitos Não-Funcionais (RNF)
* **RNF01 - Linguagem e Bibliotecas:** Implementação puramente em Python 3 utilizando a biblioteca `numpy` para otimização de álgebra linear.
* **RNF02 - Exibição Visual:** Exibição das matrizes no terminal utilizando caracteres textuais (ex: `█` para +1 e `.` para -1) para validação imediata do formato 9x5.