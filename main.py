from tkinter import Tk

from categorie.views import formulaire

if __name__ == "__main__":
    root = Tk()
    root.geometry('700x600')
    root.title('Enregistrement')
    formulaire(root)
    root.mainloop()