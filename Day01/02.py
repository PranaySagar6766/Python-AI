i=20
j=10.4
k=3
print(id(i))
print(i)
print(type(i)) #<class 'int'>
print(j)
print(type(j)) #<class 'float'>

g=complex(i,k) #(20+3j)
print(g)
print(type(g)) #<class 'complex'>

c=True #/False
print(c)
print(type(c)) #<class 'bool'>
j='thedumbrepranav'
print(j)
print(type(j)) #<class 'str'>

l=[10,20,30]
print(l)
print(type(l)) #<class 'list'>

s={20,30}
print(s)
print(type(s)) #<class 'set'>

t=(10,20)
print(t)
print(type(t)) #<class 'tuple'>

d={'color':'blue'}
print(d)
print(type(d)) #<class 'dict'>

print("---------------")
###
# Mutable & Immutable
# Mutable- list,dict,set
# Immutable- string,int,float,complex,tuple,bool
# ###
l1=[10,20]
l2=[10,20] #mutable thats why created separtely to avoid reference confusion
print(l1==l2) #True
print(id(l1)) #different than l2 id
print(id(l2))
print(l1 is l2)  #False
print("---------------")

v=10
w=10 #immutable thats why same ref is returned for same val
    #if val changes new obj is created and ref is updated
print(id(v))
print(id(w))
print(id(v)==id(w)) #true
print(v==w)
print(v is w)
# name=input('Enter name')
# age=int(input('enter age'))
# print('name is',name,'age',age)
# #print('name is {} and age is {}',format(name, age))
# print(f'name is {name} and age is {age}')

num=4e6
print(num)
print(f'{num:.0f}')
print(f'{num:.0f}')
print(f'{num:.2f}')

#format
no=25
print(no)
print(f'{no:>10}')#moves right
print(f'{no:<10}')#moves left
print(f'{no:^10}')#center
print(f'{no:10}')#
print(f'{no:06}')# append zero to left

marks=0.75
print(f'{marks:0%}')#default percent
print(f'{marks:.0%}')# number after . tells digits after decimal
print(f'{marks:.2%}')






