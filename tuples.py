x = (0,0,2,2) #immutable list
x[0] = 1 # this will raise an error
x.append(3) # this will also raise an error
print(type(x))