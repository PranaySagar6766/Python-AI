# class Car:
#     count = 0
#     def __init__ (self , make , model, price , segment = "Economy"):
#         Car.count += 1
#         self.make = make
#         self.model = model
#         self.price = price
#         self.segment = segment
#         def calculate_premium(self,tenure):
#             if self._segment == "Economy":
#                 return self.price * tenure * 0.05
#             else:
#                 return self.price * tenure * 0.01




class Student :
    #__init__ is used to initialize attributes of a Class.
    def __init__(self,rollno,student_name, marks):
        #Variables to store values of attributes
        self.rollno = rollno
        self.student_name = student_name
        self.marks = marks

    #__str__ is used to return the values of attributes in String format
    def __str__(self):
        return (f"{self.rollno},{self.student_name}")

    #Method for Gpa Calculation
    def calculate_gpa(self):
        m1, m2, m3 = self.marks
        gpa = (1/3) * m1 +(1/2) *m2 + (1/4) *m3
        return gpa


students = [Student(1, "Anhad" , [50,100,50]),
            Student(10, "Pranay", [100, 100, 150]),
            Student(11, "A", [100, 100, 150]),
            Student(12, "B", [100, 100, 150]),
            Student(13, "C", [100, 100, 150])]

#priting all the students
print("\nALL Students:")
for i in students:
    print(i)
print()

#List comprehension for searching by roll no
roll_no = int (input("enter your rollno.: "))
op = [print(i) for i in students if i.rollno == roll_no]
print()

#Lambda function to sort students by student_name
sorted_students = sorted(students , key = lambda s : s.student_name)

#Printing sorted students with their GPA
print("Students sorted by name:")
for stu in sorted_students:
    print(f"{stu} → GPA: {stu.calculate_gpa()}")