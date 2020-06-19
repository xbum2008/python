number = int(input("Введите целое положительное число >>> "))
maxnumber = 1
while number != 0 :
    #number % 10
    if maxnumber <= number % 10:
        maxnumber = number % 10
    number = number // 10
    if maxnumber == 9:
        break
print("Результат равен ", maxnumber)