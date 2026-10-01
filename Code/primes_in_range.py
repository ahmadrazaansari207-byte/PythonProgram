def primes_in_range(start, end):
    primes=[]

    for num in range(start, end + 1):
        if num < 2:
            continue

        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes


if __name__ == "__main__":
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    print(primes_in_range(start, end))