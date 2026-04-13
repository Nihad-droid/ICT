"""# Task 1
import random
suits = ["Hearts", "Spades", "Club", "Diamond"]
values = ["2","3","4","5","6","7","8","9","10", "Queen", "Jack", "King", "Ace"]
rand1 = random.randint(0, 3)
rand2 = random.randint(0, 12)
print(suits[rand1], values[rand2])

# Task 2
def FindSumofTerms(N):
    for i in N:
        sum = 0
        for x in range(i+1):
            sum += (3+2*x)/2**x
        print(f"N = {i} sum= {sum}")

N = [3, 5, 10, 15, 50, 100, 1000]
FindSumofTerms(N)

# Task 3
def function(N):
    last_digit = N % 10
    
    length = 0
    temp = N
    while temp > 0:
        temp //=10
        length += 1
    
    first_digit = N // (10 ** (length-1))

    if first_digit**2 + last_digit**2 < 100:
        return True
    else:
        return False

N = int(input("Eded daxil edin: "))
print(function(N))

# Task 4
p1_100 = float(input("Price for first 100 of Company 1: "))
p1_1000 =float(input("Price for first 1000 of Company 1: "))
p1_rest =float(input("Price for rest of Company 1: "))
p2_100 = float(input("Price for first 100 of Company 2: "))
p2_1000 =float(input("Price for first 1000 of Company 2: "))
p2_rest =float(input("Price for rest of Company 2: "))
amount = int(input("How many do you want?: "))
p1_price = 100*p1_100 + 1000*p1_1000 + (amount-1100)*p1_rest
p2_price = 100*p2_100 + 1000*p2_1000 + (amount-1100)*p2_rest
if p1_price > p2_price:
    print(f"Go with company 2 as they offer {p2_price}, while company 1 presents {p1_price}")
elif p1_price == p2_price:
    print(f"Both companies offer {p1_price}. Choose as you wish.")
else:
    print(f"Go with company 1 as they offer {p1_price}, while company 2 presents {p2_price}")

# Task 5
anna_start = int(input("Enter minutes after midnight for Anna's advent: "))
bob_start = int(input("Enter minutes after midnight for Bob's arrival:"))
anna_end = int(input("Enter minutes after midnight for Anna's departure: "))
bob_end = int(input("Enter minutes after midnight for Bob's furlough: "))
def minimum(a,b):
    if a > b:
        return b
    elif a < b:
        return a
    else:
        return a
def maximum(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return b

meet_time = minimum(anna_end, bob_end) - maximum(anna_start, bob_start)
print(meet_time if meet_time > 0 else "they didnt meet")

# Task 6
x = float(input("x-i daxil edin: "))
y = float(input("y-daxil edin: "))
if (y <= -x**2+5 and x**2+y**2>=3 and y>=-3) or ((x+0.5)**2+(y-0.5)**2<=0.1 or (x-0.5)**2+(y-0.5)**2<=0.1 or (x**2+(y+0.6)**2<=0.7 and y<=-0.5)):
    print("Şükür, daxildir.")
else:
    print("Daxil deyil...")
"""                                             
