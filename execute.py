import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

Session = sessionmaker(bind=db.engine)
session = Session()

# Add auswahl

def add_user():
    first_name = input("Vorname: ")
    last_name = input("Nachname: ")
    street = input("strasse: ")
    plz = int(input("PLZ: "))
    ausweisID = session.query(db.Bibliotheksbenutzer).order_by(db.Bibliotheksbenutzer.ausweisID.desc()).first()
    ausweisID = ausweisID.ausweisID + 1         # TODO Auto increment
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
    street = input("strasse: ")
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


def del_user():
    ausweisID = int(input("Ausweis ID: "))
    if session.query(db.Bibliotheksbenutzer).filter(db.Bibliotheksbenutzer.ausweisID == ausweisID).count() == 1:
        session.query(db.Bibliotheksbenutzer).filter(db.Bibliotheksbenutzer.ausweisID == ausweisID).delete()
        session.commit()
    else:
        print("Ausweis ID ist nicht vorhanden.")

def del_autor():
    autorID = int(input("Autor ID: "))
    if session.query(db.Autor).filter(db.Autor.autorID == autorID).count() == 1:
        session.query(db.Autor).filter(db.Autor.autorID == autorID).delete()
        session.commit()
    else:
        print("Autor ID ist nicht vorhanden.")


def del_buch():
    isbn = int(input("ISBN: "))
    if session.query(db.Buch).filter(db.Buch.isbn == isbn).count() == 1:
        session.query(db.Buch).filter(db.Buch.isbn == isbn).delete()
        session.commit()
    else:
        print("ISBN ist nicht vorhanden.")

def del_verlag():
    verlagID = int(input("Verlag ID: "))
    if session.query(db.Verlag).filter(db.Verlag.verlagID == verlagID).count() == 1:
        session.query(db.Verlag).filter(db.Verlag.verlagID == verlagID).delete()
        session.commit()
    else:
        print("Verlag ID ist nicht vorhanden.")

def del_ausleih():
    entleihe = int(input("Entleihe: "))
    if session.query(db.Ausleihe).filter(db.Ausleihe.entleihe == entleihe).count() == 1:
        session.query(db.Ausleihe).filter(db.Ausleihe.entleihe == entleihe).delete()
        session.commit()
    else:
        print("Entleihe ist nicht vorhanden.")

# Update auswahl

def update_user():
    ausweisID = int(input("Ausweis ID: "))
    if session.query(db.Bibliotheksbenutzer).filter(db.Bibliotheksbenutzer.ausweisID == ausweisID).count() == 1:
        first_name = input("Vorname: ")
        last_name = input("Nachname: ")
        street = input("strasse: ")
        plz = int(input("PLZ: "))
        session.query(db.Bibliotheksbenutzer).filter(db.Bibliotheksbenutzer.ausweisID == ausweisID).update({"first_name": first_name, "last_name": last_name, "street": street, "plz": plz})
        session.commit()
    else:
        print("Ausweis ID ist nicht vorhanden.")

def update_autor():
    autorID = int(input("Autor ID: "))
    if session.query(db.Autor).filter(db.Autor.autorID == autorID).count() == 1:
        vorname = input("Vorname: ")
        nachname = input("Nachname: ")
        session.query(db.Autor).filter(db.Autor.autorID == autorID).update({"vorname": vorname, "nachname": nachname})
        session.commit()
    else:
        print("Autor ID ist nicht vorhanden.")

def update_buch():
    isbn = int(input("ISBN: "))
    if session.query(db.Buch).filter(db.Buch.isbn == isbn).count() == 1:
        verlagid = int(input("Verlag ID: "))
        titel = input("Titel: ")
        kategorie = input("Kategorie: ")
        session.query(db.Buch).filter(db.Buch.isbn == isbn).update({"verlagid": verlagid, "titel": titel, "kategorie": kategorie})
        session.commit()
    else:
        print("ISBN ist nicht vorhanden.")

def update_verlag():
    verlagID = int(input("Verlag ID: "))
    if session.query(db.Verlag).filter(db.Verlag.verlagID == verlagID).count() == 1:
        telefonnummer = int(input("Telefonnummer: "))
        street = input("strasse: ")
        plz = int(input("PLZ: "))
        session.query(db.Verlag).filter(db.Verlag.verlagID == verlagID).update({"telefonnummer": telefonnummer, "street": street, "plz": plz})
        session.commit()
    else:
        print("Verlag ID ist nicht vorhanden.")

def update_ausleih():
    entleihe = int(input("Entleihe: "))
    if session.query(db.Ausleihe).filter(db.Ausleihe.entleihe == entleihe).count() == 1:
        frist = int(input("Frist: "))
        rückgabe = int(input("Rückgabe: "))
        session.query(db.Ausleihe).filter(db.Ausleihe.entleihe == entleihe).update({"frist": frist, "rückgabe": rückgabe})
        session.commit()
    else:
        print("Entleihe ist nicht vorhanden.")

# Suche

def search_user(search):
    nutzer = db.Bibliotheksbenutzer
    user = session.query(nutzer).filter(or_(nutzer.name.like(search), nutzer.nachname.like(search),
                                            nutzer.ausweisID.like(search))).all()
    return user
    # else:
    #     print("Ausweis ID ist nicht vorhanden.")

def search_book(search):
    buch = db.Buch
    book = session.query(buch).filter(or_(buch.titel.like(search), buch.isbn.like(search), buch.genre.like(search))).all()
    return book