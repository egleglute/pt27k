# Create a Calculator class with main functionality: add, divide, multiply, subtract , etc.. Initiate class and show up some calculations.

# class Calculator:

#     def dalyba(self, number1: int, number2: int) -> float:
#         return number1 / number2
#     def daugyba(self, number1: int, number2: int) -> float:
#         return number1 * number2
#     def pliusavimas(self, number1: int, number2: int) -> int:
#         return number1 + number2
#     def minusavimas(self, number1: int, number2: int) -> int:
#         return number1 - number2
    
# number1 = int(input("numeris1:  "))
# number2 = int(input("numeris2:  "))        
# calculator = Calculator()
# rezultatas = calculator.dalyba(number1, number2)
# print(rezultatas)
   
# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.
# class Employee:
#     def __init__(self, name: str, last_name: str) -> None:
#         self.name = name
#         self.last_name = last_name
    
#     def fullname(self) -> None:
#         print(f"{self.name} {self.last_name}")
#     def email(self) -> None:
#         print(f"{self.name.lower()}.{self.last_name.lower()}@company.com")

# employee1 = Employee("Tomas", "Rukauskis")
# employee1.fullname()
# employee1.email()

# example:
# # class Person:
#     def __init__(self, name: str, age: int = 0) -> None:
#         self.name = name
#         self.age = age

#     def travel(self):
#         print(f"{self.name} is walking...")

#     def say_hello(self):
#         print(f"{self.name} says Hello!")


# class Driver(Person):
#     def __init__(self, name: str, car: str, age: int = 0) -> None:
#         super().__init__(name, age)
#         self.car = car

#     def travel(self):
#         print(f"{self.name} is driving a car and it's {self.car}... much faster than walking")




# person1 = Person("Tom", 40)
# person2 = Driver("Antanas", "Opel", 25)

# person1.say_hello()
# person1.travel()
# person2.say_hello()
# person2.travel()

# Create a Book class that has two attributes:

# title
# author
# and two methods:

# A method named .get_title() that returns: "Title: " + the instance title.
# A method named .get_author() that returns: "Author: " + the instance author.
# and instantiate this class by creating 3 new books:

# Pride and Prejudice - Jane Austen (PP)
# Hamlet - William Shakespeare (H)
# War and Peace - Leo Tolstoy (WP)
# The name of the new instances should be pride_and_prejudice, hamlet, and war_and_peace, respectively. For instance, if I instantiated the following book using this Book class:

# Harry Potter - J.K. Rowling (harry_potter)
# I would get the following attributes and methods:

# harry_potter.title ➞ "Harry Potter"
# harry_potter.author ➞ "J.K. Rowling"
# harry_potter.get_title() ➞ "Title: Harry Potter"
# harry_potter.get_author() ➞ "Author: J.K. Rowling"

# class Books:
#     def __init__(self, title: str, author: str) -> None:
#         self.title = title
#         self.author = author
#     def get_title(self):
#         print(f"Title: {self.title}")
#     def get_author(self):
#         print(f"Author: {self.author}")

# pride_and_prejudice = Books("Pride and Prejudice", "Jane Austen")
# hamlet = Books("Hamlet", "William Shakespeare")
# war_and_peace = Books("War and Peace", "Leo Tolstoy")

# print(pride_and_prejudice.author)
# print(pride_and_prejudice.title)
# pride_and_prejudice.get_title()
# pride_and_prejudice.get_author()

# A country can be said as being big if it is:

# Big in terms of population.
# Big in terms of area.
# Add to the Country class so that it contains the attribute is_big. Set it to True if either criteria are met:

# Population is greater than 20 million.
# Area is larger than 3 million square km.
# Also, create a method which compares a country's population density to another country object. Return a string in the following format:

# {country} has a {smaller / larger} population density than {other_country}
# Examples:

# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)

# australia.is_big ➞ True
# andorra.is_big ➞ False
# andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"

class Country:
    def __init__(self, name: str, population: int, area: int) -> None:
        self.name = name
        self.population = population
        self.area = area
    def is_big(self):
        if self.population > 20000000 and self.area > 3000:
            print("True")
        else:
            print("False")
    def compare_pd(self):
        if australia.population > andorra.population:
            print("Australia has a larger population density than Andorra.")

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
australia.is_big()
andorra.is_big()
andorra.compare_pd()