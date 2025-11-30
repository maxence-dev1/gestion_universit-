from customtkinter import *
from PIL import Image, ImageTk, ImageDraw
import op, add_etu_window, del_etu_window, page_etu
import os
import subprocess
from tkinterweb import HtmlFrame
import tkinter as tk


def make_circle(image):
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    image = image.crop(((image.width - size) // 2, (image.height - size) // 2, 
                        (image.width + size) // 2, (image.height + size) // 2))
    image.putalpha(mask)

    return image


def profil_frame(parent):
    profile_frame = CTkFrame(parent)
    profile_frame.pack(side="top", fill="x", expand=False)

    image = Image.open(image_path)
    if image.size != (60, 60):
        image = image.resize((60, 60), Image.LANCZOS)

    image = make_circle(image)
    profile_image = ImageTk.PhotoImage(image)

    profile_image_label = CTkLabel(profile_frame, image=profile_image, text="")
    profile_image_label.image = profile_image
    profile_image_label.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

    name_label = CTkLabel(profile_frame, text=f"{name}", font=("Arial", 16, "bold"))
    name_label.grid(row=0, column=1, padx=5, pady=(5, 0), sticky="n")
    firstname_label = CTkLabel(profile_frame, text=f"{firstname}", font=("Arial", 16, "bold"))
    firstname_label.grid(row=0, column=2, padx=5, pady=(5, 0), sticky="n")
    if admin:
        admin_label = CTkLabel(profile_frame, text="Administrateur", font=("Arial", 14, "bold"))
    else:
        admin_label = CTkLabel(profile_frame, text="Etudiant", font=("Arial", 14, "bold"))
    admin_label.grid(row=1, column=1, columnspan=2, padx=5, pady=(0, 5), sticky="n")



def left_tab(parent):
    global left_frame
    left_frame = CTkFrame(parent, width=100, fg_color="gray")
    left_frame.pack(side="left", fill="y", expand=False)

    def resize_left_frame(event):
        new_width = event.width
        left_frame.config(width=new_width)
    add_button()
    left_frame.bind("<Configure>", resize_left_frame)

def refresh():
    table_frame.destroy()
    tab(right_frame)


def button_add():
    infos = add_etu_window.run()
    op.add_etu(infos[0], infos[1], infos[2])
    refresh()

def button_del():
    info = del_etu_window.run()
    op.delete_etu(info)
    refresh()



def add_button():
    #ADD
    button = CTkButton(left_frame, text="Ajouter", command=button_add)
    button.grid(row=left_frame.grid_size()[1], column=0, sticky="ew", pady=10, padx=5)
    left_frame.grid_columnconfigure(0, weight=1, uniform="equal")
    #Delete
    button = CTkButton(left_frame, text="Supprimer", command=button_del)
    button.grid(row=left_frame.grid_size()[1], column=0, sticky="ew", pady=10, padx=5)
    left_frame.grid_columnconfigure(0, weight=1, uniform="equal")


def on_click(row):
    if row > 0:  # Ignore l'en-tête
        student_id = op.get_all_students()[row - 1][0]  # ID dans la première colonne
        page_etu.run(student_id)
        return student_id







def tab(parent):
    global table_frame
    table_frame = CTkFrame(parent)
    table_frame.pack(side="right", fill="both", expand=True)

    headers = op.get_col_name("eleves")
    for col_index, header in enumerate(headers):
        label = CTkLabel(table_frame, text=header, fg_color="gray30", text_color="white", corner_radius=5, padx=5, pady=5)
        label.grid(row=0, column=col_index, sticky="nsew", padx=1, pady=1)

    rows = op.get_all_students()
    for row_index, r in enumerate(rows, start=1):  # Commence à la ligne 1 pour les données
        if r[0] < 0:
            continue
        for col_index, value in enumerate(r):
            label = CTkLabel(table_frame, text=value, fg_color="gray50", text_color="white", corner_radius=1, padx=0, pady=5)
            label.grid(row=row_index, column=col_index, sticky="nsew", padx=1, pady=1)
            label.bind("<Button-1>", lambda e, row_index=row_index: on_click(row_index))




    # Ajout d'un gestionnaire pour ajuster l'espace de la grille
    for i in range(len(headers)):  # Nombre de colonnes
        table_frame.grid_columnconfigure(i, weight=1)


def run(id):
    global name, firstname, image_path, root, admin
    name = ""
    firstname = ""
    image_path = ""
    print("IDDDDDDAAAAAA : ", id)
    name = op.get_name_by_id(id)
    firstname = op.get_firstname_by_id(id)
    image_path = op.get_picture_by_id(id)
    admin = False
    if id < 0:
        admin = True

    set_appearance_mode("dark")
    set_default_color_theme("blue")

    root = CTk()
    root.title("Profile Window")
    window_width = 1200
    window_height = 700

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
    paned_window.pack(fill=tk.BOTH, expand=1)

    left_pane = tk.PanedWindow(paned_window, orient=tk.VERTICAL)
    paned_window.add(left_pane)

    global right_frame
    right_frame = CTkFrame(paned_window,)
    paned_window.add(right_frame)
    tab(right_frame)



    profile_frame = CTkFrame(left_pane)
    left_pane.add(profile_frame)
    profil_frame(profile_frame)

    left_frame = CTkFrame(left_pane, width=100, fg_color="gray")
    left_pane.add(left_frame)
    left_tab(left_frame)


    
    

    root.mainloop()

