import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import pandas as pd
from perceptron import Perceptron

class PerceptronApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Classificador de Óleo - CEFET Varginha")
        self.root.geometry("400x480")
        
        self.modelo = None
        
        # Título
        tk.Label(root, text="Classificação de Pureza de Óleo", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Frame de Treinamento
        frame_treino = tk.LabelFrame(root, text=" Treinamento ")
        frame_treino.pack(padx=10, pady=10, fill="x")
        
        tk.Label(frame_treino, text="Taxa de Aprendizado (η):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_eta = tk.Entry(frame_treino)
        self.entry_eta.insert(0, "0.01")
        self.entry_eta.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_treinar = tk.Button(frame_treino, text="Treinar Rede", command=self.treinar, bg="#4CAF50", fg="white")
        self.btn_treinar.grid(row=1, column=0, columnspan=2, pady=10)

        # Frame de Teste (Onde estava o erro)
        self.frame_teste = tk.LabelFrame(root, text=" Testar Amostra ")
        self.frame_teste.pack(padx=10, pady=10, fill="x")
        
        labels = ["x1:", "x2:", "x3:"]
        self.entries = []
        for i, label in enumerate(labels):
            tk.Label(self.frame_teste, text=label).grid(row=i, column=0, padx=5, pady=2)
            entry = tk.Entry(self.frame_teste)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entries.append(entry)
            
        # CORREÇÃO: Usando grid em vez de pack para evitar o TclError
        self.btn_classificar = tk.Button(self.frame_teste, text="Classificar Óleo", command=self.classificar, state="disabled")
        self.btn_classificar.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def treinar(self):
        try:
            # Carrega os dados do CSV na pasta perceptron
            df = pd.read_csv('treinamento.csv')
            X = df[['x1', 'x2', 'x3']].values
            d = df['d'].values
            
            eta = float(self.entry_eta.get())
            self.modelo = Perceptron(n_inputs=3, learning_rate=eta)
            weights, epocas = self.modelo.train(X, d)
            
            messagebox.showinfo("Sucesso", f"Rede treinada!\nConvergência em {epocas} épocas.")
            self.btn_classificar.config(state="normal")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar treinamento.csv: {e}")

    def classificar(self):
        try:
            entradas = [float(e.get()) for e in self.entries]
            resultado = self.modelo.predict(entradas)
            classe = "C2 (Pureza Alta)" if resultado == 1.0 else "C1 (Pureza Baixa)"
            messagebox.showinfo("Resultado", f"O óleo foi classificado como:\n{classe}")
        except Exception as e:
            messagebox.showwarning("Atenção", "Insira valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PerceptronApp(root)
    root.mainloop()