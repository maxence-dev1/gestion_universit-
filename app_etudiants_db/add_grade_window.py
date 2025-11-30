from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
import tkinter as tk
import op




def get_id():
    def submit_entries():
        global submitted_entries
        submitted_entries = id_entry.get()
        window.destroy()  

    window = tk.Toplevel()  
    window.title("Supprimer Étudiant")

    tk.Label(window, text="ID").pack()
    id_entry = tk.Entry(window)
    id_entry.pack()
    id_entry.focus_set() 

    submit_button = tk.Button(window, text="Suivant", command=submit_entries)
    submit_button.pack()

    window.bind('<Return>', lambda event: submit_entries())
    window.wait_window()  
    return submitted_entries




def run():
    def submit_entries():
        preid = prenom_entry.get()
        date_value = date_entry.get()
        global submitted_entries
        submitted_entries = [ preid, date_value]
        window.destroy()

    id = get_id()


    window = tk.Toplevel()
    window.title("Ajouter Note")


    nom = op.get_name_by_id(id)
    prenom = op.get_firstname_by_id(id)
    matieres = op.get_all_matiere()
    print("matieres : ", matieres)



    tk.Label(window, text=f"Ajouter une note à : {prenom} {nom}").pack()

    tk.Label(window, text="Prénom").pack()
    prenom_entry = tk.Entry(window)
    prenom_entry.pack()

    tk.Label(window, text="Date").pack()
    date_entry = tk.Entry(window)
    date_entry.pack()

    tk.Label(window, text="Date").pack()
    date_entry = tk.Entry(window)
    date_entry.pack()

    submit_button = tk.Button(window, text="Suivant", command=submit_entries)
    submit_button.pack()

    window.bind('<Return>', lambda event: submit_entries())
    window.wait_window()  
    return submitted_entries



run()