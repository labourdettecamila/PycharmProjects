lista_encuestados = [True, False, True, True, True, False, True, False, True, True,
True, False, False, True, True, True, True, False, True, True,
True, False, True, True, False, True, True, False, True, False,
True, True, True, False, True, True, True, False, True, False,
True, True, True, False, False, True, True, True, True, False,
True, True, True, False, True, True, False, True, True, False,
True, False, True, True]

gusto = 0
no_gusto = 0

for encuestado in lista_encuestados:
    if encuestado == True:
        gusto += 1
    else:
        no_gusto += 1

porcentaje_gusto = gusto*100/len(lista_encuestados)
porcentaje_no_gusto = no_gusto*100/len(lista_encuestados)

print ("Les gustó la bebida:", porcentaje_gusto,"%")
print ("No les gustó la bebida:", porcentaje_no_gusto,"%")

print("\n")

if porcentaje_gusto > 65:
    print(f"El producto es exitoso, resultado: {porcentaje_gusto}")
else:
    print("Hay que mejorar el producto")