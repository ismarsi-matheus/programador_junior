# calclar imc

def calcular_imc(peso,altura):
    imc= peso/(altura **2)
    return imc
peso=float(input("Qual o seu peso?(Kg): "))
altura=float(input("Qual a sua altura?(m): "))

imc=calcular_imc(peso,altura)
print("Seu IMC é:",imc)