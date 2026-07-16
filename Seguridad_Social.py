salario_base = float(input("Ingrese el valor del salario base: "))

aporte_salud = salario_base * 0.04
print("El aporte de salud es:", aporte_salud)

aporte_pension = salario_base * 0.04
print("El aporte de pensión es:", aporte_pension)

descuento = aporte_salud + aporte_pension
print("El descuento es:", descuento)

salario_neto = salario_base - descuento
print("El salario neto es:", salario_neto)