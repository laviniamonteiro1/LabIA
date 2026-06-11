# 11/06/2026 - Script de Execução e Classificação Final - LVQ-1 (Seguro)
import numpy as np
from lvq1 import LVQ1Net

def executar_experimento_lvq():
    # Fixar semente para reproducibilidade exata dos resultados
    np.random.seed(42)
    
    print("=== ETAPA 1: Carregamento dos Dados ===")
    # Dados Oficiais do Apêndice (Amostra, 7h, 8h, 9h, 10h, 11h, 12h)
    X_treino = np.array([
        [2.3976, 1.5328, 1.9044, 1.1937, 2.4184, 1.8649], # Amostra 1
        [2.3936, 1.4804, 1.9907, 1.2732, 2.2719, 1.8110], # Amostra 2
        [2.2880, 1.4585, 1.9867, 1.2451, 2.3389, 1.8099], # Amostra 3
        [2.2904, 1.4766, 1.8876, 1.2706, 2.2966, 1.7744], # Amostra 4
        [1.1201, 0.0587, 1.3154, 5.3783, 3.1849, 2.4276], # Amostra 5
        [0.9913, 0.1524, 1.2700, 5.3808, 3.0714, 2.3331], # Amostra 6
        [1.0915, 0.1881, 1.1387, 5.3701, 3.2561, 2.3383], # Amostra 7
        [1.0535, 0.1229, 1.2743, 5.3226, 3.0950, 2.3193], # Amostra 8
        [1.4871, 2.3448, 0.9918, 2.3160, 1.6783, 5.0850], # Amostra 9
        [1.3312, 2.2553, 0.9618, 2.4702, 1.7272, 5.0645], # Amostra 10
        [1.3646, 2.2945, 1.0562, 2.4763, 1.8051, 5.1470], # Amostra 11
        [1.4392, 2.2296, 1.1278, 2.4230, 1.7259, 5.0876], # Amostra 12
        [2.9364, 1.5233, 4.6109, 1.3160, 4.2700, 6.8749], # Amostra 13
        [2.9034, 1.4640, 4.6061, 1.4598, 4.2912, 6.9142], # Amostra 14
        [3.0181, 1.4918, 4.7051, 1.3521, 4.2623, 6.7966], # Amostra 15
        [2.9374, 1.4896, 4.7219, 1.3977, 4.1863, 6.8336]  # Amostra 16
    ])
    
    # Classes associadas a cada perfil de demanda [1, 2, 3, 4]
    y_treino = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])
    print(f"-> Sucesso: {len(X_treino)} dias de medição carregados para o treino da potência.\n")
    
    print("=== ETAPA 2: Treinamento da Rede LVQ-1 ===")
    lvq = LVQ1Net(input_dim=6, num_classes=4, alpha=0.05)
    
    print("Iniciando treinamento supervisionado competitivo (LVQ-1) com alpha = 0.05...")
    lvq.train(X_treino, y_treino, epochs=1000, shuffle=True)
    print("-> Matriz de pesos (protótipos) ajustada com sucesso!\n")
    
    print("=== ETAPA 3: Classificação dos Perfis de Potência (Dias Inéditos) ===")
    # Matriz com os dados de teste exatos fornecidos na segunda tabela do roteiro
    X_teste = np.array([
        [2.9817, 1.5656, 4.8391, 1.4311, 4.1916, 6.9718], # Dia 1
        [1.5537, 2.2615, 1.3169, 2.5873, 1.7570, 5.0958], # Dia 2
        [1.2240, 0.2445, 1.3595, 5.4192, 3.2027, 2.5675], # Dia 3
        [2.5828, 1.5146, 2.1119, 1.2859, 2.3414, 1.8695], # Dia 4
        [2.4168, 1.4857, 1.8959, 1.3013, 2.4500, 1.7868], # Dia 5
        [1.0604, 0.2276, 1.2806, 5.4732, 3.2133, 2.4839], # Dia 6
        [1.5246, 2.4254, 1.1353, 2.5325, 1.7569, 5.2640], # Dia 7
        [3.0565, 1.6259, 4.7743, 1.3654, 4.2904, 6.9808]  # Dia 8
    ])
    
    # Realiza a inferência
    classes_preditas = lvq.predict(X_teste)
    
    print("Tabela de Resultados (Dados de Teste):")
    print("-" * 55)
    print("  Dia Inédito  |         BMU Vencedor (Perfil de Demanda)")
    print("-" * 55)
    
    for i, pred_classe in enumerate(classes_preditas):
        print(f"      Dia {i+1:02d}    |                 Classe {pred_classe}")
        
    print("-" * 55)

if __name__ == "__main__":
    executar_experimento_lvq()