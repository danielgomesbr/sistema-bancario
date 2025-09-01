while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    print(numero)
print()

for numero in range(100):
    if numero == 12:
        break  # Para no número 11
    print(numero, end=" ")
print()

for numero in range(100):
    if numero == 12:
        continue  # Não exibe o número 12
    print(numero, end=" ")
print()

for numero in range(100):
    if numero % 2 == 0:
        continue  # Mostra os números ímpares
    print(numero, end=" ")
print()

while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10:
        break  # Chegando a 10 para

    if numero % 2 == 0:
        continue  # Número ímpares exibe, números pares não exibe
print(numero)