# Birincisi Salam

legal_rows = ['1','2','3','4','5','6','7','8']
legal_columns = ['a','b','c','d','e','f','g','h']

while True:
    coordinate = input("Koordinati daxil edin")
    row = coordinate[1]
    column = coordinate[0]
    if row not in legal_rows or column not in legal_columns:
        print("A1-H8 arasi secin")
        continue
    break

row_index = legal_rows.index(row)
column_index = legal_columns.index(column)

if (row_index % 2 == 0) and (column_index % 2 == 0):
    print("Xana Qaradir")
else:
    print("Xana Agdir")

