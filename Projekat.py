from Meni import *


def main():
    datum = datetime.date.today()
    print("==== Dobrodosli u biblioteku! ==== ")
    print("Danasnji datum je: " + str(datum))
    print("Molimo vas da izaberete jednu od sledecih opcija")
    stampaj_opcije()
    while True:
        unos = input()
        if unos == "1":
            izbor_jedan()
        elif unos == "2":
            izbor_dva()
        elif unos == "3":
            izbor_tri()
        elif unos == "4":
            izbor_cetiri()
        elif unos == "5":
            grafikon()
            stampaj_opcije()
        elif unos == "6":
            print("Dovidjenja!")
            break
        else:
            print("Unesite validnu opciju")
            stampaj_opcije()


if __name__ == '__main__':
    main()

