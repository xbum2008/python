def my_func(x, y):
    #return 1 / x ** abs(y)
    return x ** y

def my_func2(x, y):
    rt = x
    while y != -1:
        y += 1
        x = x * rt
    return 1 / x

print(my_func(0.25, -10))
print(my_func2(0.25, -10))