
def pangkat(a, b):
    c = 1
    for i in range(1, b+1):
        c = c*a
    return c


print(pangkat(2, 2))
print(pangkat(3, 3))
print(pangkat(10, 5))