from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

path = 'fake_db/fake_db.json'
keys = ['age', 'breed']
db = pd.read_csv('fake_db/fake_db.csv')


class Dog:
    def __init__(self, name, age, breed, uri, author):
        self.name = name
        self.age = age
        self.breed = breed
        self.pic = uri
        self.category = author

    def display(self):
        print(self.name + ' | ' + self.breed + ': ' + str(self.age))


def csv_to_obj() -> list:
    dogs = []
    names = db['name']
    ages = db['age']
    breeds = db['breed']
    uris = db['uri']
    authors = db['author']
    for (name, age, breed, uri, author) in zip(names, ages, breeds, uris, authors):
        dogs.append(Dog(name, age, breed, uri, author))
        # print(name + ', ' + str(age) + ', ' + breed + ', ' + uri + ', ' + author)
    return dogs


def average(lst):
    return sum(lst) / len(lst)


def get_breeds():
    if db is not None:
        name = 'img.png'
        breeds = db['breed'].unique()
        for breed in breeds:
            print(breed)
        dogs = csv_to_obj()

        for breed in breeds:
            aux = []
            for dog in dogs:
                if dog.breed == breed:
                    aux.append(dog.age)
            print(aux)
            mu = average(aux)
            std = np.std(aux)
            x = np.linspace(mu - 3 * std, mu + 3 * std, 100)
            plt.plot(x, norm.pdf(x, mu, std), label=breed)
        plt.savefig('./img/' + name)
        plt.legend()
        plt.show()

        img = ImageTk.PhotoImage(Image.open('./img/' + name).resize((500, 500)))
        img_container.configure(image=img)
        img_container.image = img


root = Tk()
root.title('Graphic Dog Data')
root.geometry('500x500')
root.resizable(False, False)

button = ttk.Button(text='Calcular', command=get_breeds)
button.pack(pady=20)

img_container = Label(root)
img_container.pack(fill='both')

root.mainloop()

# eliminar por raza
