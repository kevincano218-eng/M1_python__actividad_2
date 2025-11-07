print("Bienvenido a Helados Frosty")
print("---------------------------")

chocolate = 4000
vainilla = 3500
topping = 1000

ot_sabor= "si"

while ot_sabor == "si":
    sabor = input ("Escriba el sabor que deseas hoy (chocolate/vainilla): ").lower()

    if (sabor == "chocolate"):
        precio = chocolate
    elif sabor == "vainilla":
        precio = vainilla
    else:
        print ("Sabor no disponible")
        precio = 0
        while True:
            ot_sab = input("Deseas escoger otras opciones (si-no)? ").lower()
            if (ot_sab == "si" or ot_sab == "no"):
                break
            else:
                print("Digitar solo SI o NO.")
 
    if (precio > 0):
        ag_topping = input("Deseas agregar topping por 1.000? si/no: ").lower()
        if ag_topping == "si":
            ag_topping = 1000
            print (f"Pagarás el producto y te adicionaremos el topping.\nTotal a pagar: ${precio + ag_topping}")
            ot_sabor = input("Deseas hacer otra seleccion?").lower
        else:
            print (f"Pagarás solo el producto sin topping.\n El total a pagar es: ${precio}")
            ot_sabor = input("Deseas hacer otra seleccion? ").lower
            