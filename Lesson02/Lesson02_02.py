
inlist = []
n = int(input("Vvedite kolichestvo elementov "))
for el in range(n):
    inlist.append(input("Vvedite znachenie "))
print("Vash spisok ", inlist)
if len(inlist)%2==0:
    n=len(inlist)
else:
    n=len(inlist)-1
for i in range(0,n-1,2):
    inlist[i],inlist[i+1]=inlist[i+1],inlist[i]
print("Vash spisok posle obrabotki", inlist)