def evaluar(num_victorias_a, num_victorias_b):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    resultado = ""
    if(num_victorias_a >=6 or num_victorias_b >= 6) and (num_victorias_a > num_victorias_b+1 or num_victorias_b > num_victorias_a+1):
        if (num_victorias_a+2 < num_victorias_b or num_victorias_b+2 < num_victorias_a) or (num_victorias_a > 7 or num_victorias_b > 7):
            resultado = "Inválido"
        elif num_victorias_a > num_victorias_b:
            resultado = "Ganó A"
        else:
            resultado = "Ganó B"
    else:
        if num_victorias_a == 7 and num_victorias_b == 6:
            resultado = "Ganó A"
        elif num_victorias_a == 6 and num_victorias_b == 7:
            resultado = "Ganó B"
        else:
            resultado = "Aún no termina"
    return (resultado)

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
