#!/usr/bin/python3
"""
Defines Pascal's triangle that creates a list of lists.
"""


def pascal_triangle(n):
    """
    Defines Pascal's triangle for 'n' levels.
    """
    if n <= 0:
        return []
    current_row = []
    result = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(current_row[j] + current_row[j - 1])
        current_row = row
        result.append(row)
    return result
