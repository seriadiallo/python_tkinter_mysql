from tkinter import *
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.ttk import *

from .models import  create


def formulaire(root):
    snom = StringVar()

    def save(): # pour la commande
        n = snom.get()
        if n != None and n != '':
            ligne = create(n)
            if ligne == 1:
                snom.set('')
                showinfo('Succes', 'Enregistrement effectué avec succès')
            else:
                showerror('Erreur', "Une erreur est survenue lors de l'enregistrement")

        else:
            showwarning("Attention", "Vous devez saisir avant d'enregistrer")

    lnom = Label(root, text='Nom')
    lnom.grid(row=1, column=0)
    
    
    nom = Entry(root, textvariable=snom)
    nom.grid(row=1, column=1)

    button = Button(root, text='Enregistrer', command=save)
    button.grid(row=2, column=1)



if __name__ == "__main__":
    root = Tk()
    root.geometry('700x600')
    root.title('Enregistrement')
    formulaire(root)
    root.mainloop()