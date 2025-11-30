import connect, acceuil_op,op, acceuil_eleve
import subprocess
from tkinter import messagebox

access = False
identifiant = None
password = None

def on_login(event=None):  # Ajout de l'argument event avec une valeur par défaut
    global identifiant, password
    identifiant = entry_identifiant.get()
    password = entry_password.get()

    if not connect.is_identifiant_exist(identifiant):
        messagebox.showerror("Erreur", "Identifiant incorrect")
    
    elif not connect.verif_password(identifiant, password):
        messagebox.showerror("Erreur", "Mot de passe incorrect")
    
    else:
        global access
        access = True
        print("Identifiant : ", identifiant)
        print("Mot de passe : ", password)
        next_page()

def next_page():
    root.destroy()  # Ferme la fenêtre de connexion
    if op.get_id_by_identifiant(identifiant) < 0:
        acceuil_op.run(op.get_id_by_identifiant(identifiant) )
    else : 
        acceuil_eleve.run(op.get_id_by_identifiant(identifiant) )


# Configuration de customtkinter
from customtkinter import *

def run():
    global entry_identifiant, entry_password, root
    set_appearance_mode("dark")
    set_default_color_theme("blue")

    # Création de la fenêtre principale
    root = CTk()
    root.title("Page de Connexion")
    root.geometry("400x300")


    window_width = 700
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")


    # Création d'un frame pour centrer les widgets
    frame = CTkFrame(root)
    frame.pack(expand=True)

    # Création des widgets
    label_identifiant = CTkLabel(frame, text="Identifiant:")
    label_password = CTkLabel(frame, text="Mot de passe:")
    entry_identifiant = CTkEntry(frame, width=200)
    entry_password = CTkEntry(frame, show="*", width=200)
    button_login = CTkButton(frame, text="Suivant", command=on_login, width=200)

    # Placement des widgets
    label_identifiant.pack(pady=10)
    entry_identifiant.pack(pady=10)
    label_password.pack(pady=10)
    entry_password.pack(pady=10)
    button_login.pack(pady=20)

    root.bind('<Return>', on_login)

    # Lancement de la boucle principale
    root.mainloop()