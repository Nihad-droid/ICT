"""# Task 1
import random
suits = ["Hearts", "Spades", "Club", "Diamond"]
values = ["2","3","4","5","6","7","8","9","10", "Queen", "Jack", "King", "Ace"]
rand1 = random.randint(0, 3)
rand2 = random.randint(0, 12)
print(suits[rand1], values[rand2])
"""
# Task 2
def FindSumofTerms(N):
    for i in N:
        sum = 0
        for x in range(i+1):
            sum += (3+2*x)/2**x
        print(f"N = {i} sum= {sum}")

N = [3, 5, 10, 15, 50, 100, 1000]
FindSumofTerms(N)

