a = int(input("Введите значение начального километража >>> "))
b = int(input("Введите значение целевого километража >>> "))
i = 1
while a < b :
    i +=1
    a = a * 1.1
print("Результат будет достигнут за", i, "дня/ей.")