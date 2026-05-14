import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pmc2 import PMC2

# 1. Carregar Dados do CSV (O que estava faltando no seu código!)
try:
    df_train = pd.read_csv('treinamento_pmc2.csv')
    df_test = pd.read_csv('teste_pmc2.csv')
    
    # Extraindo as 4 entradas e as 3 saídas desejadas
    X_train = df_train[['x1', 'x2', 'x3', 'x4']].values
    d_train = df_train[['d1', 'd2', 'd3']].values
    
    X_test = df_test[['x1', 'x2', 'x3', 'x4']].values
    d_test = df_test[['d1', 'd2', 'd3']].values
except FileNotFoundError:
    print("ERRO: Arquivos CSV não encontrados. Verifique se eles estão na mesma pasta.")
    exit()

# 2. Definir Pesos Iniciais Globais (0 a 1)
# Usando 15 neurônios na camada escondida conforme o diagrama
V_init = np.random.rand(15, 5) 
W_init = np.random.rand(3, 16) 

# --- EXPERIMENTO 1: PADRÃO ---
print("Treinando Backpropagation Padrão...")
rede_std = PMC2(n_inputs=4, n_hidden=15, n_outputs=3, eta=0.1, epsilon=1e-6)
rede_std.V, rede_std.W = np.copy(V_init), np.copy(W_init)

start_std = time.time()
ep_std, hist_std = rede_std.train(X_train, d_train, use_momentum=False)
time_std = time.time() - start_std

# --- EXPERIMENTO 2: MOMENTUM ---
print("Treinando Backpropagation com Momentum (alpha=0.9)...")
rede_mom = PMC2(n_inputs=4, n_hidden=15, n_outputs=3, eta=0.1, alpha=0.9, epsilon=1e-6)
rede_mom.V, rede_mom.W = np.copy(V_init), np.copy(W_init)

start_mom = time.time()
ep_mom, hist_mom = rede_mom.train(X_train, d_train, use_momentum=True)
time_mom = time.time() - start_mom #

# --- VALIDAÇÃO COM ARREDONDAMENTO SIMÉTRICO ---
def calcular_acerto(rede, X, d):
    acertos = 0
    for i in range(len(X)):
        X_wb = np.insert(X[i], 0, rede.x0)
        y_h = rede.sigmoid(np.dot(rede.V, X_wb))
        y_o = rede.sigmoid(np.dot(rede.W, np.insert(y_h, 0, rede.x0)))
        # Regra do arredondamento: >= 0.5 vira 1, senão 0
        y_final = np.where(y_o >= 0.5, 1, 0)
        if np.array_equal(y_final, d[i]):
            acertos += 1
    return (acertos / len(X)) * 100

taxa_std = calcular_acerto(rede_std, X_test, d_test)
taxa_mom = calcular_acerto(rede_mom, X_test, d_test)

# EXIBIR RESULTADOS FINAIS
print("-" * 40)
print(f"PADRÃO   | Épocas: {ep_std} | Tempo: {time_std:.4f}s | Acerto: {taxa_std:.2f}%")
print(f"MOMENTUM | Épocas: {ep_mom} | Tempo: {time_mom:.4f}s | Acerto: {taxa_mom:.2f}%")

# GRÁFICOS NÃO SUPERPOSTOS
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.plot(hist_std, color='blue')
plt.title('EQM - Backpropagation Padrão')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(hist_mom, color='red')
plt.title('EQM - Backpropagation com Momentum')
plt.xlabel('Épocas')
plt.grid(True)
plt.tight_layout()
plt.savefig('comparativo_momentum.png')
print("Gráfico salvo como 'comparativo_momentum.png'!")