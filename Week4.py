# CLASS AND OBJECT DEMONSTRATION
# num = int(10)  # Using the int() constructor
# print(f"Integer: {num}, Type: {type(num)}")

# String (str)
# text = str("Hello, World!")  # Using the str() constructor
# print(f"String: '{text}', Type: {type(text)}")

# # Float (float)
# pi = float(3.14159)  # Using the float() constructor
# print(f"Float: {pi}, Type: {type(pi)}")

# # List (list)
# my_list = list([1, 2, 3, 4])  # Using the list() constructor
# print(f"List: {my_list}, Type: {type(my_list)}")

# # Basic class definition
class Student:
    # The __init__ method (constructor) is called when a new object is created
    def __init__(self, name, gender, age, course):
        # Instance variables (properties)
        self.name = name
        self.gender = gender
        self.age = age
        self.course = course
    
    # Method (activity) - simulating a behavior of a student
    def studying(self):
        print(f"{self.name} is studying {self.course}.")

#     # Method - simulating the student's career aspiration
    def career(self):
        if self.course == "Computer Science":
            print(f"{self.name} is aspiring to become a Software Engineer.")
        else:
            print(f"{self.name} is aspiring to have a career in {self.course}.")


# # Creating an object (instance) of the Student class
student1 = Student("Alice", "Female", 22, "Computer Science")
student2 = Student("Bob", "Male", 24, "Physics")

# # Accessing methods
# student1.studying()
# student1.career()

# student2.studying()
# student2.career()


# # INHERITANCE DEMONSTRATION

# # Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# # Child class inheriting from Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        # Call the constructor of the parent class (Person)
        super().__init__(name, age)
        self.subject = subject

    # Method specific to Teacher
    def teach(self):
        super().greet()
        print(f"{self.name} is teaching {self.subject}.")

# # Creating an object of the Teacher class
teacher1 = Teacher("Dr. Smith", 45, "Mathematics")

# # # Accessing methods from both the parent class and the child class
# teacher1.greet()  # From the parent class (Person)
teacher1.teach()  # From the child class (Teacher)


# # MULTIPLE INHERITANCE DEMONSTRATION

# # Another parent class
class Employee:
    def __init__(self, job_title):
        self.job_title = job_title

    def work(self):
        print(f"Working as a {self.job_title}.")

# # Child class inheriting from both Person and Employee (Multiple Inheritance)
class WorkingStudent(Person, Employee):
    def __init__(self, name, age, job_title):
        Person.__init__(self, name, age)  # Initialize from Person class
        Employee.__init__(self, job_title)  # Initialize from Employee class

    def details(self):
        print(f"{self.name} is {self.age} years old and works as a {self.job_title}.")

# # Creating an object of the WorkingStudent class
working_student = WorkingStudent("Jane", 28, "Research Assistant")

# # Accessing methods from both parent classes
# working_student.greet()  # From Person class
# working_student.work()   # From Employee class
# working_student.details()  # Method from WorkingStudent class

student3 = Student("Dennis","Male",30,"Comp.Sci.")
person2 = Person("Ingatius",150)
person2.age
person3 = Person("Ingatius",30)
person3.age
# # PRACTICAL DEMONSTRATION OF isinstance() AND issubclass()

# Checking if an object is an instance of a class
print(isinstance(student1, Student))  # Output: True
print(isinstance(teacher1, Student))  # Output: False

# Checking if a class is a subclass of another
print(issubclass(Teacher, Person))  # Output: True
print(issubclass(WorkingStudent, Employee))  # Output: True
