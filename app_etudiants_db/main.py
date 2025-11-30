import tkinter
import sqlite3
import op
import config, subprocess, connect, login

"""
Application pour les eleves et responsables
Un eleve pourra : 
Consulter ses notes
Consulter son EDT
'Stocker' des documents (leurs chemins d'acces, chaque doc est stocké sur son propre ordi mais il pourra gerer une arborescence simple)
Envoyer des messages à lui ou d'autres eleves


Un admin pourra : 
Tout faire
"""


"""
print("============================================================================================================================================")

print("Bienvenue sur cette application.")
print("Veuillez d'abord vous connecter")
is_op = False
iden = 0
while iden == 0:
    identifiant = input("Entrez votre identifiant : ")
    if not connect.is_identifiant_exist(identifiant):
        print("Entrez un identifiant valide")
    else : 
        iden = 1
mdpp = 0
while mdpp == 0:
    mdp = input("Entrez votre mot de passe : ")
    if not connect.verif_password(identifiant, mdp):
        print("Mauvais mot de passse")
    else : 
        mdpp = 1


ID = connect.get_id(identifiant)[0]

if ID < 0:
    is_op = True

print("============================================================================================================================================")

if is_op: 
    print("______________________________________________________Bienvenue operateur______________________________________________________________ ")
    print("Pour voir la liste des commandes tapez /help, sinon vous pouvvez taper vos commandes.")
    running_op = True
    while running_op:
        command = input("")
        words = command.split()
        if command == "/help":
            print("Voici la liste des commandes : ")
            print("Consulter la liste des eleves : /list") #
            print("afficher une table : /printTable table") #
            print("Ajouter un eleve : /add nom prenom date_de_naissance")#
            print("Supprimer un etudiant : /del id")#
            print("Ajouter une note : /addGrade eleve_id, matiere_id, note")#
            print("Afficher le tableau des notes d'un etudiant : /getAllGrades id")#
            print("Récuperer toutes les infos d'un etudiant : /getInfo id")#
            print("Modifier le nom d'un etudiant : /editName id newname")#
            print("Modifier le prenom d'un etudiant : /editFirstname id newfirstname")#
            print("Modifier la date de naissance d'un etudiant : /editBirthday id newbirthday")#
            print("Supprimer une note : /delGrade idgrade")
            print("Quitter : /quit")#
        if words[0] == "/quit":
            running_op = False
        if words[0] == "/getInfo":
            op.get_info_student(words[len(words)-1])
        if words[0] == "/add":
            op.add_etu(words[1], words[2], words[3])
        if words[0] == "/list":
            op.print_table("eleves")
        if words[0] == "/printTable":
            op.print_table(words[1])
        if words[0] == "/del":
            op.delete_etu(words[1])
        if words[0] == "/addGrade":
            op.add_grade(words[1],words[2],words[3])
        if words[0] == "/editName":
            op.edit_name(words[1], words[2])
        if words[0] == "/editFistname":
            op.edit_firstname(words[1], words[2])
        if words[0] == "/editBirthday":
            op.edit_birthday(words[1], words[2])
        if words[0] == "/delGrade":
            op.delete_grade(words[1])
        
        
        
        





else : 
    print("_________________________________________________________Bienvenue_____________________________________________________________________ ")
    print("Pour voir la liste des commandes tapez /help, sinon vous pouvvez taper vos commandes.")
    running = True
    
    while running:
        command = input("")
        words = command.split()
        if command == "/help":
            print("Voici la liste des commandes : ")
            print("Modifier son mot de passe /updatePassword oldPassword newPassword")
            print("Acceder à vos notes : /grades")#
            print("Acceder à vos informations personnelles : /infos")#
            print("Quiter : /quit")#
        if words[0] == "/infos":
            op.get_info_student(ID)
        if words[0] == "/quit":
            running = False
        if words[0] == "/grades":
            op.get_all_grades(ID)
        if words[0] == "/updatePassword":
            op.edit_password(identifiant, words[1], words[2])
     """   
            
login.run()
