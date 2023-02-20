from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style

from numpy import ndarray
from pandas import DataFrame
from pandas.errors import EmptyDataError
from ttkwidgets import CheckboxTreeview
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from models.dog import Dog


def csv_to_obj() -> list:
    dogs: list = []
    names: DataFrame = db['name']
    ages: DataFrame = db['age']
    breeds: DataFrame = db['breed']
    uris: DataFrame = db['uri']
    authors: DataFrame = db['author']
    for (name, age, breed, uri, author) in zip(names, ages, breeds, uris, authors):
        dogs.append(Dog(name, age, breed, uri, author))
    return dogs


def average(lst) -> float:
    return sum(lst) / len(lst)


def load_breeds() -> None:
    global all_breeds
    if db is not None:
        all_breeds = db['breed'].unique()


def execute() -> None:
    dogs: list = csv_to_obj()

    for breed in tree.get_checked():
        aux: list = []
        for dog in dogs:
            if dog.breed == breed:
                aux.append(dog.age)

        # Average.
        avg: float = average(aux)
        # Standard Deviation.
        sd: ndarray = np.std(aux)
        # It is used to create an evenly spaced sequence in a specified interval.
        x: ndarray = np.linspace(avg - 3 * sd, avg + 3 * sd, 100)

        plt.plot(x, norm.pdf(x, avg, sd), label=breed)
    plt.legend()
    plt.show()


def check_action() -> None:
    global all_checked
    if all_checked:
        tree.uncheck_all()
        action_btn.config(text="Marcar todos")
    else:
        tree.check_all()
        action_btn.config(text="Desmarcar todos")
    all_checked = not all_checked


def load_breed_boxes():
    x: int = 0
    for key in all_breeds:
        tree.insert(parent="", index="end", iid=key, text=key, tags=("checked",))
        x += 1


try:
    db: DataFrame = pd.read_csv('fake_db/fake_db.csv')
except FileNotFoundError:
    messagebox.showinfo(message="Archivo no encontrado", title="Error!")
    print('Archivo no encontrado')
    exit()
except EmptyDataError:
    messagebox.showinfo(message="Archivo vacio", title="Error!")
    print('Archivo vacio')
    exit()

all_checked: bool = True
all_breeds: list = []

root: Tk = Tk()
root.title('Graphic Dog Data')
root.geometry('500x500')
root.resizable(False, False)

frame: Frame = Frame(root)
frame.pack(pady=10, fill=X, side=TOP)

execute_btn: Button = Button(frame, text='Calcular', width=20, command=execute)
action_btn: Button = Button(frame, text='Desmarcar todos', width=20, command=check_action)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

execute_btn.grid(row=0, column=0)
action_btn.grid(row=0, column=1)

tree: CheckboxTreeview = CheckboxTreeview(root)
scroll_bar: Scrollbar = Scrollbar(root, orient="vertical", command=tree.yview)
scroll_bar.place(x=500 - 16, y=45, height=460)
tree.configure(yscrollcommand=scroll_bar.set)
tree.pack(fill=BOTH, expand=1)

load_breeds()
load_breed_boxes()

root.mainloop()
