def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    imc = peso/(estatura**2)
    riesgo = ""
    if edad<45:
        if imc<22.0:
            riesgo = "bajo"
        else:
            riesgo = "medio"
    elif edad>45:
        if imc<22.0:
            riesgo = "medio"
        else:
            riesgo = "alto"
    return(riesgo)

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
