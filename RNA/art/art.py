# 11/06/2026 - Estrutura da Rede ART-1 - Clustering de Entradas Binárias
import numpy as np

class ART1Net:
    def __init__(self, input_dim=16, rho=0.5, L=2.0):
        """
        Inicializa a rede ART-1.
        input_dim: Número de variáveis de entrada (16 variáveis de status).
        rho (ρ): Parâmetro de vigilância (0.0 a 1.0) - define o rigor da classificação.
        L: Parâmetro constante de atualização (geralmente L > 1).
        """
        self.input_dim = input_dim
        self.rho = rho
        self.L = L
        
        # A rede começa "em branco", sem nenhuma classe.
        # W = Pesos Bottom-Up (da entrada para a camada de reconhecimento F2)
        # T = Pesos Top-Down (da camada de reconhecimento F2 para a comparação F1)
        self.W = [] 
        self.T = [] 
        self.num_classes = 0

    def _create_new_class(self, x):
        """
        Aloca um novo neurônio (nova classe) quando a amostra não ressoa com os existentes.
        """
        # Inicialização dos pesos top-down (T) recebe o próprio padrão
        self.T.append(x.copy())
        
        # Inicialização dos pesos bottom-up (W) conforme a equação da ART-1
        # W_ji = (L * x_i) / (L - 1 + ||x||)
        norm_x = np.sum(x)
        novo_W = (self.L * x) / (self.L - 1 + norm_x)
        self.W.append(novo_W)
        
        self.num_classes += 1
        return self.num_classes - 1 # Retorna o índice da nova classe

    def predict(self, x):
        """
        Apresenta um padrão x à rede.
        Retorna o índice da classe na qual o padrão ressoou.
        """
        # Se não houver classes criadas, cria a primeira imediatamente
        if self.num_classes == 0:
            return self._create_new_class(x)

        # 1. Ativação (Bottom-Up)
        # Multiplica o vetor de entrada pela matriz de pesos W
        y = np.dot(self.W, x)
        
        # 2. Competição
        # Ordena os neurônios vencedores do maior para o menor grau de ativação
        ranking = np.argsort(y)[::-1]
        
        # 3. Teste de Vigilância (Orientação)
        norm_x = np.sum(x)
        
        for vencedor_idx in ranking:
            T_j = self.T[vencedor_idx]
            
            # Cálculo da interseção (AND lógico) entre a entrada x e o peso T_j
            # Como são arrays binários (0 e 1), a multiplicação elemento a elemento funciona como AND
            intersecao = x * T_j
            norm_intersecao = np.sum(intersecao)
            
            # Teste de Similaridade (M)
            match = norm_intersecao / norm_x if norm_x > 0 else 1.0
            
            # 4. Decisão: Ressonância ou Reset?
            if match >= self.rho:
                # RESSONÂNCIA: O padrão é parecido o suficiente! Atualiza os pesos.
                
                # Atualização Top-Down: T_novo = x AND T_antigo
                self.T[vencedor_idx] = intersecao
                
                # Atualização Bottom-Up: W_novo = (L * T_novo) / (L - 1 + ||T_novo||)
                self.W[vencedor_idx] = (self.L * intersecao) / (self.L - 1 + norm_intersecao)
                
                return vencedor_idx
                
        # 5. Esgotamento: Se falhou em todos os testes de vigilância, cria uma nova classe.
        return self._create_new_class(x)

    def train(self, X_train, epochs=10):
        """
        Treina a rede ART-1. Em geral, a ART-1 converge rapidamente (poucas épocas).
        Retorna as predições finais para os dados de entrada.
        """
        X_train = np.array(X_train)
        
        for epoch in range(epochs):
            for x in X_train:
                self.predict(x)
                
        # Retorna o mapeamento final
        mapeamento = []
        for x in X_train:
            # Chama o predict apenas para ver qual classe ativa sem alterar muito,
            # pois após a estabilização, os pesos não mudam mais.
            classe = self.predict(x)
            mapeamento.append(classe)
            
        return mapeamento