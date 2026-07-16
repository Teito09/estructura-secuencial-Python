quiz = float(input("Ingrese la nota del quiz: "))
taller = float(input("Ingrese la nota del taller: "))
parcial = float(input("Ingrese la nota del parcial: "))

definitiva = (quiz + taller + parcial) / 3

print("La definitiva del estudiante es:", definitiva)