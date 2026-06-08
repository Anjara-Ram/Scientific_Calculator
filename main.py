import tkinter as tk

class ScientificCalculator:

    def __init__(self):
        # Fenetre principale
        self.root = tk.Tk()
        self.root.title("Calculatrice Scientifique")
        self.root.geometry("600x700")
        self.root.resizable(False,False)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ScientificCalculator()
    app.run()

