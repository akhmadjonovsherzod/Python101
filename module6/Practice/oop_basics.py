#to define a class

class Person:

    def __init__(self, name, age, country, occupation):
        self.name = name
        self.age = age
        self. country = country
        self.occupation = occupation

Alice = Person("Alice", 25, "USA", "Student")

print(f"Name: {Alice.name}, Age: {Alice.age}, Country: {Alice.country}, Occupation: {Alice.occupation}")

#abstraction - generalizing the object usage without needing the understanding of its core functionalities, like knowing the usage of the car
#encapsulation - bundling the data/methods into single unit or hiding the object's data, restricting
#polymorphism - use of a single type entity (method, operator or object) to represent different types in different scenarios
#inheritance - basing another object upon the other one, inherits the similar method/data in addition to its own

class Person:
   origin_country = "USA"

   def __init__(self, name, age, gender):
     self.name = name
     self.age = age
     self.gender = gender

   def speak(self, words):
     print(f"{self.name} speaks: {words}")


class Employee(Person):
   def __init__(self, name, age, gender, salary, job_title):
     super().__init__(name, age, gender)
     self.salary = salary
     self.job_title = job_title

   def display_info(self):
     print(f"Employee {self.name} works as a {self.job_title}")

print(issubclass(Employee, Person)) #returns true, if the class in the first argument is inheriting the class in the second

#data/information hiding

#Python has the 2 types of data/information hiding simulation mechanisms - Private and Protected

# _ before the data means, protected, while __ means private

class Car:
    def __init__(self, brand, type):
        self.__brand = brand
        self._type = type

#to access protected, obj._argument
#to access private, obj._Class_Name__argument

#mro, works from left to right, priority

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())