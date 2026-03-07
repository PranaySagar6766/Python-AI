num=int(input('Enter number'))
if num<2:
    print('Number is not prime')
for i in range(2,num):
    if num%i==0:
        print('Number is Not prime')
        break
    else:
        print('Number is Prime')

flag = True
