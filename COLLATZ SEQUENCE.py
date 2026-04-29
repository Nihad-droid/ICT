""" Collatz Sequence is a sequence that checks the number if its odd or even.
 If it's even divide by 2. If it's odd multiply by 3 and add 1.
 Eventually you will always end up on 1!"""

try:
    def collatz(number):
        while number != 1:
            if number % 2 == 0:
                number /= 2
                print(int(number))
            else:
                number = number * 3 + 1
                print(int(number))


    while True:
        print("Enter number")
        entered_number = int(input())
        if entered_number > 1:
            collatz(entered_number)
            break
        else:
            print("enter integer greater than 1")
            continue

except ValueError:
    print("Please enter an integer value greater than 1.")
