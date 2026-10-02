def remove_duplicates(n):
    result = []

    for i in n:
        if i not in result:
            result.append(i)

    return result


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))
    print(remove_duplicates(numbers))
