# Sual 1
tuple = (4,6,3,9,12,24,24,76,63)
indexes = []
index = 0
for i in tuple:
    if i == 24:
        indexes.append(index)
    index += 1
print(f"24 ededinin indexleri: {indexes}")

# Sual 2
tuple = (4,6,3,9,12,24,24,76,63)
for i in tuple:
    if i%3==0:
        print(i,end=" ")

# Sual 3
list1 = []
for i in range(1,6):
    x = int(input(f"{i}. "))
    list1.append(x)
list2 = []
for i in list1:
    list2.append(i+5)
print(list1, list2, sep='\n')

# Sual 4
list1 = []
for i in range(1,6):
    x = int(input(f"{i}. "))
    list1.append(x)
list2 = []
for i in list1:
    if i%2 != 0:
        list2.append(i)
