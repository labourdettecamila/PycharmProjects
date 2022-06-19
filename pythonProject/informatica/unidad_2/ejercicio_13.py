deudas = [1323.23, 5755.20, 1928, 3876, 4539, 4648, 4000, 3713, 3148, 1240, 3232, 4948, 2491,
2092, 3471, 1704.92, 4630, 4697, 1495.30, 2174, 2897, 2505, 3502, 2573]

deudas_con_interes = []

for deuda in deudas:
    deudas_con_interes.append(deuda + (3.5*deuda))

print(deudas_con_interes)
