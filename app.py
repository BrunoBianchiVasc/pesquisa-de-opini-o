"""
Pesquisa de Opinião - TudoWeb

Programa que coleta nome, idade e opinião de clientes sobre o atendimento
e exibe ao final quantas respostas foram "EXCELENTE" e quantas foram "RUIM".
"""

# Quantidade de entrevistados na pesquisa
NUM_ENTREVISTADOS = 50

# Contadores que guardam quantas respostas de cada tipo foram dadas
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

# Estrutura de repetição: um loop para cada entrevistado da pesquisa
for pessoa in range(1, NUM_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {pessoa} de {NUM_ENTREVISTADOS} ---")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    opiniao = input("Opinião sobre o atendimento (1-Excelente, 2-Bom, 3-Ruim): ")

    # Estrutura de decisão: verifica qual foi a opinião digitada e contabiliza
    match opiniao:
        case "1":
            print(f"{nome}, resposta registrada: EXCELENTE")
            qtd_excelente += 1
        case "2":
            print(f"{nome}, resposta registrada: BOM")
            qtd_bom += 1
        case "3":
            print(f"{nome}, resposta registrada: RUIM")
            qtd_ruim += 1
        case _:
            # Caso o entrevistado digite algo fora de 1, 2 ou 3
            print(f"{nome}, opção inválida, resposta não contabilizada.")

# Resultado final exibido ao término da pesquisa
print("\n=== Resultado da Pesquisa de Satisfação ===")
print(f"Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"Quantidade de respostas RUIM: {qtd_ruim}")