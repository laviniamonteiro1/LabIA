# 19/05 - Script de Automação e Gráficos - RBF 02 (Corrigido)
import numpy as np
import matplotlib.pyplot as plt
from dados_rbf2 import X_treino, D_treino, X_teste, D_teste
from rbf2 import RBFNetDynamic

def executar_bateria_rbf2():
    # Definição das topologias candidatas solicitadas pelo professor
    topologias = [
        {'nome': 'Rede 1', 'N1': 5},
        {'nome': 'Rede 2', 'N1': 10},
        {'nome': 'Rede 3', 'N1': 15}
    ]
    
    # Estruturas para armazenar os logs de treino e predições para as tabelas
    tabela_treino = {}
    melhores_historicos = {}
    predicoes_teste = {i: {} for i in range(1, 16)} # Linhas de 1 a 15 para o teste
    metricas_teste = {}

    print("=== INICIANDO BATERIA DE 9 TREINAMENTOS RBF ===")
    
    for topo in topologias:
        nome = topo['nome']
        N1 = topo['N1']
        tabela_treino[nome] = []
        metricas_teste[nome] = []
        
        print(f"\n>>> Processando {nome} (N1 = {N1} neurônios ocultos) <<<")
        
        # Variáveis para capturar a melhor rodada da topologia para o gráfico
        melhor_eqm_treino = float('inf')
        melhor_hist = None
        melhor_t_idx = 1
        
        # Executa os 3 treinamentos independentes solicitados
        for t_idx in range(1, 4):
            # Define uma semente baseada no número de neurônios e no índice do treino
            semente_aleatoria = N1 * 100 + t_idx * 7
            
            net = RBFNetDynamic(n_clusters=N1)
            
            # Etapa 1: K-means
            net.train_hidden_layer(X_treino)
            
            # Etapa 2: Regra Delta com taxa=0.01 e precisão de variação=10^-7
            epocas, eqm_final, historico_eqm = net.train_output_layer(
                X_treino, D_treino, eta=0.01, precision=1e-7, seed=semente_aleatoria
            )
            
            # Converte o array do NumPy para float nativo do Python
            eqm_final = float(eqm_final)
            
            tabela_treino[nome].append({'epocas': epocas, 'eqm': eqm_final})
            print(f"  > Treinamento T{t_idx}: Finalizado em {epocas} épocas | EQM Final: {eqm_final:.7f}")
            
            # Validação no conjunto de teste
            y_pred = net.predict(X_teste).flatten()
            d_alvo = D_teste.flatten()
            
            # Cálculo do Erro Relativo Médio (%) e Variância (%) ponto a ponto
            erros_relativos = (np.abs(d_alvo - y_pred) / d_alvo) * 100
            erro_rel_medio = np.mean(erros_relativos)
            variancia_erro = np.var(erros_relativos)
            
            metricas_teste[nome].append({
                't_idx': t_idx, 'erm': erro_rel_medio, 'var': variancia_erro
            })
            
            # Guarda as predições de cada uma das 15 amostras para a grande tabela de validação
            for idx_amostra in range(15):
                predicoes_teste[idx_amostra + 1][f"{nome}_T{t_idx}"] = y_pred[idx_amostra]
            
            if eqm_final < melhor_eqm_treino:
                melhor_eqm_treino = eqm_final
                melhor_hist = historico_eqm
                melhor_t_idx = t_idx
                
        # Armazena o histórico da curva de erro da melhor rodada
        melhores_historicos[nome] = {'historico': melhor_hist, 't_idx': melhor_t_idx}

    print("\n" + "="*60 + "\n=== SIMULAÇÃO CONCLUÍDA! IMPRIMINDO TABELAS ===\n" + "="*60)
    
    # --- GERADOR DE TEXTO PARA A TABELA 1: CONVERGÊNCIA ---
    print("\nTABELA 1: Histórico de Convergência (Treinamento)")
    print("Treinamento |   Rede 1 (N1=5)   |   Rede 2 (N1=10)  |   Rede 3 (N1=15)  ")
    print("            |   EQM   |  Épocas |   EQM   |  Épocas |   EQM   |  Épocas ")
    print("-"*76)
    for t in range(3):
        r1 = tabela_treino['Rede 1'][t]
        r2 = tabela_treino['Rede 2'][t]
        r3 = tabela_treino['Rede 3'][t]
        print(f"  T{t+1} (T{t+1})  | {r1['eqm']:.5f} | {r1['epocas']:7d} | {r2['eqm']:.5f} | {r2['epocas']:7d} | {r3['eqm']:.5f} | {r3['epocas']:7d}")

    # --- GERADOR DE TEXTO PARA A TABELA 2: VALIDAÇÃO COMPLETA ---
    print("\n\nTABELA 2: Mapeamento e Validação (Conjunto de Teste)")
    print("Amostra | Desejado (d) | R1_T1  | R1_T2  | R1_T3  | R2_T1  | R2_T2  | R2_T3  | R3_T1  | R3_T2  | R3_T3  ")
    print("-"*110)
    for am in sorted(predicoes_teste.keys()):
        d_val = D_teste[am-1][0]
        p = predicoes_teste[am]
        print(f"   {am:02d}   |    {d_val:.4f}    | {p['Rede 1_T1']:.4f} | {p['Rede 1_T2']:.4f} | {p['Rede 1_T3']:.4f} | {p['Rede 2_T1']:.4f} | {p['Rede 2_T2']:.4f} | {p['Rede 2_T3']:.4f} | {p['Rede 3_T1']:.4f} | {p['Rede 3_T2']:.4f} | {p['Rede 3_T3']:.4f}")
    
    print("-"*110)
    # Imprime as linhas de rodapé com Erro Relativo Médio e Variância
    print("Erro Relat. Médio (%): | " + " | ".join([f"{m['erm']:2.2f}%" for r in ['Rede 1', 'Rede 2', 'Rede 3'] for m in metricas_teste[r]]))
    print("Variância (%):         | " + " | ".join([f"{m['var']:2.2f}%" for r in ['Rede 1', 'Rede 2', 'Rede 3'] for m in metricas_teste[r]]))

    # --- GERADOR DE GRÁFICOS: 3 SUBPLOTS NÃO SUPERPOSTOS ---
    fig, axs = plt.subplots(3, 1, figsize=(9, 12), sharex=False)
    fig.suptitle("Evolução do Erro Quadrático Médio (EQM) - Melhores Treinamentos", fontsize=14, fontweight='bold')
    
    cores = ['firebrick', 'navy', 'darkgreen']
    for i, r_nome in enumerate(['Rede 1', 'Rede 2', 'Rede 3']):
        dados_grafico = melhores_historicos[r_nome]
        axs[i].plot(dados_grafico['historico'], color=cores[i], lw=2, label=f"Melhor Treino: T{dados_grafico['t_idx']}")
        axs[i].set_title(f"Histórico de Convergência - {r_nome}", fontsize=11, fontweight='bold')
        axs[i].set_ylabel("EQM Linear")
        axs[i].set_xlabel("Épocas de Treinamento")
        axs[i].grid(True, linestyle="--", alpha=0.6)
        axs[i].legend(loc="upper right")
        axs[i].set_yscale('log')
        
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    # Salva a imagem na mesma pasta de execução
    plt.savefig("convergencia_rbf2.png", dpi=300)
    print("\n\n[OK] Gráfico comparativo gerado e salvo como 'convergencia_rbf2.png' na pasta.")
    plt.show()

if __name__ == "__main__":
    executar_bateria_rbf2()