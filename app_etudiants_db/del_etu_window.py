from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
import tkinter as tk

def run():
    def submit_entries():
        global submitted_entries
        submitted_entries = nom_entry.get()
        window.destroy()  

    window = tk.Toplevel()  
    window.title("Supprimer Étudiant")

    tk.Label(window, text="ID").pack()
    nom_entry = tk.Entry(window)
    nom_entry.pack()
    nom_entry.focus_set() 

    submit_button = tk.Button(window, text="Suivant", command=submit_entries)
    submit_button.pack()

    window.bind('<Return>', lambda event: submit_entries())
    window.wait_window()  
    return submitted_entries  
