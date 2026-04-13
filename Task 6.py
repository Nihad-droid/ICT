"""# Sual 1
line = "Salam, siz hal hazırda bu kodu oxuyursunuz!"
symbol = input("Simvol daxil et: ")
if symbol in line:
    print("Daxildir.")
else:
    print("Daxil deyil.")

# Sual 2
string = input('Enter: ')
result = ""
for i in string:
    if i == 'a':
        result += "b"
    elif i == 'b':
        result += "a"
    elif i == 'A':
        result += "B"
    elif i == "B":
        result += "A"
    else:
        result += i
print(result)

# Sual 3
string = input("Daxil edin: ")
words = string.split()
x = 0
for i in words:
    x += 1
print(x)

# Sual 4
string = input("daxil edin: ")
words = string.split()
en_uzun = 0
for i in words:
    uzunluq = 0
    for k in i:
        if k != '.' and k != ',':    # Sozun yaninda noqte ve vergul islenerse onlari hesablama
            uzunluq += 1
    if uzunluq > en_uzun:
        en_uzun = uzunluq
        word = i
print(f"En uzun soz: {word}, uzunlugu: {en_uzun}")

# Sual 5
text = input("Soyad, ad və ata adinizi daxil edin: ")
words = text.split()
ad = words[1]
soyad = words[0]
ata_adi = words[2]
print(f"{ad[0]}.{ata_adi[0]}. {soyad}")

# Sual 6
path = input('Faylin unvanini daxil edin: ')
words = path.split("/")
for i in words:
    print(i)

# Sual 7
text = input("Setri daxil edin: ")
find = input("Neyi evezleyirik: ")  # Worddeki "find and replace funksiyasini yaratmaqimizi isteyirler"
replace = input("Ne ile evezleyirik: ")

text_length = 0     # Verilmis metnin uzunluqunu tapaq
for x in text:
    text_length += 1

length = 0
for y in find:      # Axtardigimiz sozun uzunluqun tapaq
    length += 1

i = 0
result = ""
while i < text_length:
    if text[i: i + length] == find:   # Axtarilan sozun uzunluqu qeder parcalarla yoxlama edek
        result += replace
        i += length
    else:
        result += text[i]
        i += 1
print(result)

# Sual 8
text = input("Input: ")
find = input("Axtarilan soz: ")

text_length = 0     # Verilmis metnin uzunluqunu tapaq
for x in text:
    text_length += 1

find_length = 0
for y in find:      # Axtardigimiz sozun uzunluqun tapaq
    find_length += 1

i = 0
result = 0
while i < text_length:
    if text[i: i + find_length] == find:
        result += 1
        i += find_length
    else:
        i += 1
print(f"{find} simvollarinin sayi: {result}")

# Sual 9
text = input("Setri daxil edin: ")
find = 'bayram'
replace = 'novruz'

text_length = 0  
for x in text:
    text_length += 1

length = 0
for y in find:      
    length += 1

i = 0
result = ""
count = 0
while i < text_length:
    if text[i: i + length].lower() == find.lower():
        if text[i] == 'B':
            result += replace.capitalize()
        else:
            result += replace
        i += length
        count += 1
    else:
        result += text[i]
        i += 1
print(f"Yeni cumle: {result}")
print(f"Deyisen sozlerin sayi = {count}")

# Sual 10
text = input("Setri daxil edin: ")
find = 'haqqı'
replace = 'sarı'

text_length = 0  
for x in text:
    text_length += 1

length = 0
for y in find:      
    length += 1

i = 0
result = ""
count = 0
while i < text_length:
    if text[i: i + length].lower() == find.lower():
        if text[i] == 'H':
            result += replace.capitalize()
        else:
            result += replace
        i += length
        count += 1
    else:
        result += text[i]
        i += 1
print(f"Yeni cumle: {result}")
print(f"Deyisen sozlerin sayi = {count}")

# Sual 11
text = input("Input: ")
result = ""

counter = 1
for i in text:
    if i == " ":
        counter = 0
    if counter != 2:
        result += i
    counter += 1
print(result)

# Sual 12
text = input("Setir: ")
saitler = "AOUE"
samitler = "bcmf"
reqemler = "3579"
durgu_isareleri = "!?,;"

result = ""
for i in saitler:
    if i in text:
        result += f'"{i}" '
for i in samitler:
    if i in text:
        result += f'"{i}" '
for i in reqemler:
    if i in text:
        result += f'"{i}" '
for i in durgu_isareleri:
    if i in text:
        result += f'"{i}" '
print(f"{result} simvollari var!")

# Sual 13
text = input("Ifadeni daxil edin:\n")

toplananlar = text.split('+')

total = 0

for i in toplananlar:
    total += int(i)

print(total)

# Sual 14
def birinci_metod():
    ifade = input("Ifadeni daxil edin:\n")
    result = 0

    cixma_index = 0
    toplama_index = 0
    x = 0
    for i in ifade:
        if i == "-":
            cixma_index = x
        elif i == "+":
            toplama_index = x
        x += 1

    if cixma_index < toplama_index:
        eded1 = ifade[:cixma_index]
        eded2 = ifade[cixma_index+1: toplama_index]
        eded3 = ifade[toplama_index+1:]
        print(int(eded1) - int(eded2) + int(eded3))
    else:
        eded1 = ifade[:toplama_index]
        eded2 = ifade[toplama_index+1: cixma_index]
        eded3 = ifade[cixma_index+1:]
        print(int(eded1) + int(eded2) - int(eded3))

def ikinci_metod():
    ifade = input("Ifadeni daxil edin: ")

    op1_idx = -1
    op1_type = ""
    op2_idx = -1
    op2_type = ""

    idx = 0
    for i in ifade:
        if i == "+" or i == "-":
            if op1_idx == -1:
                op1_idx = idx
                op1_type = i
            else:
                op2_idx = idx
                op2_type = i
        idx += 1


    num1 = int(ifade[:op1_idx])
    num2 = int(ifade[op1_idx + 1 : op2_idx])
    num3 = int(ifade[op2_idx + 1 :])


    if op1_type == "+":
        result = num1 + num2
    else:
        result = num1 - num2
    
    if op2_type == "+":
        result = result + num3
    else:
        result = result - num3

    print("Cavab:", result)

# Sual 15
text = input("Setri daxil edin: ")
words = text.split()
print(words[0])

# Sual 16
file = input("Faylin adini daxil edin: ")
extension = input("Uzantini daxil edin: ")
file = file.split(".")[:-1]
new_file = ""
for i in file:
    new_file += f"{i}."
print(f'{new_file}{extension}')

# Sual 17
name = input("Faylin adini daxil edin: ")
taboo = r"/\:*?“”<>|"

uzunluq = 0
for i in name:
    uzunluq += 1

for i in taboo:
    if i in name or uzunluq > 10:
        print("//")
        print("That name won't work. Use a name that doesn't include characters like \/:*?“”<>|")
        print("And please make sure it is not longer than 10 characters!")
        file = False
        break
    file = True
if file == True:
    print(f"{name} is saved")
"""
# Sual 18