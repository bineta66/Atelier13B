import json
import os
import sys
from datetime import datetime
FICHIER = "data.json"

# valeurs par défaut
solde = 50000000
transactions = []

# =========================
# CHARGEMENT DES DONNÉES
# =========================
if os.path.exists(FICHIER):
    with open(FICHIER, "r") as f:
        contenu = f.read().strip()
        if contenu != "":
            try:
                data = json.loads(contenu)
                solde = data["solde"]
                transactions = data["transactions"]
            except:
                solde = 50000000
                transactions = []

# =========================
# SAUVEGARDE
# =========================
def sauvegarder():
    with open(FICHIER, "w") as f:
        json.dump(
            {
                "solde": solde,
                "transactions": transactions
            },
            f,
            indent=4 )

# =========================
# MENU PRINCIPAL
# =========================
def menu_orange():
    while True:
        print("\n=== Bienvenue sur Orange Money ===")
        print("1: consulter le solde")
        print("2: Acheter un forfait")
        print("3: Effectuer un transfert")
        print("4: Annuler un transfert")
        print("5: Voir l’historique")
        print("6: Quitter")

        choix = input(" donner  votre choix : ")

        if choix == "1":
            consultation_solde()
        elif choix == "2":
            acheter_forfait()
        elif choix == "3":
            transfert()
        elif choix == "4":
            annuler()
        elif choix == "5":
            Tous_historeique()
        elif choix == "6":
            sauvegarder()
            sys.exit()
        else:
            print("Choix invalide")

# =========================
def consultation_solde():
    global solde
    code()
    print("Le solde de votre compte est :", solde, "FCFA")

# =========================
def acheter_forfait():
    while True:
        print("==================================")
        print("je souhaite acheter un pass  internet")
        print("1: Pass Jour")
        print("9: Accueil")
        print("0: Retour")

        choix = input("Choix : ")
        if choix == "1":
            passJour()
        elif choix == "9":
            menu_orange()
        elif choix == "0":
            return
        else:
            print("Invalide")

# =========================
def passJour():
    global solde
    while True:
        print("1: 300Mo à 200F")
        print("2: 1,5Go à 500F")
        print("3: 5Go à 1000F")
        print("0: Retour")

        choix = input("Choix : ")
        if choix == "1":
            achat_forfait(200)
        elif choix == "2":
            achat_forfait(500)
        elif choix == "3":
            achat_forfait(1000)
        elif choix == "0":
            return
        else:
            print("Invalide")

def achat_forfait(montant):
    global solde
    code()
    if solde < montant:
        print("Solde insuffisant")
        return
    solde -= montant
    sauvegarder()
    print("Achat réussi – Nouveau solde :", solde)

# =========================
def transfert():
    while True:
        print("1: Transfert national")
        print("9: Accueil")
        print("0: Retour")

        choix = input("Choix : ")
        if choix == "1":
            TelephoneN()
        elif choix == "9":
            menu_orange()
        elif choix == "0":
            return
        else:
            print("Invalide")

# =========================
def TelephoneN():
        

       while True:
              Telephone=input("donner ton numero: ").replace(" ","")
              if len(Telephone) == 9 and Telephone[:2] in ["77","78",]  :
                     if Telephone.isdigit():
                            saisie_montant1(Telephone)
                            navigation(menu_orange)
                           
                     else:
                            print("il doit etre des chifress") 
              else:
                     print("le numero doit etre des 9 chiffres , est commencer par 77,78")

# =========================
def saisie_montant1( telephone):
    date_heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    global solde, transactions

    while True:
        montant = input("donner le montant : ")
        if not montant.isdigit():
            print("Montant invalide")
            continue

        montant = int(montant)
        if montant <= 0:
            print("Montant invalide")
            continue
        if montant > solde:
            print("Solde insuffisant")
            return

        code()
        solde -= montant

        transfert_id = len(transactions) + 1
        transactions.append({
            "ID": transfert_id,
            "telephone": int(telephone),   
            "montant": montant,
            "annuler": False,
            "heure": date_heure
        })

        sauvegarder()
        print("Transfert réussi | ID :", transfert_id)
        print("Numéro :", telephone)
        print("Montant :", montant, "FCFA")
        print("Date :", date_heure)
        print("Nouveau solde :", solde)
        return


# =========================
def annuler():
    global solde, transactions

    if not transactions:
        print("Aucun transfert effectué")
        return

    print("=== LISTE DES TRANSFERTS ===")
    for t in transactions:
        if t["annuler"]:
            statut = "ANNULÉ"
        else:
            statut = "ACTIF"
        print(f"heure: {t['heure']}  | ID:  {t['ID']} |  Telephone: {t['telephone']} | montant transferer: {t['montant']} FCFA | statut transfert: {statut}")


    choix = input("Donner l'ID du transfert à annuler (0 pour quitter) : ")

    if choix == "0":
        return

    if not choix.isdigit():
        print("ID invalide")
        return

    choix = int(choix)

    for t in transactions:
        if t["ID"] == choix:
            if t["annuler"]:
                print("Ce transfert est déjà annulé")
                return

            code()
            t["annuler"] = True
            solde += t["montant"]
            sauvegarder()

            print("Transfert annulé avec succès")
            print("l identifiant transfert annuler: ",t["ID"])
            print("Montant remboursé :", t["montant"], "FCFA")
            print("Nouveau solde :", solde)
            return

    print("ID introuvable")


# =========================
def historique():
    code()
    
    if not transactions:
        print("Aucune transaction")
        return
        
    print("=== HISTORIQUE DES TRANSFERTS EFFECTUER  ===")
    for t in transactions:
        if t["annuler"]:
            statut = "ANNULÉ"
        else:
            statut = "ACTIF"
        print(f"heure: {t['heure']}  | ID:  {t['ID']} |  Telephone: {t['telephone']} | montant transferer: {t['montant']} FCFA | statut transfert: {statut}")


# =========================
def Tous_historeique():
      while True:
        print("1: voir tous les transfert")
        print("2: voir les transfert par numero")
        print("---------")
        print("9: Acceuil")
        print("0.pred")

        choix = input("Choix : ")
        if choix == "1":
           historique()
        elif choix == "2":
            parFiltrer()
        elif choix == "9":
            menu_orange()
        elif choix == "0":
            return
        else:
            print("Invalide")



# =========================
def code():
    mot_passe_correct = "1797"
    tentative = 0
    while tentative < 3:
        mp = input("Code secret : ")
        if mp == mot_passe_correct:
            return
        tentative += 1
        print("Code incorrect")
    print("Compte bloqué")
    sys.exit()

# =========================


def navigation(precedent):
    while True:
        print("-----")
        print("9 : Menu principal")
        print("0 : Précédent")
        print("1 : Quitter")

        choix = input("Votre choix : ")

        if choix == "9":
            menu_orange()
        elif choix == "0":
            transfert()
        elif choix == "1":
            print("Au revoir")
            sys.exit()
        else:
            print("Choix invalide")
def parFiltrer():
    global transactions

    code()
    telephone = input("donner le numero (0: retour, 9: accueil) : ").replace(" ", "")

    if telephone == "0":
        return
    if telephone == "9":
        return menu_orange()

    if not telephone.isdigit():
        print("Numéro invalide")
        return

    telephone = int(telephone)
   
    print("=== les tranfert effcuter sur le numero====")
    for t in transactions:
        if t["telephone"] == telephone:
             

            if t["annuler"]:
                statut = "ANNULÉ"
            else:
                statut = "ACTIF"
            
            print(
                f"heure: {t['heure']} | ID: {t['ID']} | "
                f"Telephone: {t['telephone']} | "
                f"Montant: {t['montant']} FCFA | "
                f"Statut: {statut}"
            )

        else:
            print("Numéro introuvable")
            break
