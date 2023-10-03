#!/usr/bin/python3
def return_last_digit(number):
    last_digit = abs(number) % 10
    return last_digit

# Test the function
result = return_last_digit(98)
print(result)

result = return_last_digit(-98)
print(result)

result = return_last_digit(0)
print(result)
