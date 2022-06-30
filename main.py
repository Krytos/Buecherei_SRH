from scrapper import Scrapper
import db
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db.engine)
session = Session()

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
        add_autor()
    elif answer == 2:
        add_buch()
    elif answer == 3:
        add_verlag()
    elif answer == 4:
        add_ausleih()
    elif answer == 5:
        add_user()
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
        del_autor()
    elif answer == 2:
        del_buch()
    elif answer == 3:
        del_verlag()
    elif answer == 4:
        del_ausleih()
    elif answer == 5:
        del_user()
    else:
        print("Falsche Eingabe")
        add_eintrag()

def add_user():
    first_name = input("Vorname: ")
    last_name = input("Nachname: ")
    street = input("Straße: ")
    plz = int(input("PLZ: "))
    ausweisID = session.query(db.Bibliotheksbenutzer).order_by(db.Bibliotheksbenutzer.ausweisID.desc()).first()
    ausweisID = ausweisID.ausweisID + 1
    user = db.Bibliotheksbenutzer(ausweisID, first_name, last_name, street, plz)
    session.add(user)
    session.commit()


def add_autor():
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    if session.query(db.Autor).filter(db.Autor.vorname == vorname and db.Autor.nachname == nachname).count() == 0:
        autorID = session.query(db.Autor).order_by(db.Autor.autorID.desc()).first()
        autorID = autorID.autorID + 1
        autor = db.Autor(autorID, vorname, nachname)
        session.add(autor)
        session.commit()
    else:
        print("Autor ist bereits vorhanend.")


def add_buch():
    verlagid = int(input("Verlag ID: "))
    titel = input("Titel: ")
    isbn = int(input("ISBN: "))
    kategorie = input("Kategorie: ")
    buch = db.Buch(isbn, titel, kategorie, verlagid)
    session.add(buch)
    session.commit()

def add_verlag():
    telefonnummer = int(input("Telefonnummer: "))
    street = input("Straße: ")
    plz = int(input("PLZ: "))
    verlagID = session.query(db.Verlag).order_by(db.Verlag.verlagID.desc()).first()
    verlagID = verlagID.verlagID + 1
    verlag = db.Verlag(verlagID, telefonnummer, street, plz)
    session.add(verlag)
    session.commit()

def add_ausleih():
    entleihe = int(input("Entleihe: "))
    frist = int(input("Frist: "))
    rückgabe = int(input("Rückgabe: "))
    ausleih = db.Ausleihe(entleihe, frist, rückgabe)
    session.add(ausleih)
    session.commit()

  # Delete auswahl


start()