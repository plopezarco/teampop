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


def datuak_eguneratu(taulaizena, datuak):
    if taulaizena == "bezeroak":
        bezeroak_eguneratu(datuak)
    elif taulaizena == "ticket":
        ticket_eguneratu(datuak)
    elif taulaizena == "ticket_lerroak":
        ticket_lerroak_eguneratu(datuak)
    elif taulaizena == "produktuak":
        produktuak_eguneratu(datuak)
    elif taulaizena == "banatzailea":
        banatzailea_eguneratu(datuak)
    else:
        print("Taula hori ez da existitzen")


def bezeroak_eguneratu(datuak):
    if len(datuak) == 4:
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE bezeroak SET izena = '" + datuak[1] + "', email = '" + datuak[2] +
                         "', telefonoa = '" + datuak[3] + "' WHERE id_bezeroa = " + datuak[0])
    else:
        print("Ez dituzu datuak ondo sartu")


def ticket_eguneratu(datuak):
    if len(datuak) == 5:
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE ticket SET data = '" + datuak[2] + "', totala = "+ datuak[3]
                         + ", id_banatzailea = " + datuak[4] + " WHERE id_ticket = "+ datuak[0]
                         + " AND id_bezeroa = " + datuak[1])
    else:
        print("Ez dituzu datuak ondo sartu")


def ticket_lerroak_eguneratu(datuak):
    if len(datuak) == 4:
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE ticket_lerroak SET kantitatea = '" + datuak[2] + "', subtotala = '" + datuak[3]
                         + "' WHERE id_ticket = " + datuak[0] + " AND id_produktua = " + datuak[1])
    else:
        print("Ez dituzu datuak ondo sartu")


def produktuak_eguneratu(datuak):
    if len(datuak) == 2:
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE produktuak SET izena = '" + datuak[1] + "', prezioa = " + datuak[2]
                         + " WHERE id_produktua = " + datuak[0])
    else:
        print("Ez dituzu datuak ondo sartu")


def banatzailea_eguneratu(datuak):
    if len(datuak) == 4:
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE banatzailea SET nan = '" + datuak[1] + "', izena = '" + datuak[2]
                         + "', abizena = '" + datuak[3] + "', libre_dago = " + datuak[4]
                         + " WHERE id_banatzailea = " + datuak[0])
    else:
        print("Ez dituzu datuak ondo sartu")


def datuak_ezabatu(taulaizena, datuak):
    if taulaizena == "bezeroak":
        bezeroak_ezabatu(datuak)
    elif taulaizena == "ticket":
        ticket_ezabatu(datuak)
    elif taulaizena == "ticket_lerroak":
        ticket_lerroak_ezabatu(datuak)
    elif taulaizena == "produktuak":
        produktuak_ezabatu(datuak)
    elif taulaizena == "banatzailea":
        banatzailea_ezabatu(datuak)
    else:
        print("Taula hori ez da existitzen")


def bezeroak_ezabatu(datuak):
    if len(datuak) == 1:
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM banatzailea WHERE id_banatzailea = " + datuak[0])
    else:
        print("Ez dituzu datuak ondo sartu")


def ticket_ezabatu(datuak):
    if len(datuak) == 2:
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM ticket WHERE id_ticket = "+ datuak[0] + " AND id_bezeroa = " + datuak[1])
    else:
        print("Ez dituzu datuak ondo sartu")


def ticket_lerroak_ezabatu(datuak):
    if len(datuak) == 2:
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM ticket_lerroak WHERE id_ticket = " + datuak[0] + " AND id_produktua = " + datuak[1])
    else:
        print("Ez dituzu datuak ondo sartu")


def produktuak_ezabatu(datuak):
    if len(datuak) == 1:
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM produktuak WHERE id_produktua = " + datuak[0])
    else:
        print("Ez dituzu datuak ondo sartu")


def banatzailea_ezabatu(datuak):
    if len(datuak) == 1:
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM banatzailea WHERE id_banatzailea = " + datuak[0])
    else:
        print("Ez dituzu datuak ondo sartu")


taulak_irakurri("produktuak")

mydb.close()
