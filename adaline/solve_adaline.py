import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from adaline import Adaline

# 1. Carregar os dados de treinamento
try:
    df = pd.read_csv('treinamento.csv')
    X_train = df[['x1', 'x2', 'x3', 'x4']].values
    d_train = df['d'].values
except FileNotFoundError:
    print("Erro: 'treinamento.csv' não encontrado.")
    exit()

# Amostras para classificação (Questão 3)
amostras_teste = np.array([
    [0.9694, 0.6909, 0.4334, 3.4965], [0.5427, 1.3832, 0.6390, 4.0352],
    [0.6081, -0.9196, 0.5925, 0.1016], [-0.1618, 0.4694, 0.2030, 3.0117],
    [0.1870, -0.2578, 0.6124, 1.7749], [0.4891, -0.5276, 0.4378, 0.6439],
    [0.3777, 2.0149, 0.7423, 3.3932], [1.1498, -0.4067, 0.2469, 1.5866],
    [0.9325, 1.0950, 1.0359, 3.3591], [0.5060, 1.3317, 0.9222, 3.7174],
    [0.0497, -2.0656, 0.6124, -0.6585], [0.4004, 3.5369, 0.9766, 5.3532],
    [-0.1874, 1.3343, 0.5374, 3.2189], [0.5060, 1.3317, 0.9222, 3.7174],
    [1.6375, -0.7911, 0.7537, 0.5515]
])

print("Iniciando os 5 treinamentos ADALINE...")
modelos = []
historicos_eqm = []

# Loop para os 5 treinamentos
for i in range(5):
    ada = Adaline(n_inputs=4, learning_rate=0.0025, precision=1e-6)
    
    # CAPTURA DOS PESOS INICIAIS (O QUE FALTOU ANTES)
    w_inicial = ada.weights.copy()
    
    # Treinamento
    w_final, epocas, mse_history = ada.train(X_train, d_train)
    
    modelos.append(ada)
    historicos_eqm.append(mse_history)
    
    # PRINT DETALHADO PARA A TABELA DO MD
    print(f"\n--- Treinamento T{i+1} ---")
    print(f"Épocas: {epocas}")
    print(f"Pesos Iniciais [w0, w1, w2, w3, w4]:\n{w_inicial}")
    print(f"Pesos Finais   [w0, w1, w2, w3, w4]:\n{w_final}")

# Gráfico unificado (T1 e T2)
plt.figure(figsize=(10, 6))
plt.plot(historicos_eqm[0], label='T1', color='blue')
plt.plot(historicos_eqm[1], label='T2', color='red', linestyle='--')
plt.title('Convergência EQM - Treinamentos T1 e T2')
plt.xlabel('Épocas')
plt.ylabel('Erro Quadrático Médio')
plt.legend()
plt.grid(True)
plt.savefig('graficos_eqm.png')

# Tabela de Classificação Final
print("\n--- Tabela de Classificação Final ---")
for idx, amostra in enumerate(amostras_teste):
    res = [int(m.predict(amostra)) for m in modelos]
    print(f" Amostra {idx+1:2d} | {res[0]:2d} | {res[1]:2d} | {res[2]:2d} | {res[3]:2d} | {res[4]:2d}")