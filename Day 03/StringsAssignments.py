# Problem no.1
# write a program that asks a user how many days are in a particular month and
# what day of the week the month begins on
# And then prints the calendar for that month.
month = input("Enter your month: ")
number_of_days = int(input(f"Enter number of days are in  {month} :"))
Weekday = int(input("Enter the day of the week from which this month begins: "))

# Default Calender Layout
days = " M  T  W  T  F  S  S"
print(days)

# No. of space before starting the month
print("   " * (Weekday - 1), end="")

# Printing the number of days in order
for i in range(1, number_of_days + 1):
    list1 = str(i)
    print(f"{i:< 3}", end="")
    if (i + Weekday - 1) % 7 == 0:
        print()
print()
print()

# -----------------------------------------

# Problem No.2
str1 = input("Enter a string : ")
count = 0
flag = False
for char in str1:
    if char.isupper():
        count += 1
    flag = True
if count == len(str1):
    flag = True
else:
    flag = False
print(flag)
print()
# -----------------------------------------
# Problem 3
text = input("Enter a string: ")
clean_text = "".join(char.lower() for char in text if char.isalpha())
if clean_text == clean_text[:: -1]:
    print(f"Yes, it is palindrome : {clean_text}")
else:
    print("Not a palindrome")
