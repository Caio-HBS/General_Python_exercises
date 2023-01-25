class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print('Hello, my name is', self.name, 'and I am', self.age, 'years old.')

    