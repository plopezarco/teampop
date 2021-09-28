import pymysql

mydb = pymysql.connect(
    host="192.168.73.56",
    port=3308,
    user="erronka",
    password="1234",
    database="okindegia"
)


# taulak: bezeroak, ticket, ticket_lerroak, produktuak, banatzailea

def taulak_irakurri(taulaizena):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM " + taulaizena)
    taula = mycursor.fetchall()
    print(taulaizena + ":")
    print(taula)


def taulak_bete(taulaizena, datuak):
    if taulaizena == "bezeroak":
        bezeroak_bete(datuak)
    elif taulaizena == "ticket":
        ticket_bete(datuak)
    elif taulaizena == "ticket_lerroak":
        ticket_lerroak_bete(datuak)
    elif taulaizena == "produktuak":
        produktuak_bete(datuak)
    elif taulaizena == "banatzailea":
        banatzailea_bete(datuak)
    else:
        print("Taula hori ez da existitzen")


def bezeroak_bete(datuak):
    if len(datuak) == 3:
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO bezeroak (izena, email, telefonoa) VALUES ('" + datuak[0]
                         + "', '" + datuak[1] + "', '" + datuak[2] + "')")
    else:
        print("Ez dituzu datuak ondo sartu")


def ticket_bete(datuak):
    if len(datuak) == 4:
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO ticket (id_bezeroa, data, totala, id_banatzailea) VALUES ("
                         + datuak[0] + ", '" + datuak[1] + "', "
                         + datuak[2] + ", " + datuak[3] + ")")
    else:
        print("Ez dituzu datuak ondo sartu")


def ticket_lerroak_bete(datuak):
    if len(datuak) == 4:
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO ticket_lerroak (id_ticket, id_produktua, kantitatea, subtotala) VALUES ("
                         + datuak[0] + ", " + datuak[1] + ", '"
                         + datuak[2] + "', '" + datuak[3] + "')")
    else:
        print("Ez dituzu datuak ondo sartu")


def produktuak_bete(datuak):
    if len(datuak) == 2:
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO produktuak (izena, prezioa) VALUES ('" + datuak[0] + "', "
                         + datuak[1] + ")")
    else:
        print("Ez dituzu datuak ondo sartu")


def banatzailea_bete(datuak):
    if len(datuak) == 4:
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO banatzailea (nan, izena, abizena, libre_dago) VALUES ('"
                         + datuak[0] + "', '" + datuak[1] + "', '"
                         + datuak[2] + "', " + datuak[3] + ")")
    else:
        print("Ez dituzu datuak ondo sartu")


def datuak_eguneratu():
    mycursor = mydb.cursor()


def datuak_ezabatu():
    mycursor = mydb.cursor()


taulak_irakurri("produktuak")

mydb.close()
