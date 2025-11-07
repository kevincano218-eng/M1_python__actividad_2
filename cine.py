print ("Bienvenido a cine La Estrella")
print ("--------------------")

ingresar = "si"
while ingresar == "si":
    edad = int (input("Digite la edad de la persona: "))
    if edad < 0:
        print ("ERROR")
        ingresar = input ("Deseas seguir ingresando datos: (si-no): ").lower()
    elif (edad >= 12 and edad <= 59):
        entrada = 8000
        print (f"La entrada te va a costar ${entrada}")
        ingresar = input ("¿Quieres ingresar informacion diferente (si-no)?: ").lower()
    elif edad >= 5 and edad <= 11:
        entrada = 5000
        print (f"El valor de la entrada va a ser de ${entrada}")
        ingresar = input ("¿Quieres ingresar informacion diferente (si-no)?: ").lower()
    elif edad >= 60:
        entrada = 4000
        print (f"El valor de la entrada es de ${entrada}")
        ingresar = input ("¿Quieres ingresar informacion diferente (si-no)?: ").lower()
    elif edad < 5:
        entrada = 0
        print (f"El valor de la entrada es de ${entrada}")
        ingresar = input ("Deseas seguir ingresando datos: (si-no): ").lower()

