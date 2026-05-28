# 19/05 - Script de Execução e Validação - RBF 01 (Atualizado)
import numpy as np
from dados_rbf1 import X_treino, D_treino, X_kmeans_filtro, X_teste, D_teste
from rbf1 import RBFNet

def executar_experimento():
    # 1. Instancia a rede configurada para 2 clusters conforme o enunciado
    rbf_net = RBFNet(n_clusters=2)
    
    print("=== ETAPA 1: Treinamento da Camada Escondida (k-means) ===")
    # Treina os centros baseando-se apenas nos padrões com d == 1
    centros, variancias = rbf_net.train_hidden_layer(X_kmeans_filtro)
    
    print("\n--- [RESULTADO] Coordenadas dos Centros e Variâncias ---")
    for i in range(len(centros)):
        print(f"Cluster {i+1}: Centro = {centros[i]}, Variância = {variancias[i]:.6f}")
        
    print("\n=== ETAPA 2: Treinamento da Camada de Saída (Regra Delta) ===")
    # Ajustado o texto para refletir o critério de parada por variação de erro (Delta EQM)
    print("Treinando com eta = 0.01 e precisão de variação (Δ EQM) = 10^-7... Por favor, aguarde.")
    # Executa a otimização dos pesos lineares de saída
    total_epocas, pesos_finais = rbf_net.train_output_layer(X_treino, D_treino, eta=0.01, precision=1e-7)
    
    print(f"\nConvergência atingida com sucesso em {total_epocas} épocas!")
    print("\n--- [RESULTADO] Valores dos Pesos Finais ---")
    print(f"W21,0 (Bias)      : {pesos_finais[0][0]:.6f}")
    print(f"W21,1 (Cluster 1) : {pesos_finais[1][0]:.6f}")
    print(f"W21,2 (Cluster 2) : {pesos_finais[2][0]:.6f}")
    
    print("\n=== ETAPA 3: Validação com Conjunto de Teste ===")
    # Faz as predições reais e processa pela Função Sinal (pós-processamento)
    y_reais = rbf_net.predict(X_teste, pos_processar=False)
    y_pos = rbf_net.predict(X_teste, pos_processar=True)
    
    print("\nTabela de Mapeamento dos Padrões de Teste:")
    print("Amostra |   x1   |   x2   | Desejado (d) | Saída Real (y) | Saída Pós (y_pos)")
    print("-" * 75)
    
    acertos = 0
    for i in range(len(X_teste)):
        d_alvo = int(D_teste[i][0])
        y_final = int(y_pos[i][0])
        
        # Incrementa o contador caso a classe prevista seja igual à desejada
        if y_final == d_alvo:
            acertos += 1
            
        print(f"   {i+1:2d}   | {X_teste[i][0]:.4f} | {X_teste[i][1]:.4f} |     {d_alvo:2d}     |   {y_reais[i][0]:.4f}   |       {y_final:2d}")
        
    # Calcula a métrica percentual de eficácia do modelo
    taxa_acerto = (acertos / len(X_teste)) * 100
    print("-" * 75)
    print(f"Taxa de Acerto Final (%): {taxa_acerto:.2f}%")

if __name__ == "__main__":
    executar_experimento()