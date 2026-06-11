# 11/06/2026 - Estrutura da Rede LVQ-1 - Classificação de Perfil de Potência
import numpy as np

class LVQ1Net:
    def __init__(self, input_dim=6, num_classes=4, alpha=0.05):
        """
        Inicializa a Rede LVQ-1.
        input_dim: Quantidade de variáveis de entrada (7h, 8h, 9h, 10h, 11h, 12h) -> 6
        num_classes: Quantidade de classes/perfis de potência -> 4
        alpha: Taxa de aprendizagem fixa -> 0.05
        """
        self.input_dim = input_dim
        self.num_classes = num_classes
        self.alpha = alpha
        
        # A matriz de pesos (W) representa os protótipos de cada classe.
        # Será inicializada depois, usando amostras reais para acelerar a convergência.
        self.W = None
        self.classes_w = np.arange(1, num_classes + 1) # Rótulos: [1, 2, 3, 4]

    def initialize_weights(self, X_train, y_train):
        """
        Inicializa os pesos da rede pegando a primeira amostra encontrada
        de cada classe no conjunto de treinamento. Isso posiciona os
        neurônios iniciais já dentro das bacias de atração corretas.
        """
        self.W = np.zeros((self.num_classes, self.input_dim))
        classes_encontradas = set()
        
        for i, (x, y) in enumerate(zip(X_train, y_train)):
            if y not in classes_encontradas:
                idx = np.where(self.classes_w == y)[0][0]
                self.W[idx] = x.copy()
                classes_encontradas.add(y)
            
            if len(classes_encontradas) == self.num_classes:
                break
                
        # Aviso caso o dataset não tenha todas as classes
        if len(classes_encontradas) < self.num_classes:
            print("Aviso: Nem todas as classes foram encontradas para inicialização.")

    def find_bmu(self, x):
        """
        Encontra o Best Matching Unit (BMU / Neurônio Vencedor).
        Calcula a menor distância Euclidiana entre o padrão e os vetores de pesos.
        Retorna o índice do neurônio vencedor na matriz W.
        """
        distancias = np.linalg.norm(self.W - x, axis=1)
        return np.argmin(distancias)

    def train(self, X_train, y_train, epochs=500, shuffle=True):
        """
        Executa o treinamento supervisionado competitivo (LVQ-1).
        """
        X_train = np.array(X_train, dtype=float)
        y_train = np.array(y_train, dtype=int)
        
        # Se os pesos não foram inicializados, inicializa agora
        if self.W is None:
            self.initialize_weights(X_train, y_train)
            
        for epoch in range(epochs):
            if shuffle:
                # Embaralha os dados em uníssono para evitar vícios
                indices = np.random.permutation(len(X_train))
                X_train = X_train[indices]
                y_train = y_train[indices]
                
            for x, y_real in zip(X_train, y_train):
                # 1. Encontra o neurônio vencedor (BMU)
                bmu_idx = self.find_bmu(x)
                y_predito = self.classes_w[bmu_idx]
                
                # 2. Atualização Supervisionada dos Pesos (Regra LVQ-1)
                if y_predito == y_real:
                    # Classificação Correta: Aproxima o peso da amostra (Reforço Positivo)
                    self.W[bmu_idx] += self.alpha * (x - self.W[bmu_idx])
                else:
                    # Classificação Incorreta: Afasta o peso da amostra (Punição)
                    self.W[bmu_idx] -= self.alpha * (x - self.W[bmu_idx])
                    
        return self.W

    def predict(self, X_test):
        """
        Realiza a classificação de novas amostras (inferência).
        """
        X_test = np.array(X_test, dtype=float)
        previsoes = []
        
        for x in X_test:
            bmu_idx = self.find_bmu(x)
            previsoes.append(self.classes_w[bmu_idx])
            
        return previsoes