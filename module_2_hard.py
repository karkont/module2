import random
a1 = list(range(3,21))
a = random.choice(a1)               # Первое поле
b = []                              # Второе поле
for i in range(1,a):
    for j in range(1,a):
        if i >= j:
            continue
        if a % (i+j) == 0:
            b.append([i,j])
from itertools import chain
b = list(chain(*b))
print("Если на превой табличке: ", a)
print("Пароль будет: ", "".join(str(n) for n in b))
