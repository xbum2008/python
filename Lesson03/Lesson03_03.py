def my_func(arg1 , arg2, arg3):
    minarg = min(arg1 , arg2, arg3)
    return arg2 + arg3 + arg1 - minarg

print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')