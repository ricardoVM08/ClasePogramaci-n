n = 2000000
es_primo = [True] * n
es_primo[0] = False
es_primo[1] = False

for i in range(2, n):
    if es_primo[i]:
        for j in range(i * i, n, i):
            es_primo[j] = False

suma = 0
for i in range(n):
    if es_primo[i]:
        suma += i

print(suma)