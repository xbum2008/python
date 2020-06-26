instr = input("Vvedite stroku ")
inword = []
num = 1
for el in range(instr.count(' ') + 1):
    inword = instr.split()
    if len(str(inword)) <= 10:
        print(f" {num} {inword [el]}")
        num += 1
    else:
        print(f" {num} {inword [el] [0:10]}")
        num += 1