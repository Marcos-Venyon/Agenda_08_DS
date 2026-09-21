
# Inicialização dos contadores
qtd_excelente = 0
qtd_ruim = 0

print("=== Pesquisa de Satisfação - TudoWeb ===\n")

# Estrutura de repetição para 50 entrevistados
for i in range(1, 51):
    print(f"--- Entrevistado {i} de 50 ---")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = input("Escolha uma opção (1, 2 ou 3): ")

    # Estruturas de decisão para verificar a opinião
    if opiniao == "1":
        qtd_excelente = qtd_excelente + 1
    elif opiniao == "3":
        qtd_ruim = qtd_ruim + 1

    print()  # Linha em branco para separar as entradas

# Exibição do relatório final
print("========================================")
print("         RESULTADO DA PESQUISA          ")
print("========================================")
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print("========================================")