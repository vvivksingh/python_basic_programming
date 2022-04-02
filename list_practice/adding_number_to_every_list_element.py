def sum_func(list, num):
    new_list = [i + num for i in list]
    return new_list


list = [1, 2, 3, 4, 5, 6]
num = 4
print(sum_func(list, num))


def sum_func2(list2, num):
    for i in list2:
        i = i + num
        newlist2.append(i)
    return newlist2


newlist2 = []
list2 = [5, 7, 8, 6, 3, 2]
print(sum_func2(list2, 5))
