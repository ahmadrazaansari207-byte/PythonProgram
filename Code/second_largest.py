def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

if __name__ == "__main__":
    numbers = input("Enter numbers: ").split()
    numbers = [int(x) for x in numbers]
    print("Second largest number:", second_largest(numbers))
