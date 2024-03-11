def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    caracter = ord(caracter)
    if caracter >= 48 and caracter <=57: 
        respuesta = "Es número"
    elif caracter >= 65 and caracter <= 90:
        respuesta = "Es letra mayúscula"
    elif caracter >= 97 and caracter <= 122:
        respuesta = "Es letra minúscula"
    else:
        respuesta = "No es letra ni número"
    return respuesta

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
