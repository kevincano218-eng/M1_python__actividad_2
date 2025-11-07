print ("---------------------")
print("Bienvenido a El Sabor Colombiano")
print ("---------------------")

menu = 12000
iva = 0.08
c_valid= "si"

while c_valid == "si":

    ad_bebidas = input ("Deseas una opcion de bebida? si/no: ").lower()

    if ad_bebidas == "si":
        bebidas = 3000
        subtotal = menu + bebidas
        total = subtotal * (1 + iva)
        print (f"El valor total por el menu, bebidas e iva incluido es de: ${int (total)}")
        c_valid = input("Deseas digitar informacion nueva (si-no): ").lower()

    else: 
        bebidas = 0
        subtotal = menu + bebidas
        total = subtotal * (1 + iva)
        print (f"El valor total por el menu, sin bebidas e iva incluido es de: ${int (total)}")
        c_valid = input("Deseas digitar informacion nueva (si-no): ").lower()

