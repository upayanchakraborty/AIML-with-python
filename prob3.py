def primeCheck(n):
    for i in range(2,n):
        if n%i==0:
            break
        else:
            if n>1:
                return "Prime"
    return "Not Prime"        

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(num,"is",primeCheck(num))
