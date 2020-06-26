inlist = [7, 5, 3, 3, 2]
print(f"Reyting - {inlist}")
digit = int(input("Vvedite chislo (-1 - vichod) "))
while digit != -1:
    for el in range(len(inlist)):
        if inlist[el] == digit:
            inlist.insert(el + 1, digit)
            break
        elif inlist[0] < digit:
            inlist.insert(0, digit)
        elif inlist[-1] > digit:
            inlist.append(digit)
        elif inlist[el] > digit and inlist[el + 1] < digit:
            inlist.insert(el + 1, digit)
    print(f"spisok - {inlist}")
    digit = int(input("Vvedite chislo "))