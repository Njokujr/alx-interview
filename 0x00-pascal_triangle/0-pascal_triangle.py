#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        ValueError: If n is less than or equal to 0.

    Examples:
        >>> pascal_triangle(0)
        []
        
        >>> pascal_triangle(1)
        [[1]]
        
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row [1]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1]  # Leftmost element is always 1

        # Calculate the values for the current row
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)  # Rightmost element is always 1

        triangle.append(current_row)

    return triangle

