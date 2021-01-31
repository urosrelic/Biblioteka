import re


def unos_lozinke():
    while True:
        password = input("Unesite lozinku: ")
        if len(password) < 8:
            print("Sifra mora da ima bar 8 karaktera")
        elif re.search('[0-9]', password) is None:
            print("Mora da sadrzi bar 1 broj")
        elif re.search('[A-Z]', password) is None:
            print("Mora da sadrzi bar 1 veliko slovo")
        else:
            print("--Vasa lozinka je u redu-- ")
            break
    return password


def registracija(korisnicko_ime):
    with open("Clan.txt", "r") as file:
        for f in file:
            name, passw, nivo = f[:-1].split(",")
            if korisnicko_ime == name:
                print("Korisnik vec postoji")
                break
        if korisnicko_ime != name:
            lozinka = unos_lozinke()
            print("Uspesna registracija")
            with open("Clan.txt", "a") as file2:
                file2.write(korisnicko_ime + "," + lozinka + "," + "0" + '\n')


def prijava_clana(korisnicko_ime, lozinka):
    with open("Clan.txt", "r") as file:
        for f in file:
            if f:
                name, passw, nivo = f[:-1].split(",")
                if korisnicko_ime == name:
                    if lozinka == passw:
                        if nivo == "0":
                            return True
            else:
                return False
