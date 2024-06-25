import math
def isps(n):
    root = int(math.sqrt(n))
    if root * root == n:
        return n

def count(begin, end):
    c = 0
    for i in range(begin, end + 1):
        if isps(i):
            c += 1
    return c

if __name__ == "__main__":
    # Take input from the user
    begin = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    res = count(begin, end)
    print("The number of perfect square numbers in the range",begin ,"to",end,"is:", res)
