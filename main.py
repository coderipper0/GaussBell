from tkinter import *
from tkinter import ttk
from enum import Enum
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os


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


def save_list(dogs):
    with open(path, 'w') as fake_db:
        json_data = json.dumps([dog.__dict__ for dog in dogs])
        fake_db.write(json_data)


def load_list():
    dogs = []
    with open(path, 'r') as fake_db:
        if os.stat(path).st_size != 0:
            json_data = json.load(fake_db)
            for data in json_data:
                dogs.append(Dog(**data))
            return dogs
        else:
            print('File is empty')
    return None


def load_data_file():
    dictionary = {}
    for key in keys:
        values = db[key]
        sub_dictionary = {}
        for value in values:
            if value in sub_dictionary:
                sub_dictionary[value] = sub_dictionary[value] + 1
            else:
                sub_dictionary[value] = 1
        dictionary[key] = sub_dictionary
    print(dictionary)


def csv_to_obj():
    dogs = []
    names = db['name']
    ages = db['age']
    breeds = db['breed']
    uris = db['uri']
    authors = db['author']
    for (name, age, breed, uri, author) in zip(names, ages, breeds, uris, authors):
        dogs.append(Dog(name, age, breed, uri, author))
        print(name + ', ' + str(age) + ', ' + breed + ', ' + uri + ', ' + author)


csv_to_obj()
load_data_file()

# root = Tk()
# frame = ttk.Frame(root, padding=10)
# frame.grid()
# # ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
# # ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.geometry('500x500')
# root.mainloop()
