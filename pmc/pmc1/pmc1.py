import numpy as np

class PMC:
    def __init__(self, n_inputs, n_hidden, n_outputs, eta=0.1, epsilon=1e-6):
        # Inicialização aleatória entre 0 e 1 conforme enunciado
        self.V = np.random.rand(n_hidden, n_inputs + 1) # Pesos Camada Escondida
        self.W = np.random.rand(n_outputs, n_hidden + 1) # Pesos Camada Saída
        self.eta = eta
        self.epsilon = epsilon
        self.x0 = -1 # Bias

    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def train(self, X, d_targets, max_epochs=100000):
        n_samples = len(X)
        epochs = 0
        mse_history = []

        while epochs < max_epochs:
            mse_prev = self.calculate_mse(X, d_targets)
            
            for i in range(n_samples):
                # 1. FEEDFORWARD
                # Camada Escondida
                X_with_bias = np.insert(X[i], 0, self.x0)
                u_h = np.dot(self.V, X_with_bias)
                y_h = self.sigmoid(u_h)
                
                # Camada de Saída
                y_h_with_bias = np.insert(y_h, 0, self.x0)
                u_o = np.dot(self.W, y_h_with_bias)
                y_o = self.sigmoid(u_o) # Saída final da rede
                
                # 2. BACKPROPAGATION (Ajuste de Pesos)
                # Erro na Saída
                error_o = d_targets[i] - y_o
                delta_o = error_o * y_o * (1 - y_o)
                
                # Erro na Camada Escondida (Retropropagação)
                # Remove o peso do bias do cálculo do delta
                delta_h = y_h * (1 - y_h) * np.dot(delta_o, self.W[:, 1:])
                
                # 3. ATUALIZAÇÃO DOS PESOS
                self.W += self.eta * np.outer(delta_o, y_h_with_bias)
                self.V += self.eta * np.outer(delta_h, X_with_bias)

            mse_curr = self.calculate_mse(X, d_targets)
            mse_history.append(mse_curr)
            
            # Critério de Parada pela Precisão solicitada
            if abs(mse_curr - mse_prev) <= self.epsilon:
                break
            epochs += 1
            
        return epochs, mse_history

    def calculate_mse(self, X, d):
        mse = 0
        for i in range(len(X)):
            X_with_bias = np.insert(X[i], 0, self.x0)
            y_h = self.sigmoid(np.dot(self.V, X_with_bias))
            y_h_with_bias = np.insert(y_h, 0, self.x0)
            y_o = self.sigmoid(np.dot(self.W, y_h_with_bias))
            mse += (d[i] - y_o)**2
        return (mse / len(X))[0]