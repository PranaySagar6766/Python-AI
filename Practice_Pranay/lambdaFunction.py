# Lambda Function
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even Number using lambda Funtion: ", even)

# List Comprehension
even2 = [x for x in nums if x % 2 == 0]
print("Using List comprehension :", even2)