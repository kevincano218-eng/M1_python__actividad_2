print ("Bienvenido a AhorroMax")
print ("----------------------- ")
producto = 2000

cant_prod = int (input ("Digita la cantidad de productos a llevar: "))
c_valid= "si"

while c_valid == "si":

    if (cant_prod < 0):
        print ("ERROR. Digita valores validos positivos.")
        break
    elif cant_prod >= 30:
        descuento = 0.15
        total = cant_prod * producto * (1 - descuento)
        print (f"El precio neto a pagar es {total}")
    elif cant_prod >= 10:
        descuento = 0.10
        total = cant_prod * producto * (1 - descuento)
        print (f"El precio neto a pagar es {total}")
        if (total < 50000):
            envio = 5000
            total_envio = total + envio
            print (f"Tu compra al ser inferior a $50.000 se te cobrará envio por lo que el total a pagar es {total_envio}")
            c_valid = input("Deseas digitar informacion nueva (si-no): ").lower()
    
