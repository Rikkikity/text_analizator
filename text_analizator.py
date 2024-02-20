"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiří Albrecht

email: albrecht1994@seznam.cz

discord: Rikkiti#3029

"""

# proměne programu

separator = "----------------------------------------"
data_uzivatel = {"bob":"123", "ann":"pass123",
                  "mike":"password123", "liz":"pass123"}

TEXTS = ['''
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
garpike and stingray are also present.'''
]

# vyžádání jména a hesla a jeho porovnání
uzivatel = input("username:")
heslo = input("password:")
print(separator)
if uzivatel in data_uzivatel and heslo == data_uzivatel[uzivatel]:
    print(f"""
Welcome to the app, {uzivatel}
We have 3 texts to be analyzed.
""")
elif uzivatel not in data_uzivatel:
    print("Wrong username, terminating the program..")
    exit()
elif uzivatel in data_uzivatel and heslo != data_uzivatel[uzivatel]:
    print("Wrong password, terminating the program..")
    exit()
else:
    print("unregistered user, terminating the program..")
    exit()
print(separator)
# vybrání typů textu mezi třemi možnostmi
uziv_typ_textu = int((input("Enter a number btw. 1 and 3 to select:")))
if not str(uziv_typ_textu).isdigit():
    print("wrong type of input -> must be number, terminating the program..")
    exit()
elif not uziv_typ_textu in range(1,len(TEXTS)):
    print("wrong value of number, terminating the program..")
    exit()

reseny_text = TEXTS[uziv_typ_textu -1]

# STATISTIKY
# počet slov
split_textu = reseny_text.split()
ocisteny_text = []
for slovo in split_textu:
    ocisteny_text.append(slovo.strip(",.!?;")) 
print(f"There are {len(ocisteny_text)} words in the selected text")


pocet_slov_s_vemlkym_pismenem = 0
pocet_slov_s_vemlkymi_pismeneny = 0
pocet_slov_s_malimy_pismeneny = 0
pocet_cisel = 0
suma_cisel = 0

#pozbirání dat sloupcového grafu
suma_delek_slov = {}

for slovo in ocisteny_text:
    # počet slov začínajících velkým písmenem
    if slovo[0].isupper() and slovo.isalpha():
        pocet_slov_s_vemlkym_pismenem += 1

    # počet slov psaných velkými písmeny,
    if slovo.isupper() and slovo.isalpha():
            pocet_slov_s_vemlkymi_pismeneny += 1
    
    # počet slov psaných malými písmeny,
    if slovo.islower() and slovo.isalpha():
            pocet_slov_s_malimy_pismeneny += 1

    # počet čísel (ne cifer)
    if slovo.isdigit():
        pocet_cisel += 1   

    # sumu všech čísel (ne cifer) v textu.
    if slovo.isdigit():
            suma_cisel += int(slovo)

    #pozbirání dat sloupcového grafu
    if len(slovo) not in suma_delek_slov:
        suma_delek_slov[len(slovo)]=1
    elif len(slovo) in suma_delek_slov:
        suma_delek_slov[len(slovo)]+=1            

print(f"There are {pocet_slov_s_vemlkym_pismenem} titlecase words.")    
print(f"There are {pocet_slov_s_vemlkymi_pismeneny} uppercase words.")
print(f"There are {pocet_slov_s_malimy_pismeneny} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.") 
print(f"The sum of all the numbers {suma_cisel}")


#KONEC STATISTIK
print(separator)

# sloupcovy graf
delka_nadpis = "LEN"
hvezdicky = "  OCCURENCES  "
cetnost_nadpis = "NR."
print(delka_nadpis, hvezdicky, cetnost_nadpis, sep="|")
print(separator)


#generování sloupcovýho grafu
for delka in sorted(suma_delek_slov):
    
    print(str(delka).rjust(len(delka_nadpis)), 
          ("*"*delka).ljust(len(hvezdicky)), 
          suma_delek_slov[delka], sep = "|")  



