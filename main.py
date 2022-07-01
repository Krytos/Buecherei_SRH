import execute

def start():
    answer = int(input("""
    Bitte auswählen: 
    1 - Datenbank eintrag hinzufügen
    2 - Datenbank eintrag löschen
    3 - Datenbank eintrag ändern
    4 - Datenbank eintrag suchen
    """))
    if answer == 1:
        add_eintrag()
    elif answer == 2:
        del_eintrag()

def add_eintrag():
    print("""
    Bitte auswählen: 
    1 - Autor hinzufügen
    2 - Buch hinzufügen
    3 - Verlag hinzufügen
    4 - Ausleihe hinzufügen
    5 - Nutzer hinzufügen
    """)
    answer = int(input())
    if answer == 1:
        execute.add_autor()
    elif answer == 2:
        execute.add_buch()
    elif answer == 3:
        execute.add_verlag()
    elif answer == 4:
        execute.add_ausleih()
    elif answer == 5:
        execute.add_user()
    else:
        print("Falsche Eingabe")
        add_eintrag()

def del_eintrag():
    print("""
    Bitte auswählen: 
    1 - Autor entfernen
    2 - Buch entfernen
    3 - Verlag entfernen
    4 - Ausleihe entfernen
    5 - Nutzer entfernen
    """)
    answer = int(input())
    if answer == 1:
        execute.del_autor()
    elif answer == 2:
        execute.del_buch()
    elif answer == 3:
        execute.del_verlag()
    elif answer == 4:
        execute.del_ausleih()
    elif answer == 5:
        execute.del_user()
    else:
        print("Falsche Eingabe")
        add_eintrag()

start()