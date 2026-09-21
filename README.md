# Pesquisa de Satisfação de Atendimento — TudoWeb

Este projeto consiste em um programa em Python desenvolvido para a empresa de marketing **TudoWeb**. O objetivo é realizar uma pesquisa de opinião com os clientes para avaliar o grau de satisfação com o atendimento prestado.

## 📌 Funcionalidades

- **Coleta de dados:** Solicita o nome, idade e a opinião de cada entrevistado sobre o atendimento.
- **Classificação da opinião:**
  - `1` — EXCELENTE
  - `2` — BOM
  - `3` — RUIM

- **Contagem e relatório:** Processa as respostas utilizando estruturas de repetição e decisão e exibe um relatório contendo:
  - Total de respostas **"EXCELENTE"**
  - Total de respostas **"RUIM"**

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Conceitos aplicados:**
  - Estruturas de repetição (`for` / `range`)
  - Estruturas de decisão (`if` / `elif`)
  - Entrada e saída de dados (`input` e `print`)
  - Interpolação de textos (*f-strings*)

## 🧪 Validação e Testes

O programa foi desenvolvido para atender uma amostra de **50 entrevistados** na versão final. 

Para fins de testes e validação rápida da lógica, foi criada uma versão que executa o ciclo com **10 entrevistados**, garantindo que as contagens de opções sejam incrementadas e exibidas corretamente ao final da execução.

---

## 📋 Exemplo de Execução

=== Pesquisa de Satisfação - TudoWeb ===

--- Entrevistado 1 de 50 ---
Digite o nome: Ana Silva
Digite a idade: 28
Opinião sobre o atendimento:
1 - EXCELENTE
2 - BOM
3 - RUIM
Escolha uma opção (1, 2 ou 3): 1

========================================
     RESULTADO DA PESQUISA DE OPINIÃO     
========================================
a) Quantidade de respostas 'EXCELENTE': 32
b) Quantidade de respostas 'RUIM': 5
========================================
```