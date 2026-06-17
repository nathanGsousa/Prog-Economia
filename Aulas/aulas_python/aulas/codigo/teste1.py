x = {}
x['f'] = -2
x['g'] = 0 
x['h'] = 2.1

a = 1
b = 1
c = -6
z = {}

for i in x.keys():
    z[i] = a * x[i] ** 2 + b * x[i] + c
    print(z)
print(z)
print(type(z))
print(type(x))