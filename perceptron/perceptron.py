import numpy as np

class Perceptron:
    def __init__(self, n_inputs, learning_rate=0.01):
        # Inicializa o vetor de pesos com valores aleatórios entre 0 e 1
        self.weights = np.random.rand(n_inputs + 1)
        self.eta = learning_rate # Taxa de aprendizado fixa em 0.01
        self.x0 = -1  # Valor do bias conforme o enunciado

    def predict(self, inputs):
        # Soma ponderada: v = w0*x0 + w1*x1 + ...
        inputs_with_bias = np.insert(inputs, 0, self.x0)
        v = np.dot(self.weights, inputs_with_bias)
        # Função de ativação degrau bipolar
        return 1.0 if v >= 0 else -1.0

    def train(self, training_data, labels, max_epochs=1000):
        """
        Executa o treinamento usando a Regra de Hebb e rastreia os erros.
        """
        epochs = 0
        error_history = [] # NOVA: Lista para guardar o número de erros por época

        while epochs < max_epochs:
            errors = 0
            for x, d in zip(training_data, labels):
                y = self.predict(x)
                
                # Se houver erro, ajusta pesos pela Regra de Hebb
                if y != d:
                    x_with_bias = np.insert(x, 0, self.x0)
                    self.weights += self.eta * (d - y) * x_with_bias
                    errors += 1
            
            # Registra os erros desta época
            error_history.append(errors)
            
            # Se não houver erros, convergiu
            if errors == 0:
                break
            epochs += 1
            
        # NOVA: Retorna o histórico de erros junto com os pesos e total de épocas
        return self.weights, epochs, error_history