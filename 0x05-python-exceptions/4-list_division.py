#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length  # Create a new list to store the division results
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            # Check if either of the elements is not an integer or float
            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                print("wrong type")
            else:
                result[i] = dividend / divisor
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return result
