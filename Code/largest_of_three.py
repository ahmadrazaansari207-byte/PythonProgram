def largest(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
if __name__ == "__main__":
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=int(input("Enter 3rd number:"))
    result= largest(a,b,c)
    print("Largest=", result)