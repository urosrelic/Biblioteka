from Clan import *
from Opomene import *
from Pozajmice import *


def stampaj_opcije():
    print("=" * 30)
    print("1. Registracija korisnika")
    print("2. Prijava korisnika")
    print("3. Bibliotekar")
    print("4. Registracija bibliotekara")
    print("5. Grafikon")
    print("6. Izlazak iz programa")
    print("=" * 30)


def izbor_jedan():
    print("==== Izabrali ste opciju registracija korisnika ====")
    korisnicko_ime = input("Unesite zeljeno korisnicko ime: ")
    registracija(korisnicko_ime)
    stampaj_opcije()


def izbor_dva():
    print("==== Izabrali ste opciju prijava korisnika ====")
    korisnik = input("Unesite korisnicko ime: ")
    lozinka = input("Unesite lozinku: ")
    if prijava_clana(korisnik, lozinka):
        print("==== Dobrodosli nazad " + korisnik + " ====")
        ucitaj_biblioteku()
        while True:
            print("1. Zaduzi knjigu")
            print("2. Vrati knjigu")
            print("3. Odjavite se")
            user_input = input()
            if user_input == "1":
                ispis_biblioteke()
                id_knjige = input("Unesite id knjige: ")
                if id_knjige in KNJIGE:
                    if int(KNJIGE[id_knjige]["stanje"]) > 0:
                        zaduzi_knjigu(id_knjige, korisnik)
                    else:
                        print("Svi primerci trazene knjige su zauzeti.")
                else:
                    print("Pogresan unos")
            elif user_input == "2":
                recnik = dict()
                recnik = nadji_zaduzenja(korisnik)
                if len(recnik) > 0:
                    print("Vase zaduzene knjige su: ")
                    for k, v in recnik.items():
                        print("ID knjige: " + v["id_knjige"], "Naziv: " + v["naziv"])
                    id_knjige = input("Unesite id knjige: ")
                    if id_knjige != "":
                        nadjeno = False
                        for k, v in recnik.items():
                            if id_knjige in v["id_knjige"]:
                                nadjeno = True
                                break
                        if nadjeno:
                            vrati_knjigu(id_knjige, korisnik)
                        else:
                            print("Nije validan id knjige")
                else:
                    print("Nemate zaduzenih knjiga")
            elif user_input == "3":
                print("Uspesna odjava")
                stampaj_opcije()
                break
    else:
        print("Ne nalazite se u sistemu molimo vas da se registrujete ")
        stampaj_opcije()


def izbor_tri():
    print("==== Izabrali ste opciju bibliotekar ====")
    korisnik = input("Unesite korisnicko ime: ")
    lozinka = input("Unesite lozinku: ")
    if prijava_bibliotekara(korisnik, lozinka):
        print("==== Dobrodosli nazad " + korisnik + " ====")
        while True:
            print("1. Unesi knjigu")
            print("2. Izdaj opomene")
            print("3. Odjavite se")
            user_input = input()
            if user_input == "1":
                ucitaj_biblioteku()
                ispis_biblioteke()
                knjiga = unesi_knjigu()
                if len(knjiga) > 0:  # Ako je knjiga uspesno uneta
                    dodaj_u_fajl(knjiga)
            elif user_input == "2":
                ucitaj_biblioteku()
                ime = input(
                    "Unesite ime korisnika za koga stampate opomene ('Enter' za sve korisnike): ")
                opomene(ime)
            elif user_input == "3":
                print("Uspesna odjava")
                stampaj_opcije()
                break
    else:
        print("Proverite unos korisnickog imena i lozinke")
        stampaj_opcije()


def izbor_cetiri():
    korisnicko_ime = input("Unesite korisnicko ime: ")
    registracija_bibliotekara(korisnicko_ime)
    stampaj_opcije()
