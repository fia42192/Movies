from names import name
import sys
import time
import random

Náš_pan_učitel = ["Jaroslav", "Krbec", "Jarda"]
rovna_se = "=============================================================="
dostupne_filmy = ["Shawshank Redemption", "The Godfather", "The Dark Knight", "The Prestige", "Forrest Gump", "Green Mile", "Seven", "Flight over the cuckoo's nest", "Schindler's list", "Once Upon a Time in the West"]
sály = random.randint(1, 10)

filmy = {
    "Shawshank Redemption":{
        "Year": 1994,
        "Leading actor": "Tim Robbins",
        "Nation": "USA",
        "Running time": "142 minutes"
    },


    "The Godfather":{
        "Year": 1972,
        "Leading actor": "Marlon Brando",
        "Nation": "USA",
        "Running time": "175 minutes",
    },


    "The Dark Knight":{
        "Year": 2008,
        "Leading actor": "Christian Bale",
        "Nation": "USA/GB",
        "Running time": "152 minutes"
    },


    "The Prestige":{
        "Year": 2006,
        "Leading actor": "Chrisitan Bale",
        "Nation": "USA/GB",
        "Running time": "130 minutes"
    },


    "Forrest Gump":{
        "Year": 1994,
        "Leading actor": "Tom Hanks",
        "Nation": "USA",
        "Running time": "142 minutes"
    },


    "Green Mile":{
        "Year": 1999,
        "Leading actor": "Tom Hanks",
        "Nation": "USA",
        "Running time": "188 minutes"
    },


    "Seven":{
        "Year": 1995,
        "Leading actor": "Brad Pitt",
        "Nation": "USA",
        "Running time": "127 minutes"
    },


    "Flight over the cuckoo's nest":{
        "Year": 1975,
        "Leading actor": "Jack Nicholson",
        "Nation": "USA",
        "Running time": "133 minutes"
    },


    "Schindler's list":{
        "Year": 1993,
        "Leading actor": "Liam Neeson",
        "Nation": "USA",
        "Running time": "195 minutes"
    },


    "Once Upon a Time in the West":{
        "Year": 1968,
        "Leading actor": "Henry Fonda",
        "Nation": "USA/Italy",
        "Running time": "166 minutes"
    }
}

jmeno = input("ZADEJ JMÉNO: ")
if jmeno in name:
    print("V POŘÁDKU")
if jmeno in Náš_pan_učitel:
    print("Vy jste u nás samozřejmě vítán pane učiteli!")
if jmeno not in name and jmeno not in Náš_pan_učitel:
    print("Takové jméno není na seznamu hostů")
    sys.exit()

time.sleep(0.5)

print("\n")
print(rovna_se)
print("               VÍTEJTE V NAŠEM FILMOVÉM SLOVNÍKU               ")
print(rovna_se)
print("        dostupné filmy | detaily filmu | doporuč film         ")
print(rovna_se)
výběr = str(input("Vyberte jednu z možností: "))

if výběr == "dostupné filmy":
    time.sleep(0.5)
    print("\nMomentálně dostupné filmy:")
    print(*dostupne_filmy, sep=', ')
    vyber_filmu = str(input("Jaký film by sis chtěl vybrat z nabídky? "))
    
    if vyber_filmu in dostupne_filmy:
        print(f"Pokračujte do sálu číslo {sály}, přeji hezkou podívanou.")
        sys.exit()

    else:
        print("Takový film u nás není, přeji pěkný den.")
        sys.exit()

if výběr == "detaily filmu":
    print("\nNaše filmy:")
    print(*dostupne_filmy, sep=', ')
    vyber_filmu_2 = str(input("O jakém filmu by ses chtěl dozvědět detaily? "))
    
    time.sleep(1)

    if vyber_filmu_2 not in dostupne_filmy:
        print("Takový film u nás není, přeji pěkný den.")
        sys.exit()
    
    if vyber_filmu_2 in dostupne_filmy:
        time.sleep(0.3)
        film_detaily = filmy[vyber_filmu_2]
        for key, value in film_detaily.items():
            print(f"{key}: {value}")
        ano_ne = str(input("Chceš jít na tento film?(ano/ne) "))
        if ano_ne == "ano":
            time.sleep(0.5)
            print(f"Pokračujte do sálu číslo {sály}, přeji hezkou podívanou.")
            sys.exit()
        elif ano_ne == "ne":
            time.sleep(0.5)
            print("V tom případě odejdi.")
            sys.exit()
        else:
            print("Taková možnost neexistuje.")
            sys.exit()

if výběr == "doporuč film":
    doporučený_film = random.choice(dostupne_filmy)
    print(f"Doporučuji ti jít na {doporučený_film}, sál číslo {sály}")
    ano_ne_2 = str(input("Chceš jít na tento doporučený film?(ano/ne)"))
    if ano_ne_2 == "ano":
        time.sleep(0.5)
        print(f"Pokračujte tedy do sálu, přeji hezkou podívanou.")
        sys.exit()
    elif ano_ne_2 == "ne":
        time.sleep(0.5)
        print("V tom případě odejdi.")
        sys.exit()
    else:
        print("Taková možnost neexistuje.")
        sys.exit()

