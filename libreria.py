libro = 25000
cupon = 0.10

print("--------------------------------")
print ("Bienvenido a libreria El Saber")
print("--------------------------------")
print ("El valor del libro tiene un costo de $25000")


c_valid= "si"

while c_valid == "si":

    estudiante = input ("Eres estudiante? si/no: ").lower()
    if estudiante == "si":
        estudiante = 0.15
        of_cupon = input ("¿Tienes un cupon de descuento aplicable? si/no: ").lower()
        if of_cupon == "si":
            libro10 = input ("Digita el cupon para validar el descuento: ")
            if libro10 == "LIBRO10":
                print (f"Se te aplicará el 10% y por ser estudiante se te aplicará el 15% y te queda en {libro * (1 - cupon) * (1 - estudiante)}")
                c_valid = input("Deseas digitar informacion nueva (si-no): ").lower()
            else:
                print (f"Cupon no disponible. Solo se aplicará el descuento de estudiante. El total a pagar es {libro * (1 - estudiante)}")
                c_valid = input("Deseas digitar informacion nueva (si-no): ").lower()
        else:
            print (f"No se aplicara cupon de descuento pero si se te aplicará el descuento de estudiante del 15% que es: {libro * (1 - estudiante)}")
            c_valid = input("Deseas digitar informacion nueva (si-no): ").lower()
    else:
        print (f"Al no ser estudiante el cupón y descuento no aplican y te cuesta el libro en su precio estandar: ${libro}")
        c_valid = input("Deseas digitar informacion nueva (si-no): ").lower()