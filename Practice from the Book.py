tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', "Carol", "David"],
             ['dogs', 'cats', 'mouse', 'goose']]


def printtable(tableData):
    # Find the maximum width of each column
    colwidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colwidths[i] = max(len(item) for item in tableData[i])

    # Print the table row by row
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colwidths[col]), end=' ')
        print()


printtable(tableData)
