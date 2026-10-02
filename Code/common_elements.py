def common_elements(list1, list2):
    result = []

    for i in list1:
        if i in list2 and i not in result:
            result.append(i)

    return result


if __name__ == "__main__":
    list1 = list(map(int, input("Enter first list: ").split()))
    list2 = list(map(int, input("Enter second list: ").split()))

    print(common_elements(list1, list2))
