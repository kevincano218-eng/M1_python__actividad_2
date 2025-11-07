print ("---------------------")
print ("Parqueadero RapidCar")
print ("---------------------")
hora = 2000

c_valid= "si"

while c_valid == "si":
    num_horas = int (input ("Digite el numero de horas que se usó el parqueadero: "))

    if (num_horas >= 5):
        cant_mul = hora * num_horas + 5000
        print (f"La cantidad de horas usadas fue de {num_horas}y el total a pagar es de {cant_mul} incluyendo la multa")
    else:
        print (f"El total a pagar es de ${hora * num_horas}")


    if (num_horas < 0):
        print ("No se permiten numero negativos")
        c_valid = input("Deseas digitar informacion nueva (si-no): ").lower()
