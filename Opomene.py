import datetime

from Bibliotekar import *


def nadji_zaduzenja(korisnicko_ime):
    # Pronalazi samo zaduzenja (status=0) za odredjenog korisnika ili za sve korisnike, po potrebi.
    zaduzenja = dict()
    with open("Pozajmice.txt", "r") as file:
        brojac = 0
        for f in file:
            id_knjige, korisnik, zaduzenje, razduzenje, vraceno, status = f[:-1].split("|")
            # Trazim samo zaduzenja (status 0)-------------------------
            if status == "0":
                trazi = True
                # Ako je prosledjeni korisnik prazan onda trazi zaduzenja za sve korisnike------------------
                if korisnicko_ime != "":
                    # Ako se traze zaduzenja za konkretnog korisnika, preskoci ako to nije taj korisnik---------
                    if korisnicko_ime == korisnik:
                        trazi = True
                    else:
                        trazi = False
            else:
                #  Ovo nije status 0, preskoci ga
                trazi = False
            #  --------------------------------------------------------------------------------------------------
            if trazi:
                brojac += 1
                zaduzenja[brojac] = {"id_knjige": id_knjige, "korisnik": korisnik,
                                     "naziv": KNJIGE[id_knjige]["naziv"], "zaduzenje": zaduzenje,
                                     "razduzenje": razduzenje, "vraceno": vraceno, "status": status}
    return zaduzenja


def opomene(korisnicko_ime):
    recnik = dict()
    recnik = nadji_zaduzenja(korisnicko_ime)
    today = datetime.date.today()
    for k, v in recnik.items():
        datum_razduzenja = datetime.datetime.strptime(v["razduzenje"], "%Y-%m-%d").date()
        if today > datum_razduzenja:
            print("Opomena: Korisnik " + v["korisnik"] + " nije vratio knjigu pod id-em " + v["id_knjige"] + ": '" + v[
                "naziv"] + "'")
        else:
            print("Korisnik " + v["korisnik"] + " ne kasni za vracanje knjige pod id-em " + v["id_knjige"] + ": '"
                  + v["naziv"] + "'")
