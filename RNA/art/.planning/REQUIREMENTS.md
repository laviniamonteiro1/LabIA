# Requisitos do Sistema - Rede ART-1 (Adaptive Resonance Theory)

## 1. Descrição do Problema
O objetivo é analisar o comportamento de um processo industrial a partir de 10 situações mapeadas. Cada situação é descrita por 16 variáveis de status binárias. A rede deve agrupar essas situações em clusters baseados em similaridade para auxiliar em prováveis diagnósticos de manutenção.

## 2. Especificações da Arquitetura
* **Vetor de Entrada (x):** 16 dimensões (valores binários $x_1$ a $x_{16}$).
* **Camada de Comparação (F1):** 16 nós.
* **Camada de Reconhecimento (F2):** Número dinâmico de nós (cresce conforme novas classes são criadas, limitando-se ao máximo de 10, que é o número de amostras).
* **Parâmetro de Vigilância ($\rho$):** O roteiro exige testes com quatro níveis de rigor: $0.5, 0.8, 0.9$ e $0.99$.
* **Algoritmo:** ART-1 (Clustering Não-Supervisionado para Entradas Binárias).

## 3. Dinâmica de Aprendizado
Para cada amostra apresentada:
1. **Ativação:** Calcula-se a ativação dos nós em F2.
2. **Competição:** Seleciona-se o nó vencedor (maior ativação).
3. **Teste de Vigilância:** Verifica-se se a similaridade entre a entrada e o peso do vencedor atende ao limiar $\rho$.
   * **Ressonância (Passou):** Os pesos são atualizados (interseção lógica `AND`).
   * **Reset (Falhou):** O nó vencedor é inibido e a rede busca o próximo vencedor ou cria uma nova classe.

## 4. Entregáveis Exigidos
1. Para cada simulação ($\rho \in \{0.5, 0.8, 0.9, 0.99\}$), indicar a quantidade total de classes ativas geradas.
2. Relacionar exatamente quais situações (1 a 10) ficaram agrupadas dentro de cada classe.