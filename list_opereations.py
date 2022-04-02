thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[1:3])
print(thislist[:2])
thislist[1] = "mango"
print(thislist)  # ['apple', 'mango', 'cherry']
print(thislist[1])
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon']
thislist[1:2] = ["mango", "banana"]
print(thislist)  # ['apple', 'mango', 'banana', 'watermelon']
thislist.insert(2, "cherry")
print(thislist)  # ['apple', 'mango', 'cherry', 'banana', 'watermelon']
thislist.append("orange")
print(thislist)  # ['apple', 'mango', 'cherry', 'banana', 'watermelon', 'orange']
thislist2 = ["guava", "pineapple"]
thislist.extend(thislist2)
print(thislist)  # ['apple', 'mango', 'cherry', 'banana', 'watermelon', 'orange', 'guava', 'pineapple']
thistuple = ("kiwi", "grapes")
thislist.extend(thistuple)
print(thislist)  # ['apple','mango','cherry','banana','watermelon', 'orange', 'guava', 'pineapple', 'kiwi', 'grapes']
thislist.remove("banana")
print(thislist)  # ['apple', 'mango', 'cherry', 'watermelon', 'orange', 'guava', 'pineapple', 'kiwi', 'grapes']
thislist.pop(0)
print(thislist)  # ['mango', 'cherry', 'watermelon', 'orange', 'guava', 'pineapple', 'kiwi', 'grapes']
thislist.pop()
print(thislist)  # ['mango', 'cherry', 'watermelon', 'orange', 'guava', 'pineapple', 'kiwi']
# del thislist[0]
# del thislist
# thislist.clear()
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(i)

thislist3 = ["apple", "banana", "cherry"]
[print(x) for x in thislist3]

