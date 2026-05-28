# 19/05 - Estrutura da Rede RBF - Atividade 1 (Corrigido)
import numpy as np

class RBFNet:
    def __init__(self, n_clusters=2):
        self.n_clusters = n_clusters
        self.centers = None
        self.variances = None
        self.W = None 

    def train_hidden_layer(self, X_kmeans):
        """
        Executa o k-means clássico para encontrar 2 centros.
        Baseado apenas nos padrões com d = 1.
        """
        # Inicialização determinística com os primeiros pontos para garantir reprodutibilidade
        self.centers = np.copy(X_kmeans[:self.n_clusters])
        
        for _ in range(100):
            # Atribuição de clusters pela distância Euclidiana
            distancias = np.linalg.norm(X_kmeans[:, np.newaxis] - self.centers, axis=2)
            labels = np.argmin(distancias, axis=1)
            
            # Atualização dos centros pela média geométrica dos pontos do grupo
            novos_centros = np.array([X_kmeans[labels == k].mean(axis=0) for k in range(self.n_clusters)])
            
            if np.allclose(self.centers, novos_centros):
                break
            self.centers = novos_centros

        # Cálculo da Variância (sigma^2) de cada cluster
        self.variances = np.zeros(self.n_clusters)
        for k in range(self.n_clusters):
            pontos_cluster = X_kmeans[labels == k]
            if len(pontos_cluster) > 0:
                self.variances[k] = np.mean(np.sum((pontos_cluster - self.centers[k])**2, axis=1))
            else:
                self.variances[k] = 1.0 

        return self.centers, self.variances

    def gaussian_rbf(self, x, center, variance):
        """Calcula a ativação da base radial usando a função Gaussiana."""
        dist_sq = np.sum((x - center)**2)
        return np.exp(-dist_sq / (2 * variance))

    def compute_hidden_activations(self, X):
        """Gera a matriz de ativação H incluindo o Bias (+1)."""
        n_samples = X.shape[0]
        H = np.ones((n_samples, self.n_clusters + 1)) # Coluna 0 é o Bias (W21,0)
        
        for i in range(n_samples):
            for j in range(self.n_clusters):
                H[i, j + 1] = self.gaussian_rbf(X[i], self.centers[j], self.variances[j])
        return H

    def train_output_layer(self, X_train, D_train, eta=0.01, precision=1e-7, max_epochs=50000):
        """
        Treina a camada de saída utilizando a Regra Delta Generalizada.
        Critério de parada corrigido para avaliar a variação infinitesimal do EQM (Δ EQM) 
        entre épocas consecutivas, evitando loops infinitos em platôs de erro residual.
        """
        n_samples = X_train.shape[0]
        H = self.compute_hidden_activations(X_train)
        
        # Inicialização com zeros para acelerar a convergência linear estável
        self.W = np.zeros((self.n_clusters + 1, 1))
        
        epochs = 0
        eqm_atual = 1.0
        diff_eqm = 1.0  # Guarda a variação absoluta do erro entre as épocas (Delta)
        
        # O loop agora monitora se a taxa de aprendizado estagnou abaixo da precisão desejada
        while diff_eqm > precision and epochs < max_epochs:
            error_sum = 0
            
            for i in range(n_samples):
                h = H[i].reshape(-1, 1)
                d = D_train[i]
                
                # Saída linear do combinador
                y = np.dot(self.W.T, h)[0, 0]
                
                error = d - y
                error_sum += error**2
                
                # Atualização do peso (Regra Delta)
                self.W += eta * error * h

            eqm_novo = error_sum / (2 * n_samples)
            
            # A partir da segunda época, calcula a variação real do aprendizado
            if epochs > 0:
                diff_eqm = abs(eqm_novo - eqm_atual)
            
            eqm_atual = eqm_novo
            epochs += 1
            
            # Print inteligente adaptado para monitorar o comportamento do Delta (variação)
            if epochs % 10000 == 0:
                print(f"Época {epochs:5d} | EQM RBF: {eqm_atual:.8f} | Variação (Δ): {diff_eqm:.10f}")
                
        return epochs, self.W

    def predict(self, X, pos_processar=False):
        """Realiza a inferência com a rede."""
        H = self.compute_hidden_activations(X)
        y_real = np.dot(H, self.W)
        
        if pos_processar:
            # Função sinal estrita para o pós-processamento do teste
            return np.where(y_real >= 0, 1, -1)
        return y_real