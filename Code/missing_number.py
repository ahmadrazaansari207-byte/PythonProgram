def missing_number(num):
    n = len(num) + 1
    total = n * (n + 1) // 2
    current_sum = 0
    
    for i in num:
        current_sum += i

    return total - current_sum


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))

    print("Missing number:", missing_number(numbers))
