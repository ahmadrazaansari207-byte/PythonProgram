def pos_neg_zero(n):
    if n>0:
        return "The given no. is Positive"
    elif n<0:
        return "The given no. is Negative"
    else:
        return "The given no. is Zero"

if __name__=="__main__":
    num=int(input("Enter a number:"))
    print(pos_neg_zero(num))