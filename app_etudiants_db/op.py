import tkinter
import sqlite3
import config, connect, bcrypt

cursor_eleve = config.cursor_eleve


def print_table(table):
    cursor_eleve.execute(f"PRAGMA table_info({table})")
    colonnes = cursor_eleve.fetchall()
    cursor_eleve.execute(f"select * from {table}")
    resultats = cursor_eleve.fetchall()
    for i in range(len(colonnes)):
        print(colonnes[i][1],"    ", end="")
    print("\n")
    for i in range(len(resultats)):
        print(resultats[i])



def add_etu(nom, prenom, date_de_naissance):
    """Add a student """
    cursor_eleve.execute("insert into eleves (nom, prenom, date_de_naissance) values (? , ? , ?)", (nom, prenom, date_de_naissance))
    config.eleve_db.commit()
    id = cursor_eleve.lastrowid
    identifiant = f"{nom}.{prenom}"
    connect.add(id, identifiant, "12341234")
    

def delete_etu(id):
    """Delete a student"""
    try:
        cursor_eleve.execute("delete from eleves where id = ?", (id,))
        cursor_eleve.execute("delete from identifiants where id = ?", (id,))
        config.eleve_db.commit()
        return 1
    except Exception as e:
        print("Erreur lors de la suppression :", e)
        return 2


def add_grade(eleve_id, matiere_id, note):
    """Add a grade"""
    cursor_eleve.execute(f"insert into notes (eleve_id, matiere_id, note) values ({eleve_id},{matiere_id},{note})")
    config.eleve_db.commit()
 


def get_all_grades(id):
    """Return all grades of a student"""
    cursor_eleve.execute(f"select * from notes where eleve_id = {id}")
    grades = cursor_eleve.fetchall()
    return grades

def get_info_student(id):
    """get all info of a student"""
    cursor_eleve.execute(f"select * from eleves where ID = {id}")
    infos = cursor_eleve.fetchone()
    if infos : 
        nom, prenom, date_naissance = infos[1], infos[2], infos[3]
        
        print("---------------------------------------------------")
        print(f"eleve numero {id} \nnom : {nom} \nprenom : {prenom}\ndate de naissance : {date_naissance}")
        print("-----------")
        
        cursor_eleve.execute(f"SELECT * FROM ( SELECT e.id AS eleve_id, e.nom AS eleve, m.id AS matieres, n.note FROM notes n JOIN eleves e ON n.eleve_id = e.id JOIN matieres m ON n.matiere_id = m.id) AS result WHERE result.eleve_id = {id};")
        grades = cursor_eleve.fetchall()
        
        if not grades:
            print("Aucune note trouvée pour cet élève.")
            return
        
        grades_names = ["mathematiques", "francais", "histoire","physique/chimie","anglais","espagnol","NSI"]
        all_grades = [0,0,0,0,0,0,0]
        for i in range(len(all_grades)):
            if grades_names[i]:
                print(grades_names[i], " : ", end="")
                for g in grades:
                    if g[2]-1 == i:
                        print(g[3], end=", ")
                print("\n")
        print("---------------------------------------------------")  
    else : 
        print("Cet eleve n'est pas enregistré")

def edit_name(id, new_name):
    """edit the name"""
    cursor_eleve.execute("UPDATE eleves SET nom = ? WHERE id = ?", (new_name, id))
    config.eleve_db.commit()

def edit_firstname(id, new_name):
    """edit the firstname"""
    cursor_eleve.execute("UPDATE eleves SET prenom = ? WHERE id = ?", (new_name, id))
    config.eleve_db.commit()    

def edit_birthday(id, new_date):
    """edit the birthday"""
    cursor_eleve.execute("UPDATE eleves SET date_de_naissance = ? WHERE id = ?", (new_date, id))
    config.eleve_db.commit()      

def delete_grade(id_grade):
    """delete a grade"""
    cursor_eleve.execute("delete from notes where id = ?", (id_grade,))
    config.eleve_db.commit()   

def edit_password(id, old_password, new_password):
    """Edit a password"""    
    cursor_eleve.execute("SELECT password FROM identifiants WHERE identifiant = ?", (id,))
    old_hashed = cursor_eleve.fetchone()
    if old_hashed is None:
        print("ID introuvable !")
        return
    
    if connect.verif_password(id, old_password):
        hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        cursor_eleve.execute("UPDATE identifiants SET password = ? WHERE identifiant = ?", (hashed, id))
        config.eleve_db.commit()
        
        print(f"Password changed successfully ({cursor_eleve.rowcount} ligne(s) modifiée(s))")
    else: 
        print("Wrong password")

def get_name_by_id(id):
    cursor_eleve.execute("select nom from eleves where id = ?", (id,))
    name = cursor_eleve.fetchone()
    return name[0]

def get_firstname_by_id(id):
    cursor_eleve.execute("select prenom from eleves where id = ?", (id,))
    name = cursor_eleve.fetchone()
    return name[0]

def get_picture_by_id(id):
    cursor_eleve.execute("select photo from eleves where id = ?", (id,))
    name = cursor_eleve.fetchone()
    return name[0]

def get_birthday_by_id(id):
    cursor_eleve.execute("select date_de_naissance from eleves where id = ?", (id,))
    name = cursor_eleve.fetchone()
    return name[0]

def get_picture_by_id(id):
    cursor_eleve.execute("select photo from eleves where id = ?", (id,))
    name = cursor_eleve.fetchone()
    return name[0]

def get_id_by_identifiant(identifiant):
    cursor_eleve.execute("select id from identifiants where identifiant = ?", (identifiant,))
    id = cursor_eleve.fetchone()
    print("ID : ", id[0])
    return id[0]

def get_all_students():
    cursor_eleve.execute("select * from eleves")
    liste = cursor_eleve.fetchall()
    return liste

def get_col_name(table):
    cursor_eleve.execute(f"PRAGMA table_info({table})")
    colonnes = cursor_eleve.fetchall()
    col_names = [colonne[1] for colonne in colonnes]
    return col_names

def get_all_matiere():
    cursor_eleve.execute(f"select * from matieres")
    infos = cursor_eleve.fetchall()
    return infos
