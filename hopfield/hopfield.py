# LabIA/hopfield/hopfield.py
import numpy as np

class HopfieldNetwork:
    def __init__(self, num_neurons=45):
        """
        Inicializa a Rede de Hopfield com o número de neurônios correspondente
        ao tamanho do vetor de características (45 bits para as imagens).
        """
        self.n = num_neurons
        self.W = np.zeros((num_neurons, num_neurons))

    def train_hebbian(self, patterns):
        """
        Treina a rede utilizando a regra do produto externo (Regra Hebbiana).
        patterns: np.array de formato (M, N), onde M é o número de padrões e N = 45.
        """
        patterns = np.array(patterns, dtype=float)
        num_patterns = patterns.shape[0]
        
        # Regra do produto externo: W = (1/N) * sum(xi * xi^T)
        self.W = np.dot(patterns.T, patterns) / self.n
        
        # Auto-realimentação nula: garante estabilidade e convergência zerando a diagonal
        np.fill_diagonal(self.W, 0)

    def predict(self, noisy_pattern, max_iter=100, async_update=True):
        """
        Recupera o padrão original a partir de uma entrada ruidosa.
        A função de ativação simula a Tangente Hiperbólica com ganho beta muito grande,
        o que equivale matematicamente à função sgn(u).
        """
        s = np.copy(noisy_pattern).astype(float)
        
        if async_update:
            # Atualização Assíncrona (Recomendada para garantir convergência a mínimos locais estáveis)
            for _ in range(max_iter):
                s_old = np.copy(s)
                # Permuta a ordem dos neurônios a cada iteração para evitar vieses de varredura
                indices = np.random.permutation(self.n)
                for i in indices:
                    u = np.dot(self.W[i], s)
                    # Ganho muito grande na Tangente Hiperbólica aproxima-se da função sinal (sgn)
                    if u > 0:
                        s[i] = 1.0
                    elif u < 0:
                        s[i] = -1.0
                    # Se u == 0, o neurônio mantém o estado anterior s[i]
                
                if np.array_equal(s, s_old):
                    break
        else:
            # Atualização Síncrona
            for _ in range(max_iter):
                s_old = np.copy(s)
                u = np.dot(self.W, s)
                s = np.where(u >= 0, 1.0, -1.0)
                if np.array_equal(s, s_old):
                    break
                    
        return s