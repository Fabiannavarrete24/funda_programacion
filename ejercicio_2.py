#1.Crear un bucle que cuente todos los números pares hasta el 100 ciclo for
for n in range(1,101,1):
  print(n)

#2. Haz una tabla de multiplicar utilizando el ciclo for ciclo for

num_tab = int(input("¿que tabla de multiplicar desea mostrar?\n "))
for a in range(1,10):
  print(a, " x ", num_tab , " = ", a * num_tab)

#3. Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). ciclo for

edad = int(input('Por favor ingrese su edad: \n'))
for e in range (1,edad + 1):
  print(e)

#4. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

#5. Encuentra la suma de todos los números pares del 1 al 100 ciclo for
inicio = 0

for p in range(1,101,2):
  # print(i)
  inicio = inicio + p
print(f"El total de la suma de los números pares del 1-100  es: {inicio}")