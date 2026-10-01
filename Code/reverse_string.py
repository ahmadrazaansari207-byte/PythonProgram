def reverse_string(text):
    reversed_string = ""

    for char in text:
        reversed_string = char + reversed_string

    return reversed_string


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed string:", reverse_string(text))