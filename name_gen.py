import db
from sqlalchemy.orm import sessionmaker
import random

Session = sessionmaker(bind=db.engine)
session = Session()

f_name = open("fname.txt", "r")  # open file with first names
s_name = open("sname.txt", "r")  # open file with last names
strasse = open("strasse.txt", "r")  # open file with streets

for x in range(2000, 4000):
    plz = random.randint(10000, 99999)  # generate random PLZ
    if session.query(db.Bibliotheksbenutzer).filter(db.Bibliotheksbenutzer.ausweisID == x).count() == 0:
        test = db.Bibliotheksbenutzer(f"{x:08d}", f_name.readline()[:-2], s_name.readline()[:-2], strasse.readline()[:-2], plz)
        session.add(test)
        session.commit()