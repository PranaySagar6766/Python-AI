#find prime number in range
start=int(input('Enter starting number : '))
end=int(input('Enter ending number : '))

for i in range (start,end+1):
    if i==1:
        continue
    flag=True
    for j in range (2,i):
        if(i%j==0):
            flag=False
    if flag==True:
        print(i)

# for i in range(start, end+1):
#     if i==1:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             break
#         print(i)