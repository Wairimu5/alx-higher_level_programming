#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

import sys

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

def already_exists(a, x, y):
    """Check that a queen does not already exist in that y value"""
    for i in range(x):
        if y == a[i][1]:
            return True
    return False

def reject(a, x, y):
    """Determine whether or not to reject the solution"""
    if already_exists(a, x, y):
        return False
    i = 0
    while i < x:
        if abs(a[i][1] - y) == abs(i - x):
            return False
        i += 1
    return True

def clear_a(a, x):
    """Clear the answers from the point of failure on"""
    for i in range(x, n):
        a[i][1] = None

def nqueens(a, x, n, solutions):
    """Recursive backtracking function to find the solution"""
    for y in range(n):
        clear_a(a, x)
        if reject(a, x, y):
            a[x][1] = y
            if x == n - 1:
                solutions.append(["".join(["Q" if x == 1 else "." for x in row]) for row in a])
            else:
                nqueens(a, x + 1, n, solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    a = []
    for i in range(n):
        a.append([i, None])
