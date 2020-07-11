my_list = [12, 10, 422, 6, 6, 66, 53, 53, 45, 3, 12, 10, 3, 53]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)
