from datetime import date
from datetime import time
from datetime import timedelta

print ("Por favor ingrese sus datos personales, acontinuación. \n")
nro_documento = int(input ('Ingrese su Documento: '))
nombre = (input ('Ingrese su Nombres: '))
apellido = (input ('Ingrese su Apellidos: '))
direccion = bool(input ('Ingrese su Correo Electronico: '))
edad = int(input ('Ingrese su Edad: '))
estado_civil = (input ('Ingrese su estado civil: '))
estatura = float(input ('Ingrese su estatura en centimetros: '))
print ('\n Acontinuacion ingrese la fecha en que fue contratado.\n')
ano = int(input('Introduzca el año: '))
mes = int(input('Introduzca el mes: '))
dia = int(input('Introduzca el día: '))
sueldo = float('1500000')
comi_salarial = float(sueldo * 0.05)
bono_edad = float(sueldo * 0.05)
hijo = int(input ('Ingrese cantidad de hijos: '))



print ("\n Sus datos ingresados son: \n nombres: ", nombre ,apellido , "\n su edad es: ", edad ,"Años")
print ("Tiene: " ,hijo, "hij@/s \n" + "Su estado civil es: ",estado_civil,"\n Su estatura es: ",estatura,"cm")

if hijo >= 1 and estado_civil == 'casado':
  estado1 = 'ganaste un viaje'
  print(f'{estado1}')
else: 
  estado2 = 'no cumples el requisito' 
  print(f'{estado2}')

if sueldo >= 1000000 and sueldo <= 1500000 and edad < 55:
  total1 = comi_salarial + sueldo
  print(f"El pago para este periodo es de {sueldo}, su comsión salarial es de ${comi_salarial:,.0f} y por lo cual su sueldo a pagar es ${total1:,.0f}")
elif sueldo >= 1500001 and sueldo <= 2000000 and edad < 55:
  total2 = comi_salarial + sueldo
  print(f"El pago para este periodo es de {sueldo}, su comsión salarial es de ${comi_salarial:,.0f} y por lo cual su sueldo a pagar es ${total2:,.0f}")
elif edad > 55 and sueldo >= 1000000 and sueldo <= 1500000:
  prepension1 = bono_edad + (sueldo * 0.05) + sueldo
  print(f"El pago para este periodo es de {sueldo}, su bono de prepensión es de ${bono_edad:,.0f} y de comisión salarial es {comi_salarial} por lo cual su sueldo a pagar es ${prepension1:,.0f}")
elif edad > 55 and sueldo >= 1500001 and sueldo <= 2000000:
  prepension2 = bono_edad + (sueldo * 0.05) + sueldo
  print(f"El pago para este periodo es de {sueldo}, su bono de prepensión es de ${bono_edad:,.0f} y de comisión salarial es {comi_salarial} por lo cual su sueldo a pagar es ${prepension2:,.0f}")
else:
  prepension2_1 = "no tiene comsión porque no cumple los requisitos"
  print(f'{prepension2_1}')

#fecha_contrato = date(ano, mes, dia)
#hoy = date.today()
#dia = 20
#dias_laborados = hoy - fecha_contrato

#if dias_laborados == hoy and sueldo < 1000000:
#  bono_ali = int(120000)
#else: dias_laborados > hoy and sueldo > 1000000
#print (' no puedes recibir el bono alimenticio')

#print ("La fecha de su contrato es:",fecha_contrato,"y sus dias laborados son:",dias_laborados)
#print ("Con un sPueldo mensual de $", end=f"{sueldo}" " Pesos Colombianos")


