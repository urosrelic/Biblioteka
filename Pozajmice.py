import datetime

import matplotlib.pyplot as plt

from Bibliotekar import *

dat_zad = datetime.date.today()
dat_vrac = dat_zad + datetime.timedelta(days=7)


def grafikon():
    datum = []
    datum_brojac = []
    with open("Pozajmice.txt", "r") as file:
        for f in file:
            id_knjige, korisnik, zaduzenje, razduzenje, vraceno, status = f[:-1].split("|")
            datum_zaduzenje = datetime.datetime.strptime(zaduzenje, '%Y-%m-%d')
            datum_zaduzenje = datetime.datetime.strftime(datum_zaduzenje, "%m-%d")
            datum.append(datum_zaduzenje)
    for d in datum:
        brojac = datum.count(d)
        datum_brojac.append(brojac)
    plt.bar(datum, datum_brojac)
    plt.title("Grafikon")
    plt.xlabel("Datum")
    plt.ylabel("Broj knjiga zaduzen po datumu")
    plt.show()


def ucitaj_pozajmice():
    # Ucitava iz pozajmice.txt sve pozajmice u dictionary i vraca ga kao rezultat
    pozajmice = dict()
    with open("Pozajmice.txt", "r") as file:
        brojac = 0
        for f in file:
            id_knjige, korisnik, zaduzenje, razduzenje, vraceno, status = f[:-1].split("|")
            brojac += 1
            pozajmice[brojac] = {"id_knjige": id_knjige,
                                 "korisnik": korisnik,
                                 "zaduzenje": zaduzenje,
                                 "razduzenje": razduzenje,
                                 "vraceno": vraceno,
                                 "status": status}
    return pozajmice


def snimi_pozajmice(recnik):
    # Snima u pozajmice.txt ceo prosledjen dictionary
    with open("Pozajmice.txt", "w") as file:
        for k, v in recnik.items():
            file.write(v["id_knjige"] + "|" +
                       v["korisnik"] + "|" +
                       v["zaduzenje"] + "|" +
                       v["razduzenje"] + "|" +
                       v["vraceno"] + "|" +
                       v["status"] + "\n")


def zaduzi_knjigu(id_knjige, korisnicko_ime):
    #
    # Zaduzuje korisnika za knjigu.
    # Korisnik moze da zaduzi jos jedan primerak knjige koju je vec uzeo, a nije je jos vratio.
    #
    with open("Pozajmice.txt", "a") as file:  # Radi append u txt fajl
        file.write(id_knjige + "|" + korisnicko_ime + "|" + str(dat_zad) + "|" + str(dat_vrac) + "|" + "|" + "0" + "\n")
        # Status 0 oznacava da je korisnik zaduzen
    # Smanji trenutno stanje knjige u "Knjige" dictionary
    KNJIGE[id_knjige]["stanje"] = str(int(KNJIGE[id_knjige]["stanje"]) - 1) + "\n"
    snimi_biblioteku()  # Snimi izmene u knjige.txt
    print("Uspesno zaduzivanje knjige pod id-em ", id_knjige)
    print("Molimo vas da knjigu vratite " + str(dat_vrac))


def vrati_knjigu(id_knjige, korisnicko_ime):
    #
    # Razduzuje korisnika za knjigu.
    # Ako korisnik ima trenutno zaduzeno vise primeraka iste knjige, razduzice prvu koju nadje.
    #
    recnik = dict()
    if id_knjige in KNJIGE:
        # Povecaj trenutno stanje knjige u "Knjige" dictionary
        KNJIGE[id_knjige]["stanje"] = str(int(KNJIGE[id_knjige]["stanje"]) + 1) + "\n"
        snimi_biblioteku()  # Snimi izmene u knjige.txt
        recnik = ucitaj_pozajmice()  # Ucitaj sve pozajmice - ceo txt fajl
        for k, v in recnik.items():  # Nadji poziciju trazene pozajmice u recniku
            if v["id_knjige"] == id_knjige and v["korisnik"] == korisnicko_ime and v["status"] == "0":
                v["vraceno"] = str(dat_zad)  # Popuni datum vracanja (tekuci datum)
                v["status"] = "1"  # Izmeni status na 1 - razduzeno
                break  # izadji da ne bi menjao sva zaduzenja za tog korisnika i tu knjigu (mozda ih ima vise)
        snimi_pozajmice(recnik)  # Snimi nazad u txt fajl
        print("Uspesno vracanje knjige")

    else:
        print("Uneli ste pogresan id knjige")
