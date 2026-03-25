nums = list(map(int , input("Enter number seperated by space: ").split()))
unique = sorted(set(nums) , reverse = True)

if len(unique) >= 2:
    print("Second largest number in the given list = " , unique[1])
else:
    print("Not enough unique elements")


