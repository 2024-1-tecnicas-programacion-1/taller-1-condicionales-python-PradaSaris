def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    residuo = dividendo % divisor
    cociente = int(dividendo/divisor)
    exactitud = ""
    if residuo == 0:
        exactitud = "es exacta."
    else:
         exactitud = "no es exacta."
    respuesta = "La división " + exactitud + " \n" \
        "Cociente: " + str(cociente) + "\n" \
        "Residuo: " + str(residuo)
    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
