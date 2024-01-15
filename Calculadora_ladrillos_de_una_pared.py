''''
 Programa para el calculo de ladrillos en una pared
 Datos:
 Alto de una pared
 Largo de pared
 Alto del ladrillo a utilizar
 Largo del ladrillo a utilizar

 Constante de mezcla fija: A gusto del receptor
 '''
print ("Buenas estimado, este es un programa para el calculo de ladrillos en una pared, a continuación usted empezara a introducir datos para el calculo de su estructura.")
print ("Tenga en cuenta que la mezcla funciona como constante a ")
print ()
#Asigno el valor de la cantidad mezcla
ancho_mezcla = float(input("Ingrese la constante para la mezcla: ")) #Literal que queda escrito para siempre
# Comienza el ingreso de datos
print("Ingreso de datos, (Todas las medidas deben ser cargadas en centimetros)")
alto_pared = int(input("Ingrese el alto de la pared: "))
largo_pared = int(input("Ingrese el largo de la pared: "))
alto_ladrillo = float(input("Ingrese el alto del ladrillo: "))
largo_ladrillo = float(input("Ingrese el ancho del ladrillo: "))

#Fin de la carga de datos

#Inicio del proceso

Lad_x_fila = largo_pared/(largo_ladrillo + ancho_mezcla)
Cant_de_filas = alto_pared/(alto_ladrillo + ancho_mezcla)
Cant_de_lad = Lad_x_fila * Cant_de_filas

#Fin del Proceso

# Inicio del resultado

print ()
print ("Mono, la cantidad de ladrillos para construir una pared de",\
       largo_pared, "cm de largo por", alto_pared, "cm de alto es:", Cant_de_lad, "de ladrillitos.")
print (input())

print (170 * 11)
print (input())
