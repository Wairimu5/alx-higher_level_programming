#!/usr/bin/python3
"""
this is  the "append_write function"
"""


def append_write(filename="", text=""):
    """Returns the number of characters appended"""
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            return f.write(text)
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


if __name__ == "__main":
    nb_characters = append_write("my_file.txt", "This is a new line.\n")
    print(nb_characters)
