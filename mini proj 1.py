import random

def guess_the_number():
    lb = 0
    ub = int(input("Enter the upper bound: "))
    num = random.randint(lb, ub)
    c = 0
    while True:
        g = int(input("Enter your guess: "))
        c += 1
        if g < num:
            print("Its lower than the number. Try again.")
        elif g > num:
            print("Its Above the number. Try again.")
        else:
            print("Congrats!!! You got the number ",num," in ",c,"attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
