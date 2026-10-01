def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    print("Sum of digits is:", sum_of_digits(num))
