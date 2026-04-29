#
# Create a christmas tree for the given amount of height
#
#     *
#    ***
#   *****
#  *******
# *********
#     *
#


def tree(height):
    length = height * 2 - 1
    x = 1
    for i in range(1, height + 1):
        print(("*" * x).center(length))
        x += 2
    print("*".center(length))


desired_height = int(input("Enter the height of your tree\n"))

tree(desired_height)
