# 28/05/2026 - Script de Simulação e Validação - Hopfield
import numpy as np
from hopfield import HopfieldNetwork

def injetar_ruido(padrao, nivel_ruido=0.20):
    """Inverte a polaridade de exatamente 20% dos pixels (9 pixels de 45)"""
    ruidoso = np.copy(padrao)
    n_elementos = len(padrao)
    n_corromper = int(n_elementos * nivel_ruido)
    indices = np.random.choice(n_elementos, n_corromper, replace=False)
    ruidoso[indices] *= -1
    return ruidoso

def exibir_lado_a_lado(orig, ruidoso, recuperado):
    """Exibe os três grids de forma síncrona e horizontal no terminal"""
    orig_m = orig.reshape(9, 5)
    ruidoso_m = ruidoso.reshape(9, 5)
    rec_m = recuperado.reshape(9, 5)
    
    print("  [Transmitida]          [Distorcida]            [Limpa]")
    for r in range(9):
        str_orig = "".join(['█' if p == 1 else '.' for p in orig_m[r]])
        str_ruidoso = "".join(['█' if p == 1 else '.' for p in ruidoso_m[r]])
        str_rec = "".join(['█' if p == 1 else '.' for p in rec_m[r]])
        print(f"   {str_orig}                  {str_ruidoso}                  {str_rec}")
    print("-" * 60)

# =====================================================================
# MAPEAMENTO MATRICIAL DOS NÚMEROS REAIS (9x5) DO LIBREOFFICE
# =====================================================================
# -1 = Pixel Branco | +1 = Pixel Escuro (█)

n1 = np.array([
    -1, -1,  1, -1, -1,
    -1,  1,  1, -1, -1,
    -1, -1,  1, -1, -1,
    -1, -1,  1, -1, -1,
    -1, -1,  1, -1, -1,
    -1, -1,  1, -1, -1,
    -1, -1,  1, -1, -1,
    -1, -1,  1, -1, -1,
    -1,  1,  1,  1, -1
])

n2 = np.array([
    -1,  1,  1,  1, -1,
     1, -1, -1, -1,  1,
    -1, -1, -1, -1,  1,
    -1, -1, -1,  1, -1,
    -1, -1,  1, -1, -1,
    -1,  1, -1, -1, -1,
     1, -1, -1, -1, -1,
     1, -1, -1, -1, -1,
     1,  1,  1,  1,  1
])

n3 = np.array([
     1,  1,  1,  1,  1,
    -1, -1, -1, -1,  1,
    -1, -1, -1, -1,  1,
    -1, -1, -1,  1, -1,
    -1,  1,  1,  1, -1,
    -1, -1, -1, -1,  1,
    -1, -1, -1, -1,  1,
    -1, -1, -1, -1,  1,
     1,  1,  1,  1,  1
])

n4 = np.array([
     1, -1, -1, -1,  1,
     1, -1, -1, -1,  1,
     1, -1, -1, -1,  1,
     1, -1, -1, -1,  1,
     1,  1,  1,  1,  1,
    -1, -1, -1, -1,  1,
    -1, -1, -1, -1,  1,
    -1, -1, -1, -1,  1,
    -1, -1, -1, -1,  1
])

padroes_fundamentais = np.array([n1, n2, n3, n4])

def simular_link_transmissao():
    # Inicializa e treina a memória associativa uma única vez com os 4 números
    rede = HopfieldNetwork(num_neurons=45)
    rede.train_hebbian(padroes_fundamentais)
    
    print("=== INICIANDO SIMULAÇÃO DAS 12 SITUAÇÕES DE TRANSMISSÃO ===\n")
    
    # Varre cada um dos 4 números fundamentais
    for n_idx, original in enumerate(padroes_fundamentais):
        print(f"==================== NÚMERO {n_idx + 1} ====================\n")
        
        # Executa as 3 situações de teste independentes por padrão
        for t_idx in range(1, 4):
            print(f"-> Situação de Teste #{t_idx} para o Número {n_idx + 1}:")
            
            # Aplica os 20% de ruído estocástico exigidos
            ruidoso = injetar_ruido(original, nivel_ruido=0.20)
            
            # Recupera a imagem limpa usando a dinâmica assíncrona
            recuperado = rede.predict(ruidoso, async_update=True)
            
            # Desenha as 3 colunas de forma síncrona
            exibir_lado_a_lado(original, ruidoso, recuperado)
            
            # Validação lógica de restauração
            sucesso = np.array_equal(recuperado, original)
            print(f"STATUS DA TRANSMISSÃO: {'SUCESSO (Restauração Fiel)' if sucesso else 'FALHA'}\n")

if __name__ == "__main__":
    simular_link_transmissao()