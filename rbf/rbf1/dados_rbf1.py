# 19/05 - Banco de Dados - RBF 01 (CEFET-MG)
import numpy as np

# 1. TODOS OS DADOS DE TREINAMENTO (40 amostras do Apêndice)
# Estrutura de cada linha: [x1, x2, d]
dados_treino_completos = np.array([
    [0.2563, 0.9503, -1], [0.2405, 0.9018, -1], [0.1157, 0.3676,  1],
    [0.5147, 0.0167,  1], [0.4127, 0.3275,  1], [0.2809, 0.5830,  1],
    [0.8263, 0.9301, -1], [0.9359, 0.8724, -1], [0.1096, 0.9165, -1],
    [0.5158, 0.8545, -1], [0.1334, 0.1362,  1], [0.6371, 0.1439,  1],
    [0.7052, 0.6277, -1], [0.8703, 0.8666, -1], [0.2612, 0.6109,  1],
    [0.0244, 0.5279,  1], [0.9588, 0.3672, -1], [0.9332, 0.5499, -1],
    [0.9623, 0.2961, -1], [0.7297, 0.5776, -1], [0.4560, 0.1871,  1],
    [0.1715, 0.7713,  1], [0.5571, 0.5485, -1], [0.3344, 0.0259,  1],
    [0.4803, 0.7635, -1], [0.9721, 0.4850, -1], [0.8318, 0.7844, -1],
    [0.1373, 0.0292,  1], [0.3660, 0.8581, -1], [0.3626, 0.7302, -1],
    [0.6474, 0.3324,  1], [0.3461, 0.2398,  1], [0.1353, 0.8120,  1],
    [0.3463, 0.1017,  1], [0.9086, 0.1947, -1], [0.5227, 0.2321,  1],
    [0.5153, 0.2041,  1], [0.1832, 0.0661,  1], [0.5015, 0.9812, -1],
    [0.5024, 0.5274, -1]
])

# Separação das entradas de treino (X) e saídas desejadas de treino (D)
X_treino = dados_treino_completos[:, :2]
D_treino = dados_treino_completos[:, 2].reshape(-1, 1)

# FILTRO DO K-MEANS: Isola apenas os padrões com presença de radiação (d == 1)
# Conforme exigência explícita do enunciado para mapear os clusters
X_kmeans_filtro = X_treino[(D_treino == 1).flatten()]


# 2. DADOS DE TESTE / VALIDAÇÃO (10 amostras da tabela)
dados_teste_completos = np.array([
    [0.8705, 0.9329, -1],
    [0.0388, 0.2703,  1],
    [0.8236, 0.4458, -1],
    [0.7075, 0.1502,  1],
    [0.9587, 0.8663, -1],
    [0.6115, 0.9365, -1],
    [0.3534, 0.3646,  1],
    [0.3268, 0.2766,  1],
    [0.6129, 0.4518, -1],
    [0.9948, 0.4962, -1]
])

X_teste = dados_teste_completos[:, :2]
D_teste = dados_teste_completos[:, 2].reshape(-1, 1)