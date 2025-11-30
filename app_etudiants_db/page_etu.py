import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import op

def run(id):
    # Données de l'élève
    photo_path = op.get_picture_by_id(id)
    nom = op.get_name_by_id(id)
    prenom = op.get_firstname_by_id(id)
    date_naissance = op.get_birthday_by_id(id)
    id_eleve = id
    notes = op.get_all_grades(id)
    print("notes")

    # Fenêtre principale
    window = tk.Toplevel()
    window.title("Informations de l'élève")

    # Chargement et affichage de la photo
    image = Image.open(photo_path)
    image = image.resize((150, 150))  # Redimensionner l'image
    photo = ImageTk.PhotoImage(image)

    photo_label = tk.Label(window, image=photo)
    photo_label.image = photo  # Garder une référence pour éviter la suppression
    photo_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

    # Informations générales
    infos = [
        f"Nom : {nom}",
        f"Prénom : {prenom}",
        f"Date de naissance : {date_naissance}",
        f"ID : {id_eleve}"
    ]
    for i, info in enumerate(infos):
        tk.Label(window, text=info, font=("Arial", 12)).grid(row=i, column=1, sticky="w", padx=10, pady=5)

    # Tableau des notes
    frame_notes = ttk.Frame(window)
    frame_notes.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    tree = ttk.Treeview(frame_notes, columns=("Matière", "Note"), show="headings", height=len(notes))
    tree.heading("Matière", text="Matière")
    tree.heading("Note", text="Note")

    for matiere, note in notes:
        tree.insert("", "end", values=(matiere, note))

    tree.pack()

    window.mainloop()

# Pour tester la fonction

