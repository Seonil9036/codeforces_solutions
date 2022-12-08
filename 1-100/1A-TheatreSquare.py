import math 
 
n, m, a = map(int, input("").split())

col = math.ceil(n / a)
row = math.ceil(m / a)
 
print (col * row)
