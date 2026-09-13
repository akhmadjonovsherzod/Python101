#3 built in decorators for classes

# @classmethod

class Person:
    origin_country = "USA"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, words):
        print(f"{self.name} speaks: {words}")

    @classmethod
    def change_origin_country(cls, new_country):
        cls.origin_country = new_country
        print(cls.origin_country)

# @staticmethod

class Person:
    origin_country = "USA"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def change_origin_country(cls, new_country):
        cls.origin_country = new_country
        print(cls.origin_country)

    @staticmethod
    def is_adult(age):
        return age > 18

print(Person.is_adult(19))

print(Person.is_adult(17))

# @property

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

obj = Person("Alex", "Johnson")
print(obj.email)
obj.first_name = "Bob"
print(obj.email)

#abstract classes

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        raise NotImplementedError("You have to implement eat() method")

class Dog(Animal):
    pass

#now it is possible to override the method eat()

obje = Dog()
obje.eat()