# 28/05/2026 - Script de Automação, Mapeamento e Teste - Kohonen (Completo e Corrigido)
import numpy as np
from kohonen import KohonenNet

def carregar_dados_treino(filepath="treinamento.csv"):
    """Carrega as 120 amostras do apêndice decodificando qualquer delimitador ou linha vazia."""
    X = []
    ids = []
    with open(filepath, mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            
            # Pula linhas vazias ou a linha de cabeçalho
            if not line or line.startswith("amostra"):
                continue
            
            # Identifica se o arquivo usa ponto e vírgula ou vírgula automaticamente
            separador = ";" if ";" in line else ","
            row = line.split(separador)
            
            # Garante que a linha possui todos os 4 elementos necessários (id, x1, x2, x3)
            if len(row) < 4:
                continue
                
            try:
                ids.append(int(row[0]))
                X.append([float(row[1]), float(row[2]), float(row[3])])
            except ValueError:
                # Ignora linhas com caracteres inválidos de forma segura
                continue
                
    return np.array(X), ids

def obter_classe_original(amostra_id):
    """Define a classe com base na divisão estrita do enunciado."""
    if 1 <= amostra_id <= 20:
        return "A"
    elif 21 <= amostra_id <= 60:
        return "B"
    elif 61 <= amostra_id <= 120:
        return "C"
    return "Desconhecida"

def executar_experimento_kohonen():
    # Fixa a semente aleatória global para garantir estabilidade geométrica do grid
    np.random.seed(42)
    
    print("=== ETAPA 1: Carregamento e Preparação dos Dados ===")
    X_treino, ids_treino = carregar_dados_treino("treinamento.csv")
    print(f"-> Sucesso: {len(X_treino)} amostras carregadas para o treino da borracha.\n")
    
    print("=== ETAPA 2: Treinamento da Rede de Kohonen (4x4) ===")
    # Instancia a rede com os parâmetros exatos do roteiro do Prof. Lázaro
    som = KohonenNet(input_dim=3, grid_shape=(4, 4), eta=0.001, radius=1)
    
    print("Treinando com eta=0.001 e Raio=1 por 5000 épocas... Por favor, aguarde.")
    som.train(X_treino, epochs=5000, shuffle=True)
    print("-> Treinamento auto-organizável concluído com sucesso!\n")
    
    print("=== ETAPA 3: Mapeamento Topológico do Grid (Rotulagem) ===")
    # Dicionário para computar quais amostras ativaram cada um dos 16 neurônios
    ativacoes_neuronios = {i: [] for i in range(16)}
    
    for i, x in enumerate(X_treino):
        amostra_id = ids_treino[i]
        classe_real = obter_classe_original(amostra_id)
        bmu = som.find_bmu(x)
        ativacoes_neuronios[bmu].append(classe_real)
        
    # Define a classe dominante de cada neurônio com base na maioria simples de ativações
    rotulos_grid = {}
    print("Análise de Ocupação por Neurônio:")
    for neuronio_idx in range(16):
        classes_presentes = ativacoes_neuronios[neuronio_idx]
        if len(classes_presentes) > 0:
            # Conta a moda (classe mais frequente)
            dominante = max(set(classes_presentes), key=classes_presentes.count)
            rotulos_grid[neuronio_idx] = dominante
            print(f"  Neurônio {neuronio_idx+1:02d} (Linha {neuronio_idx//4}, Col {neuronio_idx%4}): Classe Dominante {dominante} | Total de Ativações: {len(classes_presentes)}")
        else:
            rotulos_grid[neuronio_idx] = "Vazio"
            print(f"  Neurônio {neuronio_idx+1:02d} (Linha {neuronio_idx//4}, Col {neuronio_idx%4}): Sem ativações (Neurônio Inativo)")

    # Exibe visualmente o Grid Topológico 4x4 no terminal
    print("\n--- VISUALIZAÇÃO DO GRID TOPOLÓGICO (4x4) ---")
    for r in range(4):
        linha_str = []
        for c in range(4):
            idx = r * 4 + c
            linha_str.append(f"[{rotulos_grid[idx]}]")
        print("   " + "  ".join(linha_str))
    print("-" * 45 + "\n")

    print("=== ETAPA 4: Classificação das Amostras de Teste Inéditas ===")
    # Amostras fornecidas na tabela da Questão 2 do documento
    X_teste = np.array([
        [0.2471, 0.1778, 0.2905],
        [0.8240, 0.2223, 0.7041],
        [0.4960, 0.7231, 0.5866],
        [0.2923, 0.2041, 0.2234],
        [0.8118, 0.2668, 0.7484],
        [0.4837, 0.8200, 0.4792],
        [0.2923, 0.2041, 0.2234], 
        [0.7209, 0.2116, 0.7821],
        [0.5259, 0.6522, 0.5957],
        [0.2075, 0.1669, 0.1745],
        [0.7830, 0.3171, 0.7888],
        [0.5393, 0.7510, 0.5682]
    ])
    
    # Ajuste manual para a amostra 7 devido ao desalinhamento de digitação do roteiro original
    X_teste[6] = [0.3248, 0.2629, 0.2375]

    print("Tabela de Mapeamento dos Padrões de Teste:")
    print("Amostra |   x1   |   x2   |   x3   | BMU Vencedor | Classe Atribuída")
    print("-" * 65)
    
    for idx, x_amostra in enumerate(X_teste):
        bmu_vencedor = som.find_bmu(x_amostra)
        classe_atribuida = rotulos_grid[bmu_vencedor]
        
        # Se o neurônio vencedor for um neurônio sem ativação prévia, busca o vizinho mais próximo
        if classe_atribuida == "Vazio":
            dist_pesos = np.linalg.norm(som.W - x_amostra, axis=1)
            valid_indices = [k for k, v in rotulos_grid.items() if v != "Vazio"]
            bmu_vencedor = valid_indices[np.argmin(dist_pesos[valid_indices])]
            classe_atribuida = rotulos_grid[bmu_vencedor]
            
        print(f"   {idx+1:02d}   | {x_amostra[0]:.4f} | {x_amostra[1]:.4f} | {x_amostra[2]:.4f} |     {bmu_vencedor+1:02d}       |     Classe {classe_atribuida}")
    print("-" * 65)

if __name__ == "__main__":
    executar_experimento_kohonen()