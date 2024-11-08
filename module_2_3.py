my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while True:
    number = a
    if (my_list[number] >= 0):
        print(my_list[number])
        number = number + 1
        a = a + 1
    else:
        break

