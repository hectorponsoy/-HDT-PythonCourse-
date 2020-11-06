numIntentos = int(input("Digite la cantidad de intentos que desea realizar: "))
def play(intento=1):
    respuesta = input("\nDigite el color de la fruta: ")
    palabra = "naranja"
    if respuesta != palabra:
        
        if intento < numIntentos:
            print("Respuesta incorrecta, intentalo de nuevo")
            intento = intento + 1
            hacer = play(intento)
        else:
            print("\n-------------Usted ha perdido-------------")
    else:
        print("\n************Usted ha ganado************")
play()