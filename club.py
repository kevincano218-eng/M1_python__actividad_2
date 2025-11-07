print ("Bienvenido a Club Noche Estelar")
print ("--------------------------------")
opti = "si"

while opti == "si":

    while True:
                try:
                    edad = int (input ("Digita tu edad: "))
                    break
                except ValueError:
                    print("¡Error! Solo numeros, por favor")
    if (edad >= 18):
        documento = input ("¿Tienes tu documento a la mano (si-no)? ").lower()
        if ( documento == "si"):
            print ("Puedes pasar. ¡Bienvenido!")
            while True:
                opti = input ("Quieres ingresar otra información (si-no): ").lower()
                if (opti == "si" or opti == "no"):
                     break
                else: 
                     print ("Digita si o no por favor")
        else: 
            print ("Debes presentar el documento")
            while True:
                opti = input ("Quieres ingresar otra información (si-no): ").lower()
                if (opti == "si" or opti == "no"):
                     break
                else: 
                     print ("Digita si o no por favor")
    else:
        print ("¡Entrada denegada! Eres menor de edad")
        while True:
                opti = input ("Quieres ingresar otra información (si-no): ").lower()
                if (opti == "si" or opti == "no"):
                     break
                else: 
                     print ("Digita si o no por favor")