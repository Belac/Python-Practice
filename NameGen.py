import random

x = 0
while x < 100000:
    Type = ["Barbarian","Elf","Wizard","Dragon","Knight"]
    Type = random.choice(Type)

    if Type == "Dragon" or Type == "Barbarian":
        NameSil = ["Og","Bog","Um","Dum","Ope","Hul","Eeg","Qwe","Mal","Oop","Awe","Jak","Dug","Pol","Xen","Zop","Rem","Sum","Uio","Ghu","Al","Ka","Zar"]
        print (random.choice(NameSil)+"-"+random.choice(NameSil)+"-"+random.choice(NameSil), random.choice(NameSil)+"-"+random.choice(NameSil)+"-"+random.choice(NameSil), random.choice(NameSil)+"-"+random.choice(NameSil)+"-"+random.choice(NameSil), random.choice(NameSil)+"-"+random.choice(NameSil)+"-"+random.choice(NameSil), )
        x += 1

    else:
        NameSil = ["Og","Bog","Um","Dum","Ope","Hul","Eeg","Qwe","Mal","Oop","Awe","Jak","Dug","Pol","Xen","Zop","Rem","Sum","Uio","Ghu"]
        Name1 = random.choice(NameSil)
        Name2 = random.choice(NameSil)
        Name2 = Name2.lower()
        Name3 = random.choice(NameSil)
        Name4 = random.choice(NameSil)
        Name5 = random.choice(NameSil)
        Name4 = Name4.lower()
        Name5 = Name5.lower()
        Firstname = Name1+Name2
        Surname = Name3+Name4+Name5
        print (Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname, Firstname+" "+Surname)
        x += 1
