# Integer: números enteros
# Float: números con decimales

dolar = 200
monto_a_importar = dolar*1500*300

print("El monto a importar en pesos es:", monto_a_importar)

comision = 0.03*monto_a_importar
sellado = 15000

total = monto_a_importar + sellado + comision

print("El total es:",total)

cada_socio = total/5

print("Cada socio gana:", cada_socio)

# recordar que no se puede dividir por cero

# cómo obtener caracteres de un string
string="python"

print(string[0])
print(string[-1])

# si quiero dejar un renglón en la consola: /n