def prime_number(n):
    if n < 2:
        return "The given no. is not Prime"

    for i in range (2, n):
        if n % i == 0:
            return "The given no. is not Prime"
    else:
        return "The given no. is Prime"

if __name__=="__main__":
    num = int(input("Enter a number:"))
    print(prime_number(num))