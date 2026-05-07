import numpy as np

class Adaline:
    def __init__(self, n_inputs, learning_rate=0.0025, precision=1e-6):
        # Inicializa pesos aleatórios entre 0 e 1 [cite: 68]
        # n_inputs + 1 (bias)
        self.weights = np.random.rand(n_inputs + 1)
        self.eta = learning_rate # Taxa de aprendizado solicitada 
        self.epsilon = precision # Precisão solicitada 
        self.x0 = -1 # Valor do bias definido no diagrama [cite: 36, 53]

    def activation(self, inputs):
        """Calcula o potencial de ativação (saída linear) u."""
        inputs_with_bias = np.insert(inputs, 0, self.x0)
        return np.dot(self.weights, inputs_with_bias)

    def predict(self, inputs):
        """Aplica a função de ativação degrau bipolar g(u). [cite: 32, 42, 59]"""
        u = self.activation(inputs)
        return 1.0 if u >= 0 else -1.0

    def train(self, training_data, labels, max_epochs=2000):
        """Treina a rede usando a Regra Delta. """
        n_samples = len(training_data)
        epochs = 0
        mse_history = []
        
        while epochs < max_epochs:
            # Armazena o EQM da época anterior para verificar a precisão
            mse_prev = self.calculate_mse(training_data, labels)
            
            for x, d in zip(training_data, labels):
                # u é a saída linear (antes da função degrau) [cite: 43, 60]
                u = self.activation(x)
                
                # Regra Delta: Δw = η * (d - u) * x 
                x_with_bias = np.insert(x, 0, self.x0)
                self.weights += self.eta * (d - u) * x_with_bias
                
            # Calcula o novo EQM após ajustar os pesos
            mse_current = self.calculate_mse(training_data, labels)
            mse_history.append(mse_current)
            
            # Critério de Parada: precisão baseada no Erro Quadrático Médio 
            if abs(mse_current - mse_prev) <= self.epsilon:
                break
                
            epochs += 1
            
        return self.weights, epochs, mse_history

    def calculate_mse(self, X, d):
        """Calcula o Erro Quadrático Médio (EQM). """
        errors_sum = 0
        for x_sample, d_sample in zip(X, d):
            u = self.activation(x_sample)
            errors_sum += (d_sample - u)**2
        return errors_sum / len(X)