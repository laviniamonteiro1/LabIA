# 14/05 - Atividade 3 - PMC03
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pmc3 import PMC
import time

# 1. Carregar dados e preparar a sequência completa
df_treino = pd.read_csv('treinamento_pmc3.csv')
df_teste = pd.read_csv('teste_pmc3.csv')
serie_completa = np.concatenate([df_treino['f_t'].values, df_teste['f_t'].values])

def criar_janelas(dados, p, start_idx, end_idx):
    X, y = [], []
    for i in range(start_idx, end_idx):
        X.append(dados[i-p : i]) # Pega os p valores anteriores
        y.append(dados[i])       # Valor atual é o alvo
    return np.array(X), np.array(y).reshape(-1, 1)

# Configurações das Redes
config_redes = [
    {'nome': 'Rede 1', 'p': 5,  'N1': 10},
    {'nome': 'Rede 2', 'p': 10, 'N1': 15},
    {'nome': 'Rede 3', 'p': 15, 'N1': 25}
]

resultados_tabela = []

# Loop pelas 3 topologias
for config in config_redes:
    p = config['p']
    N1 = config['N1']
    print(f"\n--- Iniciando {config['nome']} (p={p}, N1={N1}) ---")
    
    # Preparar dados de treino (t=1 até 100) e teste (t=101 até 120)
    X_train, y_train = criar_janelas(serie_completa, p, p, 100)
    X_test, y_test = criar_janelas(serie_completa, p, 100, 120)

    for t_idx in range(1, 4): # 3 Treinamentos por rede
        print(f" Treinamento T{t_idx}...")
        rede = PMC(n_in=p, n_hidden=N1, n_out=1)
        
        start_time = time.time()
        epocas, hist_eqm = rede.train(X_train, y_train, eta=0.1, alpha=0.8, precision=0.5e-6)
        end_time = time.time()
        
        # Validação
        predicoes = np.array([rede.forward(x) for x in X_test]).flatten()
        erros_relativos = np.abs(y_test.flatten() - predicoes) / np.abs(y_test.flatten())
        erro_medio = np.mean(erros_relativos)
        variancia = np.var(erros_relativos)
        
        resultados_tabela.append({
            'Rede': config['nome'], 'Treino': f"T{t_idx}",
            'Épocas': epocas, 'EQM_Final': hist_eqm[-1],
            'Tempo': end_time - start_time,
            'Erro_Medio': erro_medio, 'Variancia': variancia,
            'Predicoes': predicoes, 'Hist_EQM': hist_eqm
        })

# 3. Gerar Gráficos (Exemplo para os melhores treinamentos)
# (Lógica de plotagem simplificada para visualização rápida)
plt.figure(figsize=(12, 8))
for i, config in enumerate(config_redes):
    # Busca o treinamento com menor erro médio para essa rede
    melhor = min([r for r in resultados_tabela if r['Rede'] == config['nome']], key=lambda x: x['Erro_Medio'])
    
    plt.subplot(3, 1, i+1)
    plt.plot(range(101, 121), y_test, 'ko-', label='Desejado')
    plt.plot(range(101, 121), melhor['Predicoes'], 'r--o', label='Estimado')
    plt.title(f"{config['nome']} - Melhor Treinamento (Teste)")
    plt.legend()

plt.tight_layout()
plt.savefig('comparativo_pmc3_estimacao.png')
print("\nProcessamento concluído! Gráficos salvos.")