# Roadmap do Projeto: Perceptron para Classificação de Óleo

Este documento descreve as fases de desenvolvimento para a implementação do classificador de pureza de petróleo utilizando a Regra de Hebb.

---

## ✅ Fase 1: Planejamento e Estruturação
- [x] Criação da estrutura de pastas do projeto (`.agent`, `.planning`, `perceptron`).
- [x] Definição detalhada dos requisitos em `REQUIREMENTS.md`.
- [x] Elaboração do cronograma de desenvolvimento (`ROADMAP.md`).

## 📅 Fase 2: Preparação de Dados
- [ ] Extração dos 30 padrões de treinamento do anexo.
- [ ] Criação do arquivo `perceptron/treinamento.csv`.
- [ ] Verificação da integridade dos dados (valores de $x_1, x_2, x_3$ e $d$).

## 📅 Fase 3: Implementação do Algoritmo (Core)
- [ ] Desenvolvimento da classe `Perceptron` em `perceptron/perceptron.py`.
- [ ] Implementação da **Regra de Hebb** para ajuste de pesos.
- [ ] Configuração do Bias fixo ($x_0 = -1$) e Taxa de Aprendizado ($\eta = 0.01$).

## 📅 Fase 4: Execução e Análise de Resultados
- [ ] Criação do script `perceptron/solve_assignment.py` para os 5 treinamentos.
- [ ] Implementação da lógica de pesos iniciais aleatórios entre 0 e 1.
- [ ] Geração do gráfico de convergência (`evolucao_erros.png`).
- [ ] Teste do modelo com as 10 amostras de classificação automática.

## 📅 Fase 5: Interface Gráfica e Documentação Final
- [ ] (Opcional) Implementação da interface em Tkinter em `perceptron/interface.py`.
- [ ] Preenchimento das tabelas de resultados e respostas teóricas.
- [ ] Finalização do `respostas_trabalho.md` para entrega.

---
**Status Atual:** 🕒 Iniciando Fase 2.