# def minha_funcao(valor1,valor2):
#     return valor1+valor2


# while True:
#     valor1=int(input("Valor 1: "))
#     valor2=int(input("Valor 2: "))
#     resposta =minha_funcao(valor1,valor2)
#     print(valor1,"+",valor2,"=",resposta)
    
    
# codigo sem funcao 

# fluxo_caixa=[]

# print("--------------------")
# print("Controle de fluxo de caixa")
# print("---------------------")
# print("1-adicionar receita ")
# print("2-adicionar despesa")
# print("\n# digite outro número para encerrar #\n")


# while True:
#     opcao= int(input("digite a opcao:"))
    
#     if opcao ==1:
#         nome=input("Nome da receita: ")
#         valor=float(input("Valor da receita: "))
#         fluxo_caixa.append({
#             "nome": nome,
#             "valor": valor,
#         })
#     elif opcao ==2:
#         nome=input("Nome da despesa: ")
#         valor=float(input("Valor da despesa: "))
#         fluxo_caixa.append({
#             "nome": nome,
#             "valor": valor,
#         })
#     else:
#         break
    
#     # nota fiscal
#     total=0
#     for fc in fluxo_caixa:
#        print("Nome:",fc['nome'],", valor:",fc['valor'])
#     total=total+fc['valor'] 
    
#     print("Saldo Atual R$:",total)



fluxo_caixa = []

print("--------------------")
print("Controle de fluxo de caixa")
print("---------------------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro número para encerrar #\n")

def adicionar_transacao(tipo):
    nome = input(f"Nome da {tipo}: ")
    valor = float(input(f"Valor da {tipo}: "))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor,
        "tipo": tipo
    })

while True:
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        adicionar_transacao("receita")
    elif opcao == 2:
        adicionar_transacao("despesa")
    else:
        break

    # Relatório
    total_receitas = 0
    total_despesas = 0

    print("\n--- Histórico de transações ---")
    for fc in fluxo_caixa:
        print(f"Tipo: {fc['tipo']} - Nome: {fc['nome']} - Valor: R$ {fc['valor']:.2f}")
        if fc['tipo'] == 'receita':
            total_receitas += fc['valor']
        elif fc['tipo'] == 'despesa':
            total_despesas += fc['valor']

    saldo = total_receitas - total_despesas

    print("\nTotal de Receitas: R$ {:.2f}".format(total_receitas))
    print("Total de Despesas: R$ {:.2f}".format(total_despesas))
    print("Saldo Final: R$ {:.2f}\n".format(saldo))

