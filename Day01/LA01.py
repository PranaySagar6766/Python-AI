#algo to print n! using for loop
num=int(input('ENTER NUMBER:'))
fact=1
for i in range(1,num+1):
    fact=fact*i

print(f'factorial ={fact}')