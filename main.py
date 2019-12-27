from tkinter import Tk

from categorie.views import formulaire, tableau
from produits.views import ProduitView

if __name__ == "__main__":
    root = Tk()
    root.geometry('700x600')
    root.title('GESTON DE STOCK')
    # formulaire(root)
    # tableau(root)

    pview = ProduitView(root)
    pview.form()



    root.mainloop()