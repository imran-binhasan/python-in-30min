x = [4, 'Hello', 3.12, True, None]
y = [1, 2]

print(type(x))
print(len(x), len(y)) 
x.append('World')
x.extend(y)
x[1] = 5.67
x.pop(0)
print(x)

y=x[:] #copy 
print(y)