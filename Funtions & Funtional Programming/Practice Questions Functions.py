#Problem No. 1
# Define a function overlapping () that takes two lists and returns True if they have at
# least one member in common, False otherwise.


def overlapping(l1,l2):
    return bool(set(l1) & set(l2))

print(f"{overlapping([1, 2, 3, 4], [4, 5, 6, ])} : There is a Overlap")
print()

# Problem No. 2
#Write a Function that accepts list of verbs and return a dictionary with verb as
# key and its value as past participle as value
#Rules:
# 1] If a verb ends in 'e' drop the 'e' and add 'ing'
# 2] If the verb ends in 'ie' then replace 'ie' with 'y' and add ing at the end.


def make_ing_form(l1):
    result = {}
    for items in l1:
        if items[-2:] == "ie":
            result[items] = items[:-2] + "ying"
        elif items[-1] == 'e':
            result[items] = items[:-1] + "ing"
        else:
            result[items] = items + "ing"
    return result


verbs = ["make", "die", "run", "lie", "play"]
print(make_ing_form(verbs))
print()


# #Problem No. 3
# #make a Function which displays greetings when sent an argument as today's greeting.
# #Use Decorate the greeting so its displayed using uppercase.
# # Define the decorator
def uppercase_decorator(func):
    def wrapper(greeting):
        # Call the original function
        result = func(greeting)
        # Convert the result to uppercase
        return result.upper()
    return wrapper

# Apply the decorator
@uppercase_decorator
def display_greeting(greeting):
    return f"Today's greeting is: {greeting}"

print(display_greeting("Hello, have a great day!"))
print()


# #Problem no. 4
# #Create a series of n prime numbers and display the first 10.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2 , int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(n):
    primes = []
    nums = 2
    while len(primes) < n:
        if is_prime(nums):
            primes.append(nums)
        nums += 1
    return primes


prime_series = generate_prime(10)
print("First 10 prime numbers:", prime_series)
print()


#Problem no. 5
# 1. Find employees that know 'python'
# 2. Add a new skill - 'test' in skillset of all employees
# 3. Sort employees by skills
# for the given dictionary of employees
emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
            'Aditi': ['Python', 'PHP', 'Database']}

# #Find Emp with Skill python
filter_emp = list(filter(lambda emp: 'Python' in emp_data[emp], emp_data))
print(f"Emp that knows Python: \n{filter_emp}")
print()

#Add new skills 'test' for all emp
for emp in emp_data:
    emp_data[emp].append('test')
print(f"Added 'Test' skill for all emp: \n{emp_data}")
print()

#sort emp by skills
for emp in emp_data:
    emp_data[emp].sort()
print(f"Sorted Emp by Skills: \n{emp_data}")
print()


# Q.6
# Following data displays min/max/average temp for cities
# weather= [{'Mumbai' : [28, 30, 32]},.....]

# 1. Print the weather data
# 2. Print the city with maximum/min temp
# 3. Print all the cities that expereince min temp more than 30 degree
# 4. Create a dictionary to print 'City':'Avg temp'

weather = [
    {'Mumbai': [28, 34, 31]},
    {'Delhi': [20, 30, 25]},
    {'Bangalore': [18, 27, 22]},
    {'Chennai': [26, 33, 29]},
    {'Kolkata': [24, 32, 28]},
    {'Pune': [19, 29, 24]},
    {'Goa' : [33,36,34]},
    {'Jaipur' : [35,45,40]}

]
# 1. Print the weather data

for item in weather:
    for city , temps in item.items():
        print(f'City: {city}')
        print(f"Min Temp: {temps[0]} °C")
        print(f"Max Temp: {temps[1]} °C")
        print(f"Avg Temp: {temps[2]} °C")
        print('-' * 20)


# 2. Print the city with maximum/min temp
max_weather = max(weather , key = lambda temp: list(temp.values())[0][1])
print(f"Max Temp among the cities: {max_weather}" )
print()

# 3. Print all the cities that experience min temp more than 30 degree
min_temp = list(filter(lambda item: list(item.values())[0][0] > 30, weather))
for city in min_temp:
    for name, temps in city.items():
        print(f"{name} = Min Temp: {temps[0]}°C")
print()


# 4. Create a dictionary to print 'City':'Avg temp'
avg_temp_dict = {list(item.keys())[0]: list(item.values())[0][2] for item in weather}
print(f'City: Avg temp')
print(f"{avg_temp_dict}")