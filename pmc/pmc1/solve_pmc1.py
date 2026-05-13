import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pmc1 import PMC

# 1. Carregar os dados
try:
    df = pd.read_csv('treinamento.csv')
    X_train = df[['x1', 'x2', 'x3']].values
    d_train = df['d'].values.reshape(-1, 1)
except FileNotFoundError:
    print("Erro: 'treinamento.csv' não encontrado.")
    exit()

print("Iniciando os 5 treinamentos PMC...")
modelos = []
historicos_mse = []
epocas_lista = []

for i in range(5):
    np.random.seed(None) 
    rede = PMC(n_inputs=3, n_hidden=3, n_outputs=1, eta=0.1, epsilon=1e-6)
    
    epocas, mse_history = rede.train(X_train, d_train)
    
    modelos.append(rede)
    historicos_mse.append(mse_history)
    epocas_lista.append(epocas)
    print(f"T{i+1}: {epocas} épocas.")

# --- QUESTÃO 3: GERAR GRÁFICOS NÃO SUPERPOSTOS ---
# Descobrir os índices dos dois maiores números de épocas
indices_maiores = np.argsort(epocas_lista)[-2:] # Pega os dois últimos após ordenar

print(f"\nGerando gráficos para os maiores treinamentos: T{indices_maiores[1]+1} e T{indices_maiores[0]+1}")

plt.figure(figsize=(10, 10))

# Primeiro gráfico (O maior de todos)
plt.subplot(2, 1, 1)
plt.plot(historicos_mse[indices_maiores[1]], color='blue')
plt.title(f'Treinamento T{indices_maiores[1]+1} - {epocas_lista[indices_maiores[1]]} épocas')
plt.ylabel('EQM')
plt.grid(True)

# Segundo gráfico (O segundo maior)
plt.subplot(2, 1, 2)
plt.plot(historicos_mse[indices_maiores[0]], color='red')
plt.title(f'Treinamento T{indices_maiores[0]+1} - {epocas_lista[indices_maiores[0]]} épocas')
plt.xlabel('Épocas')
plt.ylabel('EQM')
plt.grid(True)

plt.tight_layout()
plt.savefig('questao3_graficos.png')
print("Arquivo 'questao3_graficos.png' gerado com sucesso!")

# --- TABELA DE RESULTADOS (Para a Questão 1 e 2) ---
print("\n--- Resultados para o Relatório ---")
erros_rel = [[] for _ in range(5)]
for idx, x_sample in enumerate(X_train):
    target = d_train[idx][0]
    preds = [m.sigmoid(np.dot(m.W, np.insert(m.sigmoid(np.dot(m.V, np.insert(x_sample, 0, m.x0))), 0, m.x0)))[0] for m in modelos]
    for m_idx, p in enumerate(preds):
        erros_rel[m_idx].append((abs(target - p) / target) * 100)

print("Média Erro Relativo: ", [f"{np.mean(e):.4f}%" for e in erros_rel])