# Sual 1
import random
massiv = [random.randint(0,5) for _ in range(random.randint(5,10))]
print(massiv)
find = int(input("Ne axtaririq: "))
tapilanlar = []
index = 0
for element in massiv:
    if element == find:
        tapilanlar = tapilanlar + [f"A[{index}]={element}"]
    index += 1
if tapilanlar:
    print("Tapildi: ")
    for i in tapilanlar:
        print(i,end=", ")
else:
    print("Tapilmadi.")

# Sual 2
import random

def sum_of_digits(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

massiv = [random.randint(10, 100) for _ in range(random.randint(5,15))]
print('massiv =',massiv)
yeni_massiv = []

for i in massiv:
    yeni_massiv = yeni_massiv + [sum_of_digits(i)]

print('reqemleri toplanmis =',yeni_massiv)

length = 0
for i in yeni_massiv:
    length+=1

for i in range(length):
    for y in range(0, length-1):
        if yeni_massiv[y] < yeni_massiv[y+1]:
            yeni_massiv[y], yeni_massiv[y+1] = yeni_massiv[y+1], yeni_massiv[y]
print('sorted =',yeni_massiv)

# Sual 3
def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

massiv = []
print("5 setri daxil edin: ")   # Numune: 1.ana \n 2.ata
for i in range(5):
    massiv = massiv + [input().split('.')[-1]]
print(massiv)

for i in range(5):
    for x in range(0, len(massiv)-1):
        if massiv[x] > massiv[x+1]:
            massiv[x], massiv[x+1] = massiv[x+1], massiv[x]
print(massiv)

# Sual 4
names = []
print("Ad, ata adi ve soyadinizi daxil edin: ")
print("Numune: A.Q. Veliyev")
print("Bitirmek ucun bos setir daxil et.")

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

while len(names) < 20:
    name = input()
    if name != "":
        names = names + [name]
    else:
        break

def split(x,y): # x = Cumle, y = ayirici
    ifade = ""
    result = []
    index = 0
    while index < len(x):
        if x[index:index+len(y)] == y:
            result = result + [ifade]
            ifade = ""
            index += len(y)
        else:
            ifade += x[index]
            index += 1
    result = result + [ifade]
    return result

for _ in range(len(names)):
    for x in range(0, len(names) - 1):
        if split(names[x], '. ')[-1] > split(names[x+1], '. ')[-1]:
            names[x], names[x+1] = names[x+1], names[x]
print(names)

# Sual 5
import random

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

Unsorted = [random.randint(-100, 100) for _ in range(10)]
print('Unsorted =', Unsorted)
for i in range(len(Unsorted)):
    for j in range(0, len(Unsorted)-1):
        if Unsorted[j] < Unsorted[j+1]:
            Unsorted[j], Unsorted[j+1] = Unsorted[j+1], Unsorted[j]
print('Sorted_1 =', Unsorted)
Half1 = Unsorted[:len(Unsorted)//2]
Half2 = Unsorted[len(Unsorted)//2:]
for i in range(len(Half1)):
    for j in range(0, len(Half1)-1):
        if Half1[j] > Half1[j+1]:
            Half1[j], Half1[j+1] = Half1[j+1], Half1[j]
for i in range(len(Half2)):
    for j in range(0, len(Half2)-1):
        if Half2[j] > Half2[j+1]:
            Half2[j], Half2[j+1] = Half2[j+1], Half2[j]
print("Sorted_2 =", Half1+Half2)

# Sual 6
import random

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

massiv = [random.randint(-100, 100) for _ in range(6)]
new_massiv = []
print(massiv)
for i in massiv:
    if i > 0:
        new_massiv = new_massiv + [i]
for i in massiv:
    if i <= 0:
        new_massiv = new_massiv + [i]

for i in range(len(new_massiv)):
    for j in range(0, len(new_massiv)-1):
        if new_massiv[j] > 0 and new_massiv[j+1] > 0:
            if new_massiv[j] < new_massiv[j+1]:
                new_massiv[j], new_massiv[j+1] = new_massiv[j+1], new_massiv[j]
        elif new_massiv[j] <= 0 and new_massiv[j+1] <= 0:
            if new_massiv[j] > new_massiv[j+1]:
                new_massiv[j], new_massiv[j+1] = new_massiv[j+1], new_massiv[j]
print(new_massiv)

# Sual 7
import random

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

massiv1 = [random.randint(-10000, 10000) for _ in range(1000)]
massiv2 = [random.randint(-10000, 10000) for _ in range(1000)]
massiv3 = [random.randint(-10000, 10000) for _ in range(1000)]
massiv4 = [random.randint(-10000, 10000) for _ in range(1000)]
massiv5 = [random.randint(-10000, 10000) for _ in range(1000)]
massivler1 = [massiv1, massiv2, massiv3, massiv4, massiv5]
massivler2 = []

for massiv in massivler1:
    new_sub_list = []
    for item in massiv:
        new_sub_list = new_sub_list + [item]
    massivler2 = massivler2 + [new_sub_list]
swaps1 = 0
for massiv in massivler1:
    for i in range(len(massiv)):    # Bubble Sort alqoritmi
        for j in range(0, len(massiv)-1):
            if massiv[j] > massiv[j+1]:
                massiv[j], massiv[j+1] = massiv[j+1], massiv[j]
                swaps1 += 1
average_swaps1 = swaps1/5
swaps2 = 0
for massiv in massivler2:
    for i in range(len(massiv)):    # Selective Sort alqoritmi
        min_index = i
        for j in range(i+1, len(massiv)):
            if massiv[j] < massiv[min_index]:
                min_index = j
        massiv[i], massiv[min_index] = massiv[min_index], massiv[i]
        swaps2 += 1
average_swaps2 = swaps2/5
print('bubble sort:', average_swaps1, 'selective sort:', average_swaps2)

# Sual 8
import random

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

X = int(input("X ededini daxil edin: "))
massiv = [random.randint(1,10) for _ in range(10, 20)]
print(massiv)
for i in range(len(massiv)):
    for x in range(0, len(massiv)-1):
        if massiv[x] > massiv[x+1]:
            massiv[x], massiv[x+1] = massiv[x+1], massiv[x]
print(massiv)

count = 0
low = 0
high = len(massiv)-1
found = False
while low <= high:
    mid = (low + high) // 2
    count += 1
    if massiv[mid] == X:
        found = True
        break
    elif massiv[mid] < X:
        low = mid + 1
    else:
        high = mid - 1
if found:
    print(X, 'tapildi!', 'muqayiselerin sayi:', count)
else:
    print(X, 'tapilmadi!')

# Sual 9
import random

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

X = int(input("X ededini daxil edin: "))
massiv = [random.randint(1,10) for _ in range(10, 20)]
print(massiv)
for i in range(len(massiv)):
    for x in range(0, len(massiv)-1):
        if massiv[x] > massiv[x+1]:
            massiv[x], massiv[x+1] = massiv[x+1], massiv[x]
print(massiv)


def first_occurence(massiv, X):
    low = 0
    high = len(massiv)-1
    first_index = -1
    while low <= high:
        mid = (low + high) // 2
        if massiv[mid] == X:
            first_index = mid
            high = mid - 1  # Sola dogru get
        elif massiv[mid] < X:
            low = mid + 1
        else:
            high = mid - 1
    return first_index

def last_occurence(massiv, X):
    low, high = 0, len(massiv) - 1
    last_idx = -1
    while low <= high:
        mid = (low + high) // 2
        if massiv[mid] == X:
            last_idx = mid
            low = mid + 1  # Saga dogru get
        elif massiv[mid] < X:
            low = mid + 1
        else:
            high = mid - 1
    return last_idx

first = first_occurence(massiv, X)
last = last_occurence(massiv, X)

if first != -1:
    count = last- first + 1
    print(f"{X} {count} defe var.")
else:
    print("Tapilmadi!")

# Sual 10
import random

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

massiv = [random.randint(1,10) for _ in range(10, 20)]
for i in range(len(massiv)):
    for x in range(0, len(massiv)-1):
        if massiv[x] > massiv[x+1]:
            massiv[x], massiv[x+1] = massiv[x+1], massiv[x]
print('sorted massiv =',massiv)
X = int(input("X ededini daxil edin: "))

def binary_search_closest(massiv, x):
    low = 0
    high = len(massiv) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if massiv[mid] == x:
            return massiv[mid], True
        if massiv[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    low = min(low, len(massiv) - 1)
    high = max(high, 0)
            
    # Hansı qonşunun daha yaxın olduğunu tapaq.
    if abs(massiv[low] - x) < abs(massiv[high] - x):
        return massiv[low], False
    else:
        return massiv[high], False

result, found = binary_search_closest(massiv, X)
if found:
    print(f"{X} ededi tapıldı.")
else:
    print(f"{X} ededi tapılmadı. En yaxın eded: {result}")

# Sual 11
import random

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

massiv = [random.randint(100, 1000) for _ in range(8)]
print("Massiv:", massiv)

def odd_counter(x):
    count = 0
    while x > 0:
        d = x % 10
        x //= 10
        if d % 2 == 1:
            count += 1
    return count

def even_counter(x):
    count = 0
    while x > 0:
        d = x % 10
        x //= 10
        if d % 2 == 0:
            count += 1
    return count

half1 = massiv[:len(massiv)//2]
half2 = massiv[len(massiv)//2:]

for i in range(len(half1)):    # Selective Sort alqoritmi
    min_index = i
    for j in range(i+1, len(half1)):
        if odd_counter(half1[j]) < odd_counter(half1[min_index]):
            min_index = j
    half1[i], half1[min_index] = half1[min_index], half1[i]
for i in range(len(half2)):    
    max_index = i
    for j in range(i+1, len(half2)):
        if even_counter(half2[j]) > even_counter(half2[max_index]):
            max_index = j
    half2[i], half2[max_index] = half2[max_index], half2[i]
print('Yekun =', half1 + half2)

# Sual 12
import random

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

N = int(input("Interval daxil edin: "))
mylist = [random.randint(2, N-1) for _ in range(10)]
print(mylist)

def non_zero__counter(x):
    count = 0
    while x > 0:
        d = x % 10
        x //= 10
        if d != 0:
            count += 1
    return count

def sum_of_digits(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

half1 = mylist[:len(mylist)//2]
half2 = mylist[len(mylist)//2:]

for i in range(len(half1)): # Secme (selective sorting) usulu
    min_index = i       # artan sira
    for j in range(i+1, len(half1)):
        if non_zero__counter(half1[j]) < non_zero__counter(half1[min_index]):
            min_index = j
    half1[i], half1[min_index] = half1[min_index], half1[i]
for i in range(len(half2)):
    max_index = i   # azalan sira
    for j in range(i+1, len(half2)):
        if sum_of_digits(half2[j]) > sum_of_digits(half2[max_index]):
            max_index = j
    half2[i], half2[max_index] = half2[max_index], half2[i]
mylist = half1 + half2
print('mylist sorted =', mylist)  


r"""
 ________________________________
/ This code is written by Nihad. \
\ All rights are reserved.       /
 --------------------------------
         \
          \
               ,.-----__
            ,:::://///,:::-.
           /:''/////// ``:::`;/|/
          /'   ||||||     :://'`\
        .' ,   ||||||     `/(  e \
  -===~__-'\__X_`````\_____/~`-._ `.
              ~~        ~~       `~-'
"""