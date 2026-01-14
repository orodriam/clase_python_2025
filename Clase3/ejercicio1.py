# suscrito = input("Esta suscripto?").strip().lower()

# if suscrito != "si":
#     print("No estás suscrito")
#     print("Te invitamos a obtener")
# elif suscrito == "no":
#     print("Gracias por tu suscripcion")
# else:
#     print("Respuesta no válida")

########################################

# nombreEstudiante = input("Ingrese su nombre: ").strip().lower()
# notaEstudiante = float(input("Ingrese su nota: "))

# if notaEstudiante >= 90 and notaEstudiante <= 100:
#     print(f"Felicidades {nombreEstudiante}, tu nota es Excelente")
# elif notaEstudiante >= 80 and notaEstudiante < 90:
#     print(f"Felicidades {nombreEstudiante}, tu nota es muy bien")
# elif notaEstudiante >= 70 and notaEstudiante < 80:
#     print(f"Felicidades {nombreEstudiante}, tu nota es bien")
# elif notaEstudiante >= 60 and notaEstudiante < 70:
#     print(f"{nombreEstudiante}, tu nota es regular")
# elif notaEstudiante < 60 and notaEstudiante >= 0:
#     print(f"{nombreEstudiante}, reprobaste el curso")
# else:
#     print("Nota no válida")


########################################

EXCELENTE = "excelente!"
MUY_BIEN = "muy bien"
BIEN = "bien"
REGULAR = "regular"
REPRUEBA = "reprueba"

nombre = input("Ingresa el nombre del estudiante: ")
nota = int(input ("Ingresa tu nota (0-100) :. ") )

# Validación del rango
if nota < 0 or nota > 100:
    print("Error: la nota debe estar entre 0 y 100")
else:
    if nota >= 90:
        resultado = EXCELENTE
    elif nota >= 80:
        resultado = MUY_BIEN
    elif nota >= 70:
        resultado = BIEN
    elif nota >= 60:
        resultado = REGULAR
    else:
        resultado = REPRUEBA

print(f"{nombre} tiene una nota de {nota} y es {resultado}")