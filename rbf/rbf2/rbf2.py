# 19/05 - Estrutura da Rede RBF - Atividade 2 (Aproximação Funcional)
import numpy as np

class RBFNetDynamic:
    def __init__(self, n_clusters):
        self.n_clusters = n_clusters
        self.centers = None
        self.variances = None
        self.W = None 

    def train_hidden_layer(self, X_train):
        """
        Executa o k-means para encontrar N1 centros usando todo o dataset de treino,
        já que o problema é de aproximação funcional.
        """
        # Seleção dos primeiros pontos de forma determinística para garantir a estabilidade
        # geométrica dos centros antes do treino da camada linear.
        self.centers = np.copy(X_train[:self.n_clusters])
        
        for _ in range(100):
            # Atribuição de clusters pela distância Euclidiana
            distancias = np.linalg.norm(X_train[:, np.newaxis] - self.centers, axis=2)
            labels = np.argmin(distancias, axis=1)
            
            # Atualização dos centros pela média geométrica dos pontos do grupo
            novos_centros = []
            for k in range(self.n_clusters):
                pontos_cluster = X_train[labels == k]
                if len(pontos_cluster) > 0:
                    novos_centros.append(pontos_cluster.mean(axis=0))
                else:
                    novos_centros.append(X_train[np.random.choice(X_train.shape[0])])
            
            novos_centros = np.array(novos_centros)
            if np.allclose(self.centers, novos_centros):
                break
            self.centers = novos_centros

        # Cálculo da Variância (sigma^2) de cada cluster
        self.variances = np.zeros(self.n_clusters)
        for k in range(self.n_clusters):
            pontos_cluster = X_train[labels == k]
            if len(pontos_cluster) > 0:
                self.variances[k] = np.mean(np.sum((pontos_cluster - self.centers[k])**2, axis=1))
                # Evita variância zero em clusters muito densos
                if self.variances[k] == 0:
                    self.variances[k] = 0.1
            else:
                self.variances[k] = 1.0 

        return self.centers, self.variances

    def gaussian_rbf(self, x, center, variance):
        """Calcula a ativação da base radial usando a função Gaussiana."""
        dist_sq = np.sum((x - center)**2)
        return np.exp(-dist_sq / (2 * variance))

    def compute_hidden_activations(self, X):
        """Gera a matriz de ativação H incluindo o Bias (+1) na primeira coluna."""
        n_samples = X.shape[0]
        H = np.ones((n_samples, self.n_clusters + 1))
        
        for i in range(n_samples):
            for j in range(self.n_clusters):
                H[i, j + 1] = self.gaussian_rbf(X[i], self.centers[j], self.variances[j])
        return H

    def train_output_layer(self, X_train, D_train, eta=0.01, precision=1e-7, seed=None, max_epochs=150000):
        """
        Treina a camada de saída linear usando a Regra Delta Generalizada.
        Inicialização obrigatória com valores aleatórios entre 0 e 1.
        """
        if seed is not None:
            np.random.seed(seed) # Garante matrizes iniciais estritamente diferentes por treino
            
        n_samples = X_train.shape[0]
        H = self.compute_hidden_activations(X_train)
        
        # Exigência do roteiro: pesos aleatórios entre 0 e 1
        self.W = np.random.rand(self.n_clusters + 1, 1)
        
        epochs = 0
        eqm = 1.0
        eqm_history = []
        
        # Loop de otimização linear com teto de segurança contra loop infinito
        while eqm > precision and epochs < max_epochs:
            error_sum = 0
            
            for i in range(n_samples):
                h = H[i].reshape(-1, 1)
                d = D_train[i]
                
                # Saída contínua pura (Problema de aproximação funcional)
                y = np.dot(self.W.T, h)[0, 0]
                
                error = d - y
                error_sum += error**2
                
                # Ajuste linear dos pesos (Regra Delta)
                self.W += eta * error * h

            eqm = error_sum / (2 * n_samples)
            eqm_history.append(eqm)
            epochs += 1
            
        return epochs, eqm, eqm_history

    def predict(self, X):
        """Realiza a inferência contínua (sem pós-processamento de sinal)."""
        H = self.compute_hidden_activations(X)
        return np.dot(H, self.W)