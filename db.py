from sqlalchemy import create_engine, Column, String, Integer
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


base.metadata.create_all(engine)  # create table if not exists