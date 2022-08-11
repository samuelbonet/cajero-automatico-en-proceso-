
from pickletools import OpcodeInfo


saldo=1000

print("MENU")
print("1")
print("2")
print("3")
print("4")

opcion=int(input("Digite"))

print()
if opcion == 1:
    extra = float(input('Cunto dinero ingresar'))
    saldo += extra
    print("Su saldo es de:", saldo)
   
elif opcion == 2:
    retirar = float(input("Cuanto desea retirar"))
    if retirar > saldo:
        print("No tiene esa cantidad")
    else:
        saldo -= retirar
        print("Dispone de {saldo}")
elif opcion == 3:
    print(f"Dinero en la cuenta {saldo}")
elif opcion == 4:
    print("Gracias por utilizarlo")

opcion()