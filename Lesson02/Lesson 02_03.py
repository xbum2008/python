n = int(input("Vvedite poryadkoviy nomer mesyatca "))
#variant s dict
seasons = {'Zima': (1, 2, 12),
           'Vesna': (3, 4, 5),
           'Leto': (6, 7, 8),
           'Osen': (9, 10, 11)}
for key in seasons.keys():
    if n in seasons[key]:
        print(key)

# variant s list

zima = (1, 2, 12)
vesna = (3, 4, 5)
leto = (6, 7, 8)
osen = (9, 10, 11)
if n in zima:
  print("Zima")
if n in vesna:
  print("Vesna")
if n in leto:
  print("Leto")
if n in osen:
  print("Osen")