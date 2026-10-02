def find_duplicates(num):
    duplicates = []
    
    for i in num:
        if num.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    
    return duplicates


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))

    print("Duplicate elements:", find_duplicates(numbers))
