age=int(input('Enter your age'))
if age > 18:
    print('Permitted')
else:
    print('Not permitted')

gender = input('Enter your your gender')
if age > 18:
    if gender=='M':
        print('male')
    else:
        print('female')
else:
    print('Child')

if age>18 and gender=='M':
    print('male')
elif age>18 and gender=='F':
    print('female')
else:
    print('child')

marks = int(input('Enter marks'))
if 85<marks<100:
    print('A')
elif 70<marks<85:
    print('B')
elif 60<marks<70:
    print('C')
else:
    print('D')