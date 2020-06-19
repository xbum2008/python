time = int(input("Введите время в секундах >>> "))
hour = time // 3600
minute = (time % 3600) // 60
sec = (time % 3600) % 60
print(f"{hour}:{minute}:{sec}")