# 11/06/2026 - Script de Execução e Automação - ART-1 (Seguro)
import numpy as np
from art import ART1Net

def executar_experimento_art():
    print("=== ETAPA 1: Carregamento dos Dados ===")
    # Matriz oficial do apêndice: 10 Situações x 16 Variáveis Binárias
    X_treino = np.array([
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1], # Situação 1
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0], # Situação 2
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1], # Situação 3
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0], # Situação 4
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1], # Situação 5
        [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1], # Situação 6
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0], # Situação 7
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1], # Situação 8
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], # Situação 9
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1]  # Situação 10
    ])
    
    print(f"-> Sucesso: {len(X_treino)} situações industriais carregadas.\n")
    
    # O roteiro exige testes com os seguintes graus de vigilância
    graus_vigilancia = [0.5, 0.8, 0.9, 0.99]
    
    print("=== ETAPA 2: Simulações (Teste de Estabilidade e Plasticidade) ===")
    
    for rho in graus_vigilancia:
        print(f"\n--- Simulação com Vigilância (ρ) = {rho} ---")
        
        # Instancia uma nova rede zerada para o grau de vigilância atual
        art = ART1Net(input_dim=16, rho=rho)
        
        # Treina e obtém o mapeamento final
        mapeamento = art.train(X_treino, epochs=10)
        
        # Estrutura auxiliar para agrupar as situações em suas respectivas classes
        classes_geradas = {}
        for i, classe_idx in enumerate(mapeamento):
            situacao = i + 1
            if classe_idx not in classes_geradas:
                classes_geradas[classe_idx] = []
            classes_geradas[classe_idx].append(situacao)
            
        print(f"Total de classes ativas (criadas): {art.num_classes}")
        print("Agrupamentos (Diagnósticos Prováveis):")
        
        # Exibe os agrupamentos ordenados
        for classe_idx in sorted(classes_geradas.keys()):
            situacoes = classes_geradas[classe_idx]
            situacoes_str = ", ".join([f"Situação {s}" for s in situacoes])
            print(f"  Classe {classe_idx + 1}: [{situacoes_str}]")
            
    print("\n--------------------------------------------------------------")

if __name__ == "__main__":
    executar_experimento_art()