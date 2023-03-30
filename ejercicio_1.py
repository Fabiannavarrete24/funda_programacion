# ejercicio 1
#Un vendedor recibe un sueldo base más un 10% extra por
#comisión de sus ventas, el vendedor desea saber cuánto
#dinero obtendrá por concepto de comisiones por las tres
#ventas que realiza en el mes y el total que recibirá en
#el mes tomando en cuenta su sueldo base y comisiones.

salario = float("1000000")
comision = float("0.10")
venta1 = float(input("ingrese el valor total de la venta: $"))
venta2 = float(input("ingrese el valor total de la venta: $"))
venta3 = float(input("ingrese el valor total de la venta: $"))
comision1 = venta1 * comision
comision2 = venta2 * comision
comision3 = venta3 * comision
valor_comi = comision1 + comision2 + comision3
valor_pagar = salario + comision1 + comision2 + comision3

print(f"Su sueldo es de ${salario:,.0f}")
print("El valor de comsión en la venta 1 es = ${:,.0f}".format(comision1))
print("El valor de comsión en la venta 2 es = ${:,.0f}".format(comision2))
print("El valor de comsión en la venta 3 es = ${:,.0f}".format(comision3))
print(f"el valor total de comisiones es ${valor_comi:,.0f}")
print(f"Su sueldo correspondiente para este mes es de ${valor_pagar:,.0f} correspondiente las de mes actual")

#ejercicio 2
#Una tienda ofrece un descuento del 15% sobre el total
#de la compra y un cliente desea saber cuánto deberá
#pagar finalmente por su compra.

producto1 = float(input("Ingrese el Valor del producto 1: $"))
producto2 = float(input("Ingrese el Valor del producto 2: $"))
producto3 = float(input("Ingrese el Valor del producto 3: $"))
total = producto1 + producto2 + producto3
descuento = total * 0.15
total_pagar = total - descuento

print(f"El valor que debe pagar es ${total_pagar:.0f}") 

#ejercicio 4
#Un maestro desea saber qué porcentaje de hombres y que
#porcentaje de mujeres hay en un grupo de estudiantes.

estu_f = int(input("Ingrese el numero de estudiantes del genero femenino: "))
estu_m = int(input("Ingrese el numero de estudiantes del genero masculino: "))
estudiantes = int(estu_f + estu_m)
porc_f = float(estu_f / estudiantes) * 100
porc_m = float(estu_m / estudiantes) * 100

print(f"El porcentaje de mujeres es %{porc_f:,.0f}")
print(f"El porcentaje de hombres es %{porc_m:,.0f}")
print(f"El numero total de estudiantes es {estudiantes}")

