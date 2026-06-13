class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print()


student1 = Student("Kavya", 20, "CSE")
student2 = Student("Rahul", 21, "ECE")
student3 = Student("Priya", 20, "IT")

student1.display_info()
student2.display_info()
student3.display_info()