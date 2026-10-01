def char_frequency(string):
    frequency = {}

    for char in string:
        if char != " ":
            frequency[char] = frequency.get(char, 0) + 1

    return frequency


if __name__ == "__main__":
    string = input("Enter a string: ")
    print(char_frequency(string))
