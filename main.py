from tkinter import Tk

from categorie.views import CategorieView
from produits.views import ProduitView

if __name__ == "__main__":
    root = Tk()
    root.geometry('700x600')
    root.title('GESTON DE STOCK')

    CategorieView(root)
    

    # pview = ProduitView(root)
    # pview.form()
    # pview.table()



    root.mainloop()