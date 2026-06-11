# 28/05/2026 - Estrutura da Rede de Kohonen - Atividade SOM 01
import numpy as np

class KohonenNet:
    def __init__(self, input_dim=3, grid_shape=(4, 4), eta=0.001, radius=1):
        """
        Inicializa o Mapa Auto-Organizável (SOM).
        input_dim: Quantidade de variáveis de entrada (x1, x2, x3) -> 3
        grid_shape: Dimensões da matriz topológica -> 4x4 (16 neurônios)
        eta: Taxa de aprendizado fixa -> 0.001
        radius: Raio de vizinhança estrutural -> 1
        """
        self.input_dim = input_dim
        self.grid_shape = grid_shape
        self.n_neurons = grid_shape[0] * grid_shape[1]
        self.eta = eta
        self.radius = radius
        
        # Inicialização dos pesos aleatórios entre 0 e 1 (alinhado aos limites do dataset)
        self.W = np.random.rand(self.n_neurons, self.input_dim)
        
        # Mapeamento matricial indexado: converte índice linear (0-15) em coordenadas 2D (linha, coluna)
        self.coords = np.array([(i // grid_shape[1], i % grid_shape[1]) for i in range(self.n_neurons)])

    def find_bmu(self, x):
        """
        Encontra o Best Matching Unit (BMU / Neurônio Vencedor).
        Calcula a menor distância Euclidiana entre o padrão de entrada e os vetores de pesos.
        """
        # Distância Euclidiana clássica d = sqrt(sum((w_j - x)^2))
        distancias = np.linalg.norm(self.W - x, axis=1)
        return np.argmin(distancias)

    def update_weights(self, x, bmu_idx):
        """
        Atualiza os pesos do neurônio vencedor e de sua vizinhança topológica direta.
        Utiliza a distância de Manhattan no grid para delimitar o raio R = 1.
        """
        bmu_coord = self.coords[bmu_idx]
        
        # Calcula a distância absoluta (Manhattan) de todos os neurônios do grid em relação ao BMU
        grid_distances = np.sum(np.abs(self.coords - bmu_coord), axis=1)
        
        # Filtra a máscara booleana dos neurônios que estão dentro do raio de cobertura (<= 1)
        vizinhos = grid_distances <= self.radius
        
        # Regra de Kohonen vetorizada: w(t+1) = w(t) + eta * (x - w(t))
        # Derivada direta da minimização do erro quadrático da norma Euclidiana
        self.W[vizinhos] += self.eta * (x - self.W[vizinhos])

    def train(self, X_train, epochs=2000, shuffle=True):
        """
        Executa o laço cíclico de treinamento auto-organizável.
        Como a taxa de aprendizado e o raio são fixos por exigência do roteiro,
        a estabilização é atingida pelo volume de iterações.
        """
        X_train = np.array(X_train, dtype=float)
        
        for epoch in range(epochs):
            # Embaralha as amostras a cada época para evitar vício de ordenação no grid
            if shuffle:
                np.random.shuffle(X_train)
                
            for x in X_train:
                bmu_idx = self.find_bmu(x)
                self.update_weights(x, bmu_idx)
                
        return self.W