costo_pan = 300
print ("--------------------")
print ("Panaderia Don Pancho")
print ("--------------------")

c_valid= "si"

while c_valid == "si":

    cantidad = int (input ("ingrese la cantidad de panes que desea comprar: "))

    if (cantidad <= 0):
        print ("Cantidad invalida")
    else: 
        total = cantidad * costo_pan

        if (cantidad > 50):
            descuento = 0.20
            total_final = total * (1 - descuento)
            print(f"Al llevar mas de 50 panes tienes un descuento del 20% por lo que esto te queda en: ${total_final}")
        elif cantidad > 20:
            descuento = 0.10
            total_final = total * (1 - descuento)
            print(f"Al llevar mas de 20 panes tienes un descuento del 10% por lo que esto te queda en: ${total_final}")

        else: 
            descuento = 0
            total_final = total
            print(f"Al llevar menos panes no tienes descuento y esto te costaria en total: ${total_final}")


    

    
    

