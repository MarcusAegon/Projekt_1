"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Marek Žemlička
email: mara.bello@seznam.cz
discord: marcusaegon
"""

TEXTS = """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""



registrovani_uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

while True:
        uzivatel = input("Enter your username: ")
        heslo = input("Enter your password: ")

        if uzivatel in registrovani_uzivatele and registrovani_uzivatele[uzivatel] == heslo:
            print("Login successful. Welcome,", uzivatel)
            break 
        else:
            print("Invalid username or password. Exiting the program.")
            exit()

cara = '-' * 50

print(cara)
print ("We have 3 texts to be analyzed.")
print(cara)

while True:
    volba = int(input("Choose your text (1-3): "))
    if 1 <= volba <= 3:
        vybrany_text = TEXTS[volba - 1]
        break
    else:
                    print("Wrong number. Exiting the program")
                    quit ()

slova = TEXTS.split()
delka_slov = [len(slovo.strip(".,:;!?_")) for slovo in slova]
delka_slov_pocet = {}

for delka in delka_slov:
        if delka not in delka_slov_pocet:
            delka_slov_pocet[delka] = 1
        else:
            delka_slov_pocet[delka] += 1

psane_velkymi_pismeny = [slovo for slovo in slova if slovo.isupper()]
psane_malymi_pismeny = [slovo for slovo in slova if slovo.islower()]
prvni_velke_pismeno = [slovo for slovo in slova if slovo.istitle()]
cisla = [slovo for slovo in slova if slovo.isdigit()]
soucet_cisel = sum(int(cislo) for cislo in cisla)


print(cara)
print(f"There are {len(slova)} words in the selected text")
print(f"There are {len(prvni_velke_pismeno)} titlecase words.")
print(f"There are {len(psane_velkymi_pismeny)} uppercase words.")
print(f"There are {len(psane_malymi_pismeny)} lowercase words.")
print(f"There are {len(cisla)} numeric strings.")
print(f"The sum of all the numbers: {soucet_cisel}")
print(cara)

print(cara)
print("\nFrequency of word lengths:")
for delka, pocet in sorted(delka_slov_pocet.items()):
        print(f"{delka}: {'*' * pocet}")
print(cara)
