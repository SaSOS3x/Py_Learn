class Person:
    name = "Anonimus"

    def __init__(self, name:str, age:int):

        self.name = name
        self.age = age

    def __str__(self):

        return f"Person: {self.name}, Age: {self.age}"

    def display_info(self):

        print(self)

    
    