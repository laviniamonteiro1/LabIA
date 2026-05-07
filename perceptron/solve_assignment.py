import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from perceptron import Perceptron

# 1. Carregar os dados de treinamento
try:
    # O arquivo treinamento.csv deve estar na mesma pasta deste script
    df = pd.read_csv('treinamento.csv')
    X_train = df[['x1', 'x2', 'x3']].values
    d_train = df['d'].values
except FileNotFoundError:
    print("Erro: O arquivo 'treinamento.csv' não foi encontrado.")
    print("Certifique-se de estar rodando o script de dentro da pasta 'perceptron'.")
    exit()

# 2. Amostras para a classificação automática (Questão 3 do trabalho)
amostras_teste = np.array([
    [-0.3565, 0.0620, 5.9891], [-0.7842, 1.1267, 5.5912],
    [0.3012, 0.5611, 5.8234], [0.7757, 1.0648, 8.0677],
    [0.1570, 0.8028, 6.3040], [-0.7014, 1.0316, 3.6005],
    [0.3748, 0.1536, 6.1537], [-0.6920, 0.9404, 4.4058],
    [-1.3970, 0.7141, 4.9263], [-1.8842, -0.2805, 1.2548]
])

print("Iniciando os 5 processos de treinamento...")
modelos = []
historico_final = None

# Executar 5 treinamentos com inicialização aleatória
for i in range(5):
    # O Perceptron inicializa pesos aleatórios entre 0 e 1 no __init__
    p = Perceptron(n_inputs=3, learning_rate=0.01)
    
    w_inicial = p.weights.copy()
    # Realiza o treinamento e captura o histórico de erros por época
    w_final, epocas, error_history = p.train(X_train, d_train)
    
    modelos.append(p)
    
    print(f"Treinamento {i+1} (T{i+1}):")
    print(f"  - Épocas para convergência: {epocas}")
    print(f"  - Pesos Finais: {w_final}\n")
    
    # Armazena o histórico do último treinamento para o gráfico
    if i == 4:
        historico_final = error_history

# --- GERAÇÃO DO GRÁFICO DE CONVERGÊNCIA ---
print("Gerando gráfico 'evolucao_erros.png'...")
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(historico_final) + 1), historico_final, color='blue', linewidth=2)
plt.title('Evolução do Erro de Treinamento (Regra de Hebb) - T5')
plt.xlabel('Épocas')
plt.ylabel('Quantidade de Erros')
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('evolucao_erros.png')
print("Gráfico salvo com sucesso!\n")

# --- TABELA DE CLASSIFICAÇÃO DAS AMOSTRAS (Questão 3) ---
print("--- Resultados da Classificação das 10 Amostras ---")
print("Amostra | T1 | T2 | T3 | T4 | T5")
print("-" * 35)
for idx, amostra in enumerate(amostras_teste):
    predicoes = [int(mod.predict(amostra)) for mod in modelos]
    print(f" {idx+1:2d}     | {predicoes[0]:2d} | {predicoes[1]:2d} | {predicoes[2]:2d} | {predicoes[3]:2d} | {predicoes[4]:2d}")