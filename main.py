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
    elif answer == 3:
        update_eintrag()
    elif answer == 4:
        search_eintrag()

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
        del_eintrag()

def update_eintrag():
    print("""
    Bitte auswählen: 
    1 - Autor ändern
    2 - Buch ändern
    3 - Verlag ändern
    4 - Ausleihe ändern
    5 - Nutzer ändern
    """)
    answer = int(input())
    if answer == 1:
        execute.update_autor()
    elif answer == 2:
        execute.update_buch()
    elif answer == 3:
        execute.update_verlag()
    elif answer == 4:
        execute.update_ausleih()
    elif answer == 5:
        execute.update_user()
    else:
        print("Falsche Eingabe")
        update_eintrag()

def search_eintrag():
    print("""
    Bitte auswählen: 
    1 - Autor suchen
    2 - Buch suchen
    3 - Verlag suchen
    4 - Ausleihe suchen
    5 - Nutzer suchen
    """)
    answer = int(input())
    if answer == 1:
        execute.search_autor()
    elif answer == 2:
        execute.search_buch()
    elif answer == 3:
        execute.search_verlag()
    elif answer == 4:
        execute.search_ausleih()
    elif answer == 5:
        execute.search_user()
    else:
        print("Falsche Eingabe")
        search_eintrag()

start()