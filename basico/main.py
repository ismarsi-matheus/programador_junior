# print("Quero meu primeiro emprego")
# # print serve para imprimir no terminal

# print("oi")
# print(1+1)
# print(10/2)


# # boolean
# is_python = True
# is_java = False

# #armazenamento condições 

# ingressos=50
# compradores=250
# tem_ingressos_suficientes=(ingressos>=compradores)
# print(tem_ingressos_suficientes)


# nome = "Matheus"
# idade = 18
# peso=88.8

# print(nome)
# print(idade)
# print(peso)


# nome =input("Qual o seu nome?: ")
# idade = int(input("Qual a sua idade?: "))
# peso = float(input("Qual o seu peso?: "))

# print(nome)
# print(type(idade))
# print(type(peso))

# Operadores aritméticos

# soma=10+5
# multiplicacao=10*5
# subtracao=10-5
# divisao=10/5


# print("soma",soma)
# print("multiplcação",multiplicacao)
# print("subtração",subtracao)
# print("divisão",divisao)


# valor1= 10
# valor2=5

# if valor1>valor2:
#     print("Valor 1 é maior que valor 2")
# else:
#     print("Valor 2 é maior que valor 1")


# IDADE = int(input("Qual a sua idade?: "))
# if IDADE >= 18:
#     print("PERMITIDO")
# else:
#     print("BLOQUEADO")


# salario=float(input("Qual o seu salário?: "))


# if salario <= 3000:
#     print("programador junior")
# elif salario > 3000 and salario <= 6000:
#     print("programador pleno")
# elif salario > 6000:
#     print("programador sênior")
# else:
#     print("gerente de projetos")
    
# elif=else if

# lista_numeros=[1,2,3,4,5,6,7,8,9,10]
# lista_numeros[0]=5


# print(lista_numeros[0])
# print(lista_numeros[1])
# print(lista_numeros[2])

# numeros=[1,2,3,]
# strings=["João","Maria","José"]
# decimais=[10.8,15.2,33.3]


# lista_vazia=[]

# lista_vazia.append('olá')
# lista_vazia.append('Mundo')

# print(lista_vazia)
# # append adiciona um elemento na lista

# numeros=[1,2,3,4,5]

# print("total:",len(numeros))
# # len conta o número de elementos na lista
# print("menor valor:",min(numeros))
# # min retorna o menor valor da lista
# print("maior valor:",max(numeros))
# # max retorna o maior valor da lista


# REPETIÇÕES

# for :loop que percorre sequências,repetindo um bloco de código para cada elemento da sequência

# while:loop que repete um bloco de código enquanto uma condição for verdadeira

nota=[]

# codigo_aluno=input("RM:")
# nota=float(input("Nota:"))
# resultado=input[codigo_aluno,nota]
# nota.append(resultado)

# for x in range(300):
#     codigo_aluno=input("RM:")
#     nota=float(input("Nota:"))
#     resultado=[codigo_aluno,nota]
#     nota.append(resultado)


# # x:valor alterado para cada repetição ,pode ser usada apenas dentro do bloco de repetição
# # range(5)=[0,1,2,3,4],nesse caso ,possui 5 itens

# print("qunatidade de notas:",len(nota))

# for n in nota :
#     codigo_aluno=n[0]
#     nota=n[1]
#     print("0 RM",codigo_aluno,"tirou a nota",nota)
    
    
# notas=[
# 0=>[1234,10]    <=rm,nota
# 1=>[321,5.5]
# 2=>{444,6.0}
# ]

# while

# contador=1

# while contador<=5:
#     codigo_aluno=input("RM:")
#     nota=float(input("Nota:"))
#     resultado=[codigo_aluno,nota]
#     nota.append(resultado)
    
#     # alternativa:conatdor+=1
#     contador=contador+1
    
#     print ("quantidade de notas",len(nota))


pessoa={
    "nome":"Matheus",
    "idade":18,
    "peso":88.8
}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["peso"])
# dicionário:estrutura de dados que armazena pares de chave-valor

# informações do jogador 

player={
    "nome":"Matheus",
    "level":1,
    "hp":100,
    "exp":0,
    "dano":5,
}

# lista de inimigos

npcs=[
    {"nome":"monstrinho","dano":2,"hp":50,"exp":5},
    {"nome":"monstro","dano":5,"hp":100,"exp":10},
    {"nome":"monstrão","dano":10,"hp":150,"exp":15},
    {"nome":"Chefão","dano":25,"hp":200,"exp":20},
]

# dicionario:estrutura de dados que armazena pares de chave-valor

# lista:estrutura de dados que armazena uma sequência de valores

