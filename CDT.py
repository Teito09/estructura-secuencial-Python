valor_presente = float(input("Ingrese el valor inicial: "))
dias = float(input("Ingrese el número de días: "))

tasa_de_interes = (1 + 0.115) ** (dias / 360) - 1
print("La tasa de interés es:", tasa_de_interes)

intereses_brutos = valor_presente * tasa_de_interes
print("Los intereses brutos son:", intereses_brutos)

impuesto = intereses_brutos * 0.04
print("El impuesto es:", impuesto)

intereses_neto = intereses_brutos - impuesto
print("Los intereses netos son:", intereses_neto)

valor_final = valor_presente + intereses_neto
print("El valor final es:", valor_final)