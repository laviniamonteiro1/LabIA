import numpy as np

class PMC2:
    def __init__(self, n_inputs, n_hidden, n_outputs, eta=0.1, alpha=0.9, epsilon=1e-6):
        self.eta = eta
        self.alpha = alpha # Fator de Momentum [cite: 40]
        self.epsilon = epsilon
        self.x0 = -1
        
        # Pesos iniciais (serão definidos externamente para garantir igualdade nos testes)
        self.V = None 
        self.W = None
        
        # Memória para o Momentum (Variação anterior dos pesos)
        self.prev_delta_V = 0
        self.prev_delta_W = 0

    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def train(self, X, d_targets, use_momentum=False, max_epochs=100000):
        n_samples = len(X)
        epochs = 0
        mse_history = []
        
        # Reset de memória de momentum para novo treino
        self.prev_delta_V = np.zeros_like(self.V)
        self.prev_delta_W = np.zeros_like(self.W)

        while epochs < max_epochs:
            mse_prev = self.calculate_mse(X, d_targets)
            
            for i in range(n_samples):
                # FEEDFORWARD
                X_wb = np.insert(X[i], 0, self.x0)
                y_h = self.sigmoid(np.dot(self.V, X_wb))
                y_h_wb = np.insert(y_h, 0, self.x0)
                y_o = self.sigmoid(np.dot(self.W, y_h_wb))
                
                # BACKPROPAGATION
                error_o = d_targets[i] - y_o
                delta_o = error_o * y_o * (1 - y_o)
                delta_h = y_h * (1 - y_h) * np.dot(delta_o, self.W[:, 1:])
                
                # CÁLCULO DO AJUSTE (Com ou sem Momentum)
                grad_W = np.outer(delta_o, y_h_wb)
                grad_V = np.outer(delta_h, X_wb)
                
                if use_momentum:
                    # Delta_w(t) = eta * grad + alpha * Delta_w(t-1) 
                    delta_W = (self.eta * grad_W) + (self.alpha * self.prev_delta_W)
                    delta_V = (self.eta * grad_V) + (self.alpha * self.prev_delta_V)
                else:
                    delta_W = self.eta * grad_W
                    delta_V = self.eta * grad_V
                
                # Atualização e salvamento para próxima época
                self.W += delta_W
                self.V += delta_V
                self.prev_delta_W = delta_W
                self.prev_delta_V = delta_V

            mse_curr = self.calculate_mse(X, d_targets)
            mse_history.append(mse_curr)
            if abs(mse_curr - mse_prev) <= self.epsilon: break
            epochs += 1
            
        return epochs, mse_history

    def calculate_mse(self, X, d):
        mse = 0
        for i in range(len(X)):
            X_wb = np.insert(X[i], 0, self.x0)
            y_h = self.sigmoid(np.dot(self.V, X_wb))
            y_h_wb = np.insert(y_h, 0, self.x0)
            y_o = self.sigmoid(np.dot(self.W, y_h_wb))
            mse += np.sum((d[i] - y_o)**2)
        return mse / (len(X) * d.shape[1])