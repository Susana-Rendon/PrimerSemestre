"""monto_cantidad = float(input("ingrese la cantidad a invertir: "))
tasa_anual = float(input("ingrese la tasa anual: "))
tiempo_inversion = float(input("ingrese el tiempo de inversion: "))

interes_simple = monto_cantidad * tasa_anual/100 * tiempo_inversion
monto_total = monto_cantidad + interes_simple

print(f" el interes simple es: {interes_simple} y el monto total de inversion es {monto_total}")"""

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))

if edad>=18:
    print(f'la persona {nombre} tiene {edad} años y puede votar')
else:
    print('es menor')


