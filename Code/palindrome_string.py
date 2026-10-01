def palindrome_string(string):
    if string == string[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(palindrome_string(string))