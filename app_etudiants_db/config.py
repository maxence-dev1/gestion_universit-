#Stocke ici les variables globales pour tout le projet
import sqlite3
eleve_db = sqlite3.connect("etudiants.db")
cursor_eleve = eleve_db.cursor()