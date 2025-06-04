def add(a, b, plus=0): #plus is a default argument
    x = a + b + plus
    return x


c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3) #keyboard argument
