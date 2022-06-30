from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
connection = engine.connect()  # connect to database
base = declarative_base()  # create base class

class Bibliotheksbenutzer (base):
    __tablename__ = "bibliotheksbenutzer"

    ausweisID = Column(Integer, primary_key=True)
    name = Column(String)
    nachname = Column(String)
    straße = Column(String)
    plz = Column(Integer)

    def __init__(self, ausweisID, name, nachname, straße, plz):
        self.ausweisID = ausweisID
        self.name = name
        self.nachname = nachname
        self.straße = straße
        self.plz = plz

class Autor (base):
    __tablename__ = "autor"

    autorID = Column(Integer, primary_key=True)
    vorname = Column(String)
    nachname = Column(String)

    def __init__(self, autorID, vorname, nachname):
        self.autorID = autorID
        self.vorname = vorname
        self.nachname = nachname


class Buch (base):
    __tablename__ = "buch"

    isbn = Column(Integer, primary_key=True)
    verlagID = Column(Integer, ForeignKey('verlag.verlagID'))
    titel = Column(String)
    kategorie = Column(String)

    def __init__(self, isbn, verlagID, titel, kategorie):
        self.isbn = isbn
        self.verlagID = verlagID
        self.titel = titel
        self.kategorie = kategorie

class Verlag (base):
    __tablename__ = "verlag"

    verlagID = Column(Integer, primary_key=True)
    telefonnummer = Column(Integer)
    straße = Column(String)
    plz = Column(Integer)

    def __init__(self, verlagID, telefonnummer, straße, plz):
        self.verlagID = verlagID
        self.telefonnummer = telefonnummer
        self.straße = straße
        self.plz = plz

class Bücher (base):
    __tablename__ = "bücher"

    bücherID = Column(Integer, primary_key=True)
    isbn = Column(Integer, ForeignKey('buch.isbn'))

    def __init__(self, bücherID, isbn):
        self.bücherID = bücherID
        self.isbn = isbn


class Ausleihe (base):
    __tablename__ = "ausleihe"

    entleihe = Column(Integer, primary_key=True)
    frist = Column(Integer)
    ausweisID = Column(Integer, ForeignKey('bibliotheksbenutzer.ausweisID'))
    buchID = Column(Integer, ForeignKey('bücher.bücherID'))
    rückgabe = Column(Date)

    def __init__(self, entleihe, frist, ausweisID, buchID, rückgabe):
        self.entleihe = entleihe
        self.frist = frist
        self.ausweisID = ausweisID
        self.buchID = buchID
        self.rückgabe = rückgabe


class Identifikation (base):
    __tablename__ = "identifikation"

    autorid = Column(Integer, ForeignKey('autor.autorID'))
    isbn = Column(Integer, ForeignKey('buch.isbn'))

    def __init__(self, autorid, isbn):
        self.autorid = autorid
        self.isbn = isbn


base.metadata.create_all(engine)  # create table if not exists