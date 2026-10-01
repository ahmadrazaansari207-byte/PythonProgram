def palindrome_number(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if palindrome_number(num):
        print("Palindrome number")
    else:
        print("Not a palindrome number")
