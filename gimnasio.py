print ("Bienvenido al gimnasio Solo Leveling Fit")

puntos = 0
otra_o = "si"
while otra_o == "si":

    cant_dias = int(input("Digite los dias entrenados esta semana: "))
    if (cant_dias >= 4):
        puntos += 1
        print (f"¡Excelente disciplina! Ganaste un punto\nTus puntos son {puntos}")
        otra_o = input ("¿Deseas digitar otros datos?").lower()
    elif cant_dias >= 2:
        print("Bien, pero puedes dar más.\nPor ahora no tienes puntos semanales.")
        otra_o = input ("¿Deseas digitar otros datos?").lower()
    elif (puntos >= 0 and puntos <= 1):
        puntos = 0
        print (f"No aflojes, tu puedes mejorar.\nTus puntos son {puntos}")
        otra_o = input ("¿Deseas digitar otros datos?").lower()