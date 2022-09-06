import sys
print('Parametros: Los valores deben de cumplir: Xo ≥ 0 || A ≥ 0 || C ≥ 0 || M ≥ Xo, A')
try:
    semilla = int(input('Ingrese el valor de Xo: '))
    a = int(input('Ingrese el valor de A: '))
    c = int(input('Ingrese el valor de C: '))
    m = int(input('Ingrese el valor de M: '))

    if semilla >= 0 and a >= 0 and c >= 0 and m > semilla and m > a:
        pruebas = int(input('Ingrese las pruebas a generar: '))

        for x in range(pruebas):
            semilla = semilla 
            a = a
            c = c
            m = m
            subtotal = semilla * a + c 
            pseudoaleatorio = subtotal % m
            random =pseudoaleatorio / (m-1)
            print(f'[{x}] Xo: {semilla}, A= {a}, C: {c}, M: {m}, Subtotal: {subtotal}, Pseudoaleatorio: {pseudoaleatorio}, Random: {random}')
            semilla = pseudoaleatorio

            if pseudoaleatorio == 0:
                print('Límite del Método.')
                break
        print('Programa finalizado.')
    else:
        print('Debe de proporcionar valores mayores a cero, o que cumplan con los parametros.')

except (ValueError):
    print('Tienes un error de tipo: ', sys.exc_info()[0]) # sys.exc_info() Muestra el tipo de error
    print('Nota: Debes introducir valores de tipo numerico.')