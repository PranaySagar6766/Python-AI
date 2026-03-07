emp_data = {'Name' : 'Anhad',
            'Age' : 23,
            'PhoneNo.' : 9037712381,
            'salary' : 80000,
            'skills' : 'python , java, C++ ,Rust'}


capitals = {'India' : 'New Delhi',
            'UK' : 'London',
            'France' : 'Paris',
            'Japan' : 'Tokyo'}

#Prints value based on keys
print(capitals['UK'])

#for loop in dict
for key , value in capitals.items():
    print(f'{key} - {value}')

for key in capitals.keys():
    print(f'{key} - {capitals[key]}')
    print(f'{key} - {capitals.get(key)}')

for value in capitals.values():
        print(value)



