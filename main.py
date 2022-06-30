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
        add_user()

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

start()