salarioBase = float(input("Ingrese el salario base del empleado: "))

aporteSalud = salarioBase * 0.04
aportePension = salarioBase * 0.04
descuento = aporteSalud + aportePension
salarioNeto = salarioBase - descuento

print("El aporte de salud es de:", aporteSalud)
print("El aporte de pensión es de:", aportePension)
print("El descuento es de:", descuento)
print("El salario neto a pagar es:", salarioNeto)
