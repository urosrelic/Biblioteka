from Clan import unos_lozinke

KNJIGE = dict()
POLJA = ["ID", "naziv", "autori", "izdavac", "cena", "godina", "primerci"]
TEMPLATE = "{ID:<5}{naziv:40}{autori:30}{izdavac:30}{cena:13}{godina:10}{primerci:12}{stanje:12}"


def unesi_knjigu():
    knjiga = dict()
    for p in POLJA:
        unos = input("Unesite vrednost za polje {}: ".format(p))
        if p == "ID":
            if unos in KNJIGE:
                print("Knjiga sa ID-em {} vec postoji".format(unos))
                knjiga.clear()
                break
        knjiga[p] = unos
    if len(knjiga) > 0:
        knjiga["stanje"] = knjiga["primerci"]
        KNJIGE[knjiga["ID"]] = knjiga
        print("Uspesan unos knjige")
    else:
        print("Knjiga nije uneta.")
    return knjiga


def snimi_biblioteku():
    with open("Knjige.txt", "w") as file:
        for k, v in KNJIGE.items():
            file.write(v["ID"] + "|" + v["naziv"] + "|" + v["autori"] + "|" + v["izdavac"]
                       + "|" + v["cena"] + "|" + v["godina"] + "|" + v["primerci"] + "|" +
                       v["stanje"])


def dodaj_u_fajl(knjiga):
    with open("Knjige.txt", "a") as file:
        file.write(knjiga["ID"] + "|" + knjiga["naziv"] + "|" + knjiga["autori"] + "|" + knjiga["izdavac"] + "|" +
                   knjiga["cena"] + "|" + knjiga["godina"] + "|" + knjiga["primerci"] + "|" +
                   knjiga["stanje"] + "\n")


def ispis_biblioteke():
    header = TEMPLATE.format(ID="ID", naziv="NAZIV", autori="AUTORI",
                             izdavac="IZDAVAC", cena="CENA", godina="GODINA", primerci="UKUPNO", stanje="RASPOLOZIVO")
    print(header)
    print("=" * len(header))
    for knjiga, k in KNJIGE.items():
        knjiga_stampa = TEMPLATE.format(ID=k["ID"], naziv=k["naziv"], autori=k["autori"],
                                        izdavac=k["izdavac"], cena=k["cena"], godina=k["godina"],
                                        primerci=k["primerci"],
                                        stanje=k["stanje"])
        print(knjiga_stampa.strip())
    print("=" * len(header))


def ucitaj_biblioteku():
    with open("Knjige.txt", "r") as f:
        for line in f:
            if line:
                ID, naziv, autori, izdavac, cena, godina, primerci, stanje = line.split("|")
                k = {"ID": ID, "naziv": naziv, "autori": autori,
                     "izdavac": izdavac, "cena": cena, "godina": godina, "primerci": primerci, "stanje": stanje}
                KNJIGE[ID] = k  # Dodeljujemo id recniku KNJIGE, isti id koji se nalazi u recniku k
    print("=" * 152)


def registracija_bibliotekara(korisnicko_ime):
    with open("Clan.txt", "r") as file:
        for f in file:
            name, passw, nivo = f[:-1].split(",")
            if korisnicko_ime == name:
                print("Korisnik vec postoji")
                break
        if korisnicko_ime != name:
            lozinka = unos_lozinke()
            with open("Clan.txt", "a") as file2:
                file2.write(korisnicko_ime + "," + lozinka + "," + "1" + '\n')


def prijava_bibliotekara(korisnicko_ime, lozinka):
    with open("Clan.txt", "r") as file:
        for f in file:
            if f:
                name, passw, nivo = f[:-1].split(",")
                if korisnicko_ime == name:
                    if lozinka == passw:
                        if nivo == "1":
                            return True
            else:
                return False
