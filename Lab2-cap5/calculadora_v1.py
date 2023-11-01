# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************\n")
print("Selecione o número da opção desejada\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão\n")
operacao = input("Digite sua operação (1/2/3/4): " )
while operacao not in ("1", "2", "3", "4"):
    print("Opção inválida!")
    operacao = input("Digite sua operação (1/2/3/4): " )

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if operacao == "1":
    resultado = n1 + n2
    operacao = "+"
elif operacao == "2":
    resultado = n1 - n2
    operacao = "-"
elif operacao == "3":
    resultado = n1 * n2
    operacao = "*"
elif operacao == "4":
    if n2 != 0:
        resultado = n1 / n2
        operacao = "/"
    else:
        print("Impossível divisão por zero")
        exit(0)
print(f"{n1} {operacao} {n2} = {resultado}")
        





