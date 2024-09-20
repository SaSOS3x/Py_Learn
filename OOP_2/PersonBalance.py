import Person

class PersonBalance(Person.Person):

    def __init__(self, obj:Person.Person):

        super().__init__(obj.name, obj.age)

        self.__balance = 0

        print(f"Create balance for person: {self.name}, Age: {self.age}")

    def __str__(self):

        return f"Person: {self.name} balance: {self.__balance}"

    def display_info(self):

        super().display_info()

    def pay(self, sum:float, agree:bool):
        
        if agree == True:

            if (self.__balance - sum) > 0:

                self.__balance = self.__balance - sum
                print(f"Operation succesful, operation sum: {sum}")

            else:
                print(f"{self.name} balance not enough money")

        else:
            print(f"Operation is not agree")

        print(f"{self.name} balance is: {self.__balance}")

    def earn(self, sum:float, agree:bool):

        if agree == True:

            self.__balance = self.__balance + sum
            print(f"Operation succesful, operation sum: {sum}")

        else:
            print(f"Operation is not agree")

        print(f"{self.name} balance is: {self.__balance}")