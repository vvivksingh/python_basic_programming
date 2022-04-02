x = " Hello, world "
print(x[-2::1])  # print last two strings
print(x[::-1])  # reverse the string
print(x[-1:-3:-1])  # print last two in reverse order
print(x[:5])  # its start slicing from the start
print(x[6:])  # its goes upto last
print(x.upper())
print(x.lower())
print(x.strip())  # remove whitespace from the beginning or the end
print(x.split("."))
print(x.split(","))  # if separator instance is present then its breaks the string from there
print(x.replace("H", "h"))


# string format

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))