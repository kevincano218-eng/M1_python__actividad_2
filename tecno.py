print ("----------------------")
print ("Bienvenido a TecnoPlus")
print ("----------------------")
ingre_nota = "si"

while ingre_nota == "si":
    p_tecnica = float (input("Digita el resultado de la prueba tecnica (0.0-5.0): "))
    p_logica = float (input("Digita el resultado de la prueba logica (0.0-5.0): "))

    nota_final = (p_tecnica * 0.7) + (p_logica * 0.3)

    if (p_tecnica < 0 or p_logica > 5 or p_logica < 0 or p_tecnica > 5):
        print ("Error, las notas deben estar en el rango 0.0-5.0")
    else:
        nota_final = (p_tecnica * 0.7) + (p_logica * 0.3)
        if (nota_final >= 3):
            print ("Aprobado")
        elif nota_final >= 2 and nota_final < 3:
            print ("Revision")
        elif nota_final < 2:
            print ("Reprobado") 
        print (f"Tu nota final es: {nota_final}")

        ingre_nota =input("Deseas seguir ingresando notas si-no: ")


    




