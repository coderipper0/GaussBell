class Dog:
    def __init__(self, name, age, breed, uri, author):
        self.name = name
        self.age = age
        self.breed = breed
        self.pic = uri
        self.category = author

    def display(self):
        print(self.name + ' | ' + self.breed + ': ' + str(self.age))