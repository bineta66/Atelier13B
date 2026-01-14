from menu_orangeM import menu_orange
print("=========================================")
print("Composez #144#")
print("=========================================")
print()
while True:
    ussd_Om=input("donner le code de consultation du menu orange money: ").strip()
    if ussd_Om == "#144#":
        bb=input("taperz sur entre pour continuer")
        menu_orange()
    else:
        print("invalide") 