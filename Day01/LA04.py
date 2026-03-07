#count even odd digits in number sum of digits
num=int(input("enter number:"))
sum=0
even=0
odd=0
while(num != 0):
    d=num%10
    sum=sum+d
    if d%2==0:
        even+=1
    else:
        odd+=1
    num=num//10
print(f'even:{even}')
print(f'odd:{odd}')
print(f'sum:{sum}')