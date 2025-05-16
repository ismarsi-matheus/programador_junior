import os
# usada para interagir com o sistema operacional

mensagens = []

nome = input("Nome: ")

while True:
    # limpamdo terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

# se alista for maior que 0, imprime as mensagens

    print("----------------------")

    # obtendo o texto

    texto = input("Digite sua mensagem: ")
    if texto == "fim":
        break
    # adicionando a mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
