def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Add the middle values of the row by summing two adjacent numbers from the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with 1
        row.append(1)
        triangle.append(row)

    return triangle
