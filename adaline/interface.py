import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
from adaline import Adaline

class AdalineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Válvulas ADALINE - CEFET")
        self.root.geometry("450x520")
        
        self.modelo = None
        
        # Título Principal
        tk.Label(root, text="Classificador de Sinais (Válvula A/B)", font=("Arial", 14, "bold")).pack(pady=10)
        
        # --- Secção de Treino ---
        frame_treino = tk.LabelFrame(root, text=" Configuração do Treinamento (Regra Delta) ")
        frame_treino.pack(padx=15, pady=10, fill="x")
        
        # Taxa de Aprendizado
        tk.Label(frame_treino, text="Taxa de Aprendizado (η):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_eta = tk.Entry(frame_treino)
        self.entry_eta.insert(0, "0.0025") # Valor do enunciado
        self.entry_eta.grid(row=0, column=1, padx=5, pady=5)
        
        # Precisão
        tk.Label(frame_treino, text="Precisão (epsilon):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_eps = tk.Entry(frame_treino)
        self.entry_eps.insert(0, "0.000001") # 10^-6
        self.entry_eps.grid(row=1, column=1, padx=5, pady=5)
        
        self.btn_treinar = tk.Button(frame_treino, text="Treinar Rede ADALINE", command=self.treinar, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        self.btn_treinar.grid(row=2, column=0, columnspan=2, pady=10)

        # --- Secção de Teste de Sinal ---
        self.frame_teste = tk.LabelFrame(root, text=" Entrada de Sinal Ruidoso {x1, x2, x3, x4} ")
        self.frame_teste.pack(padx=15, pady=10, fill="x")
        
        labels = ["Grandeza x1:", "Grandeza x2:", "Grandeza x3:", "Grandeza x4:"]
        self.entries = []
        for i, label in enumerate(labels):
            tk.Label(self.frame_teste, text=label).grid(row=i, column=0, padx=5, pady=3, sticky="e")
            entry = tk.Entry(self.frame_teste)
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.entries.append(entry)
            
        self.btn_classificar = tk.Button(self.frame_teste, text="Identificar Válvula de Destino", command=self.classificar, state="disabled", font=("Arial", 10, "bold"))
        self.btn_classificar.grid(row=len(labels), column=0, columnspan=2, pady=15)

    def treinar(self):
        try:
            # Carregar dados do anexo
            df = pd.read_csv('treinamento.csv')
            X = df[['x1', 'x2', 'x3', 'x4']].values
            d = df['d'].values
            
            eta = float(self.entry_eta.get())
            eps = float(self.entry_eps.get())
            
            self.modelo = Adaline(n_inputs=4, learning_rate=eta, precision=eps)
            weights, epocas, mse_history = self.modelo.train(X, d)
            
            messagebox.showinfo("Treino Concluído", f"Rede ADALINE treinada com sucesso!\nÉpocas: {epocas}\nEQM Final: {mse_history[-1]:.8f}")
            self.btn_classificar.config(state="normal")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar treinamento: {e}")

    def classificar(self):
        try:
            entradas = [float(e.get()) for e in self.entries]
            resultado = self.modelo.predict(entradas)
            
            # Convenção: -1 para Válvula A, +1 para Válvula B
            if resultado == -1:
                classe = "VÁLVULA A"
                cor = "#FF5722" # Laranja/Vermelho
            else:
                classe = "VÁLVULA B"
                cor = "#4CAF50" # Verde
                
            messagebox.showinfo("Decisão do Comutador", f"Encaminhar sinal para:\n\n{classe}")
        except ValueError:
            messagebox.showwarning("Atenção", "Insira valores numéricos válidos para as grandezas.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdalineApp(root)
    root.mainloop()