import math

g = int(input("Digite o grau da sua equação: "))
print(" ")

if g == 1:
    print("A equação é do primeiro grau")
    print(" ")
    a = float(input("Digite o valor de A: "))
    print(" ")
    if a == 0:
        print("Valor de a inválido")
    else:
        b = float(input("Digite o valor de B: "))
        print(" ")
        r = - b / a
        print(f"A raiz da equação '{a}X + {b} = 0' é {r:.2f}")
        

elif (g == 2):
    print("A equação é do segundo grau")
    a = float(input("Digite o valor de A: "))
    if a == 0:
        print("Valor de a inválido")
    else:    
        b = float(input("Digite o valor de B: "))
        c = float(input("Digite o valor de C: "))

        if ((b ** 2) - (4 * a * c)) < 0:
            print("A equação não possui raízes reais")
        
        elif ((b ** 2) - (4 * a * c)) == 0:
            r = (-b + (math.sqrt((b**2) - (4 * a * c)))) / 2 * a
            print(f"A equação possui apenas uma raiz real, {r:.2f}")
        
        elif ((b ** 2) - (4 * a * c)) > 0:
            r1 = (-b + (math.sqrt((b**2) - (4 * a * c)))) / 2 * a
            r2 = (-b + (math.sqrt((b**2) - (4 * a * c)))) / 2 * a
            print(f"A equação possui duas raízes reais, {r1:.2f}, {r2:.2f}")

    
else:
    print("Grau inválido")
