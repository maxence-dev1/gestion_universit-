import tkinter as tk

def show_frame(frame):
    frame.tkraise()  # Affiche le frame passé en argument

root = tk.Tk()
root.geometry("400x300")

# Création des frames (pages)
page1 = tk.Frame(root)
page2 = tk.Frame(root)

for frame in (page1, page2):
    frame.grid(row=0, column=0, sticky="nsew")  # Superpose les frames

# Contenu de la page 1
tk.Label(page1, text="Page 1", font=("Arial", 18)).pack(pady=20)
tk.Button(page1, text="Aller à Page 2", command=lambda: show_frame(page2)).pack()

# Contenu de la page 2
tk.Label(page2, text="Page 2", font=("Arial", 18)).pack(pady=20)
tk.Button(page2, text="Retour à Page 1", command=lambda: show_frame(page1)).pack()

show_frame(page1)  # Affiche la première page par défaut

root.mainloop()
