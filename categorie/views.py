from tkinter import *
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.ttk import *

from .models import  Categorie

class CategorieView(Frame):

    def __init__(self, root):
        super().__init__(root)
        # appel des methode pour le formulaire et le tableau
        self.formulaire(root)
        self.tableau(root)

    def formulaire(self, root):
        snom = StringVar()

        def save(): # pour la commande
            n = snom.get()
            if n != None and n != '':
                ligne = Categorie.create(n) # appel de la fonction qui permet de faire l'insertion dans la base de donnees
                if ligne == 1:
                    snom.set('') # supprimer le contenu de la zone de saisi
                    showinfo('Succes', 'Enregistrement effectué avec succès')
                    
                else:
                    showerror('Erreur', "Une erreur est survenue lors de l'enregistrement")

            else:
                showwarning("Attention", "Vous devez saisir avant d'enregistrer")

        Label(root, text='Gestion des catégoires').pack()
        frame = Frame(root)
        lnom = Label(frame, text='Nom')
        lnom.grid(row=1, column=0)
        
        
        nom = Entry(frame, textvariable=snom)
        nom.grid(row=1, column=1)

        button = Button(frame, text='Enregistrer', command=save)
        button.grid(row=2, column=1)

        frame.pack(side=TOP)



    def tableau(self, root):
        frame = Frame(root)
        Label(frame, text='Liste des catégories').grid(row=0, column=0, sticky='nesw', pady=40)
        tree = Treeview(frame)
        tree['columns'] = ('un', 'deux') # listes les index des colonnes du tableau

    # parametrer les colonnes
        tree.column('#0',width=40, minwidth=30,  anchor=CENTER)
        tree.column("un", width=150, minwidth=150, stretch=NO)
        tree.column("deux", width=400, minwidth=200)

    # ajout des entete du tableau
        tree.heading('#0', text='N°')
        tree.heading("un", text="Identifient",anchor=W)
        tree.heading("deux", text="Nom",anchor=W)

    # insertion des lignes du tableau
        
        categories = Categorie.getAll() # répération de toutes les categories dans la base de données
        for index, categorie in enumerate(categories, start=1):
            tree.insert('', index, text=index, values=(categorie['id'], categorie['nom']))

        tree.grid(row=1, column=0) # afficher le tableau sur le frame
        frame.pack() # affichage du frame sur la fenetre



