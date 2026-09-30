def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    return fact

if __name__=="__main__":
    num=int(input("Enter a number:"))
    result=factorial(num)
    print("Factorial=", result)