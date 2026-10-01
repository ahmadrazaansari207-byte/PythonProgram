def fibonacci_series(n):
    if n<=0:
        return "Enter a positive number"
    a=0
    b=1
    series=""
    for i in range(n):
        series+=str(a)+" "
        a, b=b, a+b
    return series

if __name__=="__main__":
    num=int(input("Enter number of terms:"))
    print(fibonacci_series(num))