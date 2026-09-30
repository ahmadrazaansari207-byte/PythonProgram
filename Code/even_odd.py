def even_odd(n):
    if n%2==0:
        return f"The given no. {n} is even"
    else:
        return f"The given no. {n} is odd"

if __name__ == "__main__":
    num=int(input("Enter a number:"))
    print(even_odd(num))