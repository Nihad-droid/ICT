def generate_pascals_triangle(n):
    pascal_triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
        row.append(1)  # End each row with 1
        pascal_triangle.append(row)
    return pascal_triangle


# Example usage
n = int(input("Enter number of rows: "))
triangle = generate_pascals_triangle(n)

for row in triangle:
    print(' '.join(map(str, row)))
