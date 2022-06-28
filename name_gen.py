from sqlalchemy import create_engine, Column, String, Integer

f_name = open("fname.txt", "r")
s_name = open("sname.txt", "r")
datenbank = open("bibliothek_projekt.sql", "r")

# for x in range(50):
#     print(f"{f_name.readline(x)} {s_name.readline(x)}")


engine = create_engine('sqlite:///:memory:', echo=True)
connection = engine.connect()
result = engine.execute(datenbank.read())
print(result)

class bibliotheksbenutzer (base):
    __tablename__ = "bibliotheksbenutzer"

    ausweisID = Column(Integer)
    name = Column(String)
    nachname = Column(String)
    straße = Column(String)
    plz = Column(Integer)