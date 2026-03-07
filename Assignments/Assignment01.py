#problem No.1
#write a python function that takes a list of words and returns the length of the longest one.
# Function for max len of words in a list
def longest_word(words):
    # if not words covers corner case of an empty string.
    if not words:
        return 0
    return max(words , key = len)


print('Enter list of words: ')
word = input().split()
print(word)
print(f"Longest word Lenght is: {len(longest_word(word))}\n" )
print()

#Problem no.2
# write a python program to remove duplicates from a list

l = input("Enter List of words: ").split()
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)

print(l2)
print()


#Problem No. 3
#Create a list of books
#perform Following operations
#1. add new book with price
#2. Remove entry for a book
#3. Update price for a book
#4. Sort the list by book name
#5. Sort the list by price
#6. print the book with max and min functions of python
book_list = [['Java8' , 700] , ['Python for beginners' , 500] , ['C++' , 600] , ['Let us C' , 400]]
print ( book_list)
book_list.insert(1 , ['AI' , 1000])
print (book_list.insert)
del book_list [2]
print(book_list)
book_list[ 1 ][ 1 ] = 550
book_list.sort (key = lambda k : k [0])
print ( book_list)
book_list.sort (key = lambda x : x[1])
print (book_list)
max_price = max (price[1] for price in book_list)

min_price = min (price[1] for price in book_list)
print(max_price)
print(min_price)
print()


#Problem 4
#Write a program to compute element-wise sum of given tuple using zip() Function
#Orignal Tuple
#(1,2,3,4)
#(3,5,2,1)
#(2,2,3,1)
#---------Element-wise Addition of tuple-------
#(6,9,8,6)

t1 = (1,2,3,4)
t2 = (3,5,2,1)
t3 = (2,2,3,1)

#use List comprehension
result = tuple(a + b + c for a,b,c in zip(t1,t2,t3))
print("---------Element-wise Addition of tuple-------")
print(result)
print()


#Problem No. 5
# Write a program to find repeated elements of a tuple
t1 = (1,2,2,4,5,1)
repeated = []
for i in t1:
    if t1.count(i) > 1 and i not in repeated:
        repeated.append(i)

print("Repeated elements in the tuple are : ", tuple(repeated))


