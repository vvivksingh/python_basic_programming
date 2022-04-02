def square_func(list):
    for i in list:
        i = i * i
        square_list.append(i)
    return square_list


square_list = []
list = [1, 2, 3, 4, 5, 6]
print(square_func(list))


def square_func2(list):
    square_list2 = [i * i for i in list]

    return square_list2


print(square_func2(list))
