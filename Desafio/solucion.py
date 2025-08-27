import re

texto = "En el sistema de monitoreo climático registramos varios datos importantes por ejemplo la temperatura actual puede ser un número flotante como 23.7 grados mientras que la temperatura mínima registrada hoy fue un número entero negativo -5 grados el sensor de humedad reporta un valor de 56.3% que también es un flotante para saber si la estación meteorológica está activa usamos un booleano si está funcionando el valor es True y si no es False actualmente el estado es True los nombres de las estaciones se almacenan como strings por ejemplo \"Estación Norte\", \"Estación Sur\" y \"Estación Central\" además tenemos listas con datos históricos de temperaturas diarias como [12, 15, 20, -3, 0, 8] donde los números son enteros positivos y negativos también hay listas de temperaturas promedio diarias en flotantes por ejemplo [14.5, 16.2, 19.8, 0.0, -1.5, 7.3] con estos datos podemos analizar las tendencias climáticas y preparar alertas para cambios bruscos de temperatura"
patron1 = r"(?<!\d\.)-?\b\d+\b(?!\.\d)"
patron2 = r"-?\b\d+\.\d+\b"
patron3 = r"\b(True|False)\b"
patron4 = r'"(.*?)"'
patron5 = r"\[[^\]]+\]"

enteros = re.findall(patron1, texto)
flotantes = re.findall(patron2, texto)
booleans = re.findall(patron3, texto)
strings = re.findall(patron4, texto)
listas = re.findall(patron5, texto)

print()
print("El texto de entrada es: ", texto)
print()
print("Resultados: ")
print("Numeros enteros: " + str(enteros) + "\nNumeros flotantes: " + str(flotantes) + "\nBooleanos: " + str(booleans) + "\nStrings: " + str(strings) + "\nListas: " + str(listas))
print()
print("Cantidad de enteros: ",len(enteros), "\nCantidad de flotantes: ",len(flotantes), "\nCantidad de booleanos: ",len(booleans), "\nCantidad de Strings: ",len(strings), "\nCantidad de listas: ",len(listas))
print()
print("Este fue un ejemplo de lo que hace, ahora ingresa tu texto.")
texto2= input("Texto 2: ")

enteros = re.findall(patron1, texto2)
flotantes = re.findall(patron2, texto2)
booleans = re.findall(patron3, texto2)
strings = re.findall(patron4, texto2)
listas = re.findall(patron5, texto2)

print("Numeros enteros: " + str(enteros) + "\nNumeros flotantes: " + str(flotantes) + "\nBooleanos: " + str(booleans) + "\nStrings: " + str(strings) + "\nListas: " + str(listas))
print()
print("Cantidad de enteros: ",len(enteros), "\nCantidad de flotantes: ",len(flotantes), "\nCantidad de booleanos: ",len(booleans), "\nCantidad de Strings: ",len(strings), "\nCantidad de listas: ",len(listas))
