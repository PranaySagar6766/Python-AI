fruits = {'mango' , 'banana' , 'orange' , 'watermelon', 'grape' , 'guava', 'pineapple'}
fruits1 = {'mango' , 'banana' , 'strawberry','litchi','chiku'}
print(fruits)
print(fruits1)
print()

for fruit in fruits:
    print(fruit)

print()

print('mango' in fruits)
print('pomegranate' not in fruits)
print(fruits)

print()

fruits.add('kiwi')
print(fruits)

print()

fruits.remove('mango')

fruits.discard('mango')
print(fruits)

print()

fruits.pop()
print(fruits)

print()

d_fruits = fruits.difference(fruits1)
print(d_fruits)
print()

s_fruits = fruits.symmetric_difference(fruits1)
print(s_fruits)
print()

s1 ={'apple' , 'mango' , 'grapes'}
s2 = {'apple' , 'guava'}
print ( s1 | s2)

u_fruits = fruits | fruits1
u1_fruits = fruits.union(fruits1)
print(u_fruits)
print(u1_fruits)





