import sqlite3, config, op, bcrypt
cursor_eleve = config.cursor_eleve


def add(id, identifiant, password):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  
        cursor_eleve.execute("insert into identifiants (id, identifiant, password) values (?, ?, ?)", (id, identifiant, hashed))
        config.eleve_db.commit()
        return 

def is_identifiant_exist(identifiant):
    cursor_eleve.execute("select 1 from identifiants where identifiant = ?", (identifiant,))
    result = cursor_eleve.fetchone()
    if result:
        return True
    else :
        return False



def verif_password(identifiant, password):
    cursor_eleve.execute("SELECT password FROM identifiants WHERE identifiant = ?", (identifiant,))
    hashed = cursor_eleve.fetchone()

    if hashed is None:
        print("Identifiant introuvable.")
        return False  

    return bcrypt.checkpw(password.encode(), hashed[0].encode() if isinstance(hashed[0], str) else hashed[0])
    
def get_id(identifiant):
    cursor_eleve.execute("select ID from identifiants where identifiant = ?", (identifiant,))
    id = cursor_eleve.fetchone()
    return id
