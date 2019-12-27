'''
la partie graphique de gestion des produits
-un formulaire d'enregistrement
-un tableau de tous les produits

'''
from tkinter import Frame, IntVar, StringVar, Tk
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.ttk import Button, Combobox, Entry, Label, Treeview

from .models import Produit
from categorie.models import getAll, getByName

class ProduitView(Frame):


    def __init__(self, root):
        super().__init__(root)
        self.frameform = Frame(root)
        self.frametable = Frame(root)
        self.table = Treeview(self.frametable)

        self.frameform.pack()
        self.frametable.pack()

        self.nom = StringVar()
        self.prix = IntVar()
        self.quantite = IntVar()
        self.date_expiration = StringVar()
        self.categorie = StringVar()

    
    def form(self):

        def save():

            
            
            if self.nom.get() is not '' and self.quantite.get() != '' and self.categorie.get() != '':
                categorie = getByName(self.categorie.get()) # recuperation de la categorie selectionnee
                val = Produit.create(self.nom.get(), self.quantite.get(), 
                self.prix.get(), self.date_expiration.get(), categorie['id'])
                if val == 1:
                    showinfo("Succès", 'Enregistrement ok')
                    # vider les champs de saisi
                    self.nom.set('')
                    self.prix.set(0)
                    self.quantite.set(0)
                    self.date_expiration.set('')
                    self.categorie.set('')
                else:
                    showerror('Erreur', "Une erreur est survenue")
            else:
                showwarning("Attention", "Vous devez bien remplir le formulaire avant")
        

        def getCategories():
            cts = getAll()
            t = []
            for ct in cts:
                t.append(ct['nom'])
            return t


            

        Label(self.frameform, text='Formulaire d\'enregistrement').grid(row=0, column=1)
        Label(self.frameform, text='Nom').grid(row=1, column=0)
        Entry(self.frameform, textvariable=self.nom).grid(row=1, column=1, pady=5)

        Label(self.frameform, text='Quantite').grid(row=2, column=0)
        Entry(self.frameform, textvariable=self.quantite).grid(row=2, column=1, pady=5)

        Label(self.frameform, text='Prix').grid(row=3, column=0)
        Entry(self.frameform, textvariable=self.prix).grid(row=3, column=1, pady=5)

        Label(self.frameform, text='Date Expiration').grid(row=4, column=0)
        Entry(self.frameform, textvariable=self.date_expiration).grid(row=4, column=1, pady=5)

        Label(self.frameform, text='Categorie').grid(row=5, column=0)
        Combobox(self.frameform, textvariable=self.categorie,
        values=getCategories(),
        ).grid(row=5, column=1, pady=5)

        Button(self.frameform, text='Enregistrer', command=save).grid(row=6, column=1, sticky='ne')


        
