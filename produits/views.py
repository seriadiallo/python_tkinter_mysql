'''
la partie graphique de gestion des produits
-un formulaire d'enregistrement
-un tableau de tous les produits

'''
from tkinter import END, Frame, IntVar, StringVar, Tk, TclError
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.ttk import Button, Combobox, Entry, Label, Treeview

from .models import Produit
from categorie.models import Categorie

class ProduitView(Frame):


    def __init__(self, root):
        super().__init__(root)
        self.frameform = Frame(root)
        self.frametable = Frame(root)

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
                categorie = Categorie.getByName(self.categorie.get()) # recuperation de la categorie selectionnee
                values = self.nom.get(), self.quantite.get(), \
                    self.prix.get(), self.date_expiration.get(), categorie['id']
                val = Produit.create(*values)
                if val == 1:
                    showinfo("Succès", 'Enregistrement ok')
                    # vider les champs de saisi
                    self.nom.set('')
                    self.prix.set(0)
                    self.quantite.set(0)
                    self.date_expiration.set('')
                    self.categorie.set('')
                    # self.tree.insert('', END, values=values)
                else:
                    showerror('Erreur', "Une erreur est survenue")
            else:
                showwarning("Attention", "Vous devez bien remplir le formulaire avant")
        

        def getCategories():
            cts = Categorie.getAll()
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


        
    def table(self):
        Label(self.frametable, text='Liste des produits').pack()
        self.tree = Treeview(self.frametable)
        
        self.tree['columns'] = ('id', 'nom', 'quantite', 'prix', 'expiration', 'categorie')

        self.tree.column('id', width=30)
        self.tree.column('quantite', width=100)

        self.tree.heading('id', text='Id')
        self.tree.heading('nom', text='Nom')
        self.tree.heading('quantite', text='Quantite')
        self.tree.heading('prix', text='Prix')
        self.tree.heading('expiration', text='Expiration')
        self.tree.heading('categorie', text='Id Categorie')

        self.fill_table()
        self.tree.pack()
    
    def fill_table(self):
        produits = Produit.all()
        for index, produit in enumerate(produits):
            try:

                self.tree.insert('', produit['id'], index, values=(produit['id'], produit['nom'],
                produit['quantite'], produit['prix'],
                produit['date_expiration'], produit['id_categorie']))
            except TclError as exc:
                print('erreur lors de l\'ajout d\' une ligne')
                print(exc)


        