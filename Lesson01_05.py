income = int(input("Введите значение выручки фирмы >>> "))
outcome = int(input("Введите значение издержек фирмы >>> "))

if income > outcome:
        print("Фирма работает в прибыль.")
        rent = (income - outcome) / income
        print("Рентабельность равна ", rent)
        emp = int(input("Введите количество сотрудников фирмы >>> "))
        emp2 = (income - outcome) / emp
        print("Прибыль на сотрудника равна ", emp2)
else:
        print("Фирма работает в убыток или в ноль.")