frecuencia_obtenida  = (166,95,47,118,95,48,95,144,120,72)
#frecuencia_esperada = (100,100,100, 100,100,100, 100,100,100,100)

results = []
total = 0
for value in frecuencia_obtenida:
    res = (100-value)**2/100
    total += res
print(results)
print(total)


