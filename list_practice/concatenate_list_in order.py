list1 = ["Hello ", "Take "]
list2 = ["Dear", "Sir"]

list3 = [i+j for i in list1 for j in list2]
print(list3)


# expected output['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# def conc_func(list1, list2):
#     for i in list1:
#         for j in list2:
#             list3.append(i + j)
#     return list3


# list3 = []
# print(conc_func(list1, list2))
