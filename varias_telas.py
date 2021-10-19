from tkinter import *

class Jan2(Toplevel):
    def __init__(self, original):
        self.frame_original = original
        Toplevel.__init__(self)
        self.widgets()

    def widgets(self):
        btn = Button(self, text='Voltar', command=self.onClose)
        btn.pack()

    def onClose(self):
        self.destroy()
        self.frame_original.show()



class App:
    def __init__(self):
        self.root = root
        self.widgets()

        root.mainloop()
    def widgets(self):
        btn = Button(self.root, text='Jan2', command=self.entra_jan2)
        btn.pack()

    def entra_jan2(self):
        self.subFrame = Jan2(self)
        self.hide()
    def hide(self):
        self.root.withdraw()
    def show(self):
        self.root.update()
        self.root.deiconify()
# Programa Principal
root = Tk()
App()