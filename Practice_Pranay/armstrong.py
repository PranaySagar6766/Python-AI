def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum( int(d) ** power for d in digits)
    return total == n

num = int(input("Enter your number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not a Armstrong number")