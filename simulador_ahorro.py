"""
SIMULADOR DE AHORRO MENSUAL
Instrucciones:

1) Escribe una función llamada «calcular_ahorro» que reciba como parámetros:
• monto_mensual (cantidad ahorrada cada mes)
• meses (cantidad de meses. Por defecto, 12)
• La función debe retornar el total ahorrado
2) Escribe otra función llamada «mostrar_ahorro» que reciba el total ahorrado y lo imprima en pantalla (sin retorno)
3) Crea un programa que permita al usuario ingresar el monto mensual y opcionalmente los meses.
"""

# Función para calcular el ahorro
def calcular_ahorro(monto_mensual, meses = 12):
    ahorro = monto_mensual * meses
    return ahorro

# Función para mostrar el ahorro total
def mostrar_ahorro(total_ahorrado):
    print(f"El monto total ahorrado es de ${total_ahorrado}.")


print("SIMULADOR DE AHORRO MENSUAL:")

# Ingreso de datos
while True:
    try:
        ingresar_monto = int(input("Ingrese el monto mensual ahorrado: $"))
        break
    except ValueError:
        print("¡Error! El dato ingresado no es válido. Solo se aceptan números. Intente nuevamente.")

cantidad_meses = input("Ingrese la cantidad de meses (En el caso de elegir 12 meses, solo presionar Enter): ")

if cantidad_meses == "":
    meses = 12
else:
    meses = int(cantidad_meses)

# Llamando a la función calcular_ahorro() con los datos ingresados en «ingresar_monto» y «meses» como parámetros
total_ahorrado = calcular_ahorro(ingresar_monto, meses)

# Se muestra por consola el valor que retorna de la función calcular_ahorro() como valor del argumento «total_ahorrado»
mostrar_ahorro(total_ahorrado)

print('Gracias por utilizar "Simulador de ahorro mensual". ¡Adiós!')