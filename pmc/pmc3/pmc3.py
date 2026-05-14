# 14/05 - Atividade 3 - PMC03
import numpy as np

class PMC:
    def __init__(self, n_in, n_hidden, n_out):
        # Inicialização de pesos entre 0 e 1
        self.V = np.random.rand(n_hidden, n_in + 1) 
        self.W = np.random.rand(n_out, n_hidden + 1)
        # Matrizes para o Termo de Momento
        self.dV_ant = np.zeros_like(self.V)
        self.dW_ant = np.zeros_like(self.W)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, X):
        # Camada Escondida
        self.X_bias = np.append(X, 1) # Adiciona bias
        self.Zin = np.dot(self.V, self.X_bias)
        self.Z = self.sigmoid(self.Zin)
        
        # Camada de Saída
        self.Z_bias = np.append(self.Z, 1)
        self.Yin = np.dot(self.W, self.Z_bias)
        self.Y = self.sigmoid(self.Yin)
        return self.Y

    def train(self, X_train, D_train, eta=0.1, alpha=0.8, precision=0.5e-6):
        epochs = 0
        eqm = 1.0
        eqm_hist = []

        while eqm > precision:
            error_sum = 0
            # Embaralha os dados a cada época para melhor convergência
            indices = np.arange(len(X_train))
            np.random.shuffle(indices)

            for i in indices:
                X = X_train[i]
                D = D_train[i]
                
                # Forward
                Y = self.forward(X)
                
                # Backpropagation (Saída)
                error = D - Y
                error_sum += np.sum(error**2)
                delta_w = error * Y * (1 - Y)
                
                # Backpropagation (Escondida)
                delta_v = (self.Z * (1 - self.Z)) * np.dot(delta_w, self.W[:, :-1])
                
                # Atualização com Momentum
                dW = eta * np.outer(delta_w, self.Z_bias) + alpha * self.dW_ant
                dV = eta * np.outer(delta_v, self.X_bias) + alpha * self.dV_ant
                
                self.W += dW
                self.V += dV
                
                self.dW_ant = dW
                self.dV_ant = dV

            eqm = error_sum / (2 * len(X_train))
            eqm_hist.append(eqm)
            epochs += 1
            if epochs % 1000 == 0:
                print(f"Época {epochs} - EQM: {eqm:.8f}")
        
        return epochs, eqm_hist