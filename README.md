# Orange Money – Application Console Python

##  Description
Ce projet est une **application console en Python** qui simule les fonctionnalités de **Orange Money**.  
Il permet à un utilisateur de gérer son solde, effectuer des transferts, annuler des transferts et consulter l’historique, avec **sauvegarde des données dans un fichier JSON**.

Le projet est conçu dans un **style simple et pédagogique**, idéal pour les étudiants débutants/intermédiaires en Python .

---

##  Fonctionnalités
###  Accès USSD
- L’utilisateur doit composer **#144#** pour accéder au menu
- Simulation fidèle du fonctionnement USSD réel

### Sécurité
- Code secret requis pour les opérations sensibles
- 3 tentatives maximum avant blocage

###  Gestion du solde
- Solde initial : **50 000 000 FCFA**
- Solde automatiquement sauvegardé dans `data.json`

###  Gestion du compte
- Consultation du solde
- Solde initial : **50 000 000 FCFA**
- Sauvegarde automatique dans `data.json`

### Achat de forfait internet
- Pass Jour :
  - 300 Mo → 200 FCFA
  - 1,5 Go → 500 FCFA
  - 5 Go → 1000 FCFA

###  TTransfert d’argent
- Transfert national
- Vérification du numéro :
  - 9 chiffres
  - commence par **77** ou **78**
- Enregistrement automatique :
  - ID du transfert
  - numéro
  - montant
  - date et heure
  - statut (ACTIF / ANNULÉ)

###  Annulation de transfert
- Annulation possible si le transfert n’est pas déjà annulé
- Remboursement automatique du montant

### Historique
- Voir tous les transferts
- Filtrer les transferts par numéro de téléphone
- Affichage du statut : **ACTIF / ANNULÉ**

---

##  Structure du projet
OrangeMoney
main.py
menu_orangeM.py # Programme principal
data.json # Données (solde + transactions)
 README.md

