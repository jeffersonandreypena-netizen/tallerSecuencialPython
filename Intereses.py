cantidad = float(input("Ingrese el valor invertido: "))
periodo = float(input("Ingrese el tiempo dado invertido: "))
porcentajeint = float(input("Ingrese el porcentaje de interes invertido: "))

valorinteres = (cantidad * (porcentajeint / 100) * periodo) / 360
impuesto = valorinteres * 0.07
total = cantidad + valorinteres - impuesto

print("El recibido es del interes es", total)
print("El impuesto es", impuesto)
print("El valor del interes es", valorinteres)
