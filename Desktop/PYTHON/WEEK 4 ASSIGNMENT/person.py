class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def intoduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and my gender is {self.gender}.")


# Creating an instance of the person class

person1 = person("Dan",25,"Male")

# calling the introduce method to display the person's information.

person1.intoduce()