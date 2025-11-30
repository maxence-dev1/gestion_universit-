from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
import tkinter as tk

def run():
    def submit_entries():
        nom_value = nom_entry.get()
        prenom_value = prenom_entry.get()
        date_value = date_entry.get()
        global submitted_entries
        submitted_entries = [nom_value, prenom_value, date_value]
        window.destroy()

    window = tk.Toplevel()  # Crée une nouvelle fenêtre indépendante
    window.title("Ajouter Étudiant")

    tk.Label(window, text="Nom").pack()
    nom_entry = tk.Entry(window)
    nom_entry.pack()

    tk.Label(window, text="Prénom").pack()
    prenom_entry = tk.Entry(window)
    prenom_entry.pack()

    tk.Label(window, text="Date").pack()
    date_entry = tk.Entry(window)
    date_entry.pack()

    submit_button = tk.Button(window, text="Suivant", command=submit_entries)
    submit_button.pack()

    window.bind('<Return>', lambda event: submit_entries())
    window.wait_window()  # Attend la fermeture de la fenêtre
    return submitted_entries

