#swap 3 digit number
num=int(input("Enter Number :"))
rev=0


while(num != 0):
    rev=num%10+rev*10
    num=num//10
print(rev)