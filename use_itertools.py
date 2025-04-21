import math

def C(n, k):
    return math.comb(n, k)

n = 400
k = 104
p = 0.2
q = 1 - p
c = C(400, 104)

r = c * p**k * q**(n-k)
print("Неокругленный ответ: ", r)
r = round(r, 5)
print("Округленный ответ: ", r)