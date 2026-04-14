"""# Sual 1
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
print(list1, list2, sep='\n')

# Sual 5
import random
list = [random.randint(0, 10) for i in range(7)]
cem=0
for i in list:
    cem += i
hasil=1
for i in list:
    hasil*=i
average=cem/7
maximum=0
index=0
for i in list:
    if i > maximum:
        maximum = i
        max_index = index
    index += 1
minimum=11
index=0
for i in list:
    if i < minimum:
        minimum = i
        min_index = index
    index += 1
print(list, cem, hasil, average, maximum, max_index, minimum, min_index, sep="\n")

# Sual 6
import random
list1 = [random.randint(1, 100) for i in range(10)]
list2 = []
list3 = []
for i in list1:
    if i < 50:
        list2.append(i)
    else:
        list3.append(i)
sum_list2 = 0
count2 = 0
sum_list3 = 0
count3 = 0
for i in list2:
    sum_list2 += i
    count2 += 1
for i in list3:
    sum_list3 += i
    count3 += 1
print(list1)
print(f"[0, 50) araliginda ededi orta = {(sum_list2/count2):.1f}")
print(f"[50, 100) araliginda ededi orta = {(sum_list3/count3):.1f}")
   
# Sual 7
list = [x**2 for x in range(1, 16)]
y = 0
list2 = []
list3 = []
for i in list:
    if y<=4:
        list2.append(i)
    elif y>=10:
        list3.append(i)
    y += 1
print(list, list2, list3)

# Sual 8
list1 = []
list2 = []
while True:
    x = input("list 1 ucun eded daxil edin: ")
    if x != "": 
        list1.append(int(x))
    else:
        break
print(f"list1 = {list1}")
while True:
    x = input("list 2 ucun eded daxil edin: ")
    if x != "": 
        list2.append(int(x))
    else:
        break
print(f"list2 = {list2}")
ortaq = False
for x in list1:
    if ortaq == False:
        for y in list2:
            if x == y:
                print("Ortaq element var.")
                ortaq = True
if ortaq == False:
    print("Ortaq element yoxdur.")

# Sual 9
list1 = []
list2 = []
while True:
    x = input("list 1 ucun eded daxil edin: ")
    if x != "": 
        list1.append(int(x))
    else:
        break
print(f"list1 = {list1}")
while True:
    x = input("list 2 ucun eded daxil edin: ")
    if x != "": 
        list2.append(int(x))
    else:
        break
print(f"list2 = {list2}")

count = 0
found_any = False
idx1 = 0
for x in list1:
    idx2 = 0
    for y in list2:
        if idx1 == idx2 and x == y:
            if not found_any:
                print("Tekrarlanan elementler:", end=" ")
                found_any = True

            print(x, end=" ")
            count += 1

        idx2 += 1
    idx1 += 1 

if not found_any:
    print("Ortaq element yoxdur.")

print("\nEyni indeksde yerlesen eyni elementlerin sayi:", count)

# Sual 10
list = [3,4,6,7,23]
result_list = []

index = 0
for i in list:
    if index != 0:
        result_list.append(i)
    index += 1
index = 0
for i in list:
    if index == 0:
        result_list.append(i)
    index += 1
print(result_list)

# Sual 11
yeni_list = []
list1 = ['A', 'B', 'C']
list2 = [1, 2, 3]
idx1 = 0
for x in list1:
    idx2 = 0
    for y in list2:
        if idx1 == idx2:
            yeni_list.append([x, y])
        idx2 += 1
    idx1 += 1
print(yeni_list)

# Sual 12
list = [5,7,5,9,2,6,4,3,2,5,6]
sum = 0
for i in list:
    if i%2 != 0:
        sum += i
    else:
        break
print(sum)

# Sual 13
import random
N = int(input("Siyahinin uzunlugunu daxil edin: "))
list = [random.randint(10, 50) for i in range(N)]
yekun_list = []
for i in list:
    for k in range(1, i):
        if k**2 == i:
            yekun_list.append(i)
print(yekun_list)

# Sual 14
import random
N = int(input("Siyahinin uzunlugunu daxil edin: "))
list = [random.randint(100, 999) for i in range(N)]
yekun_list = []
for i in list:
    y = i % 10
    x = (i // 10) % 10
    if (abs(x-y)%2 != 0) and ((x+y)%2 != 0):
        yekun_list.append(i)
print('list1 =', list)
print('list2 =', yekun_list)

# Sual 15
import random
N = int(input("Siyahinin uzunlugunu daxil edin: "))
A = [random.randint(0, 100) for i in range(N)]
B = []

def prime(X):
    for i in range(2, X):
        if X % i == 0:
            return False
    return True

for element in A:
    if prime(element):
        B.append(element)
print(A, B, sep="\n")

# Sual 16
import random
A = [random.randint(-10, 10) for i in range(10)]
B = []
for i in A:
    if i % 2 == 0 and i < 0:
        B.append(i)
print(A, B, sep="\n")

# Sual 17
list1 = [1,2,'aasf','1','123',123]
list2 = []
for i in list1:
    if type(i) == int and i >= 0:
        list2.append(i)
print(list2)

# Sual 18
eded = int(input("Eded daxil edin: "))
list = []
for i in range(1,eded+1):
    if eded%i == 0:
        list.append(i)
print(list)

# Sual 19
import math
N = [6,2,5,3,9,7,4]
List = []

for i in N:
    n = list(range(1, i+1))
    sum = 0
    for x in n:
        sum += (4*math.sin(x)+2*x)/(math.log(9*x, 3)*2**x)
    List.append(sum)

print(List)
"""