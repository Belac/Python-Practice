"""
Planet of Fightcraft
"""
import random
import ASCII

ASCII.Intro()

print ("                                  ==========  CHARACTER CREATION  ==========")
print ("\n\n")
Player1 = input("                              Player 1 Name: ")
Player1 = Player1.capitalize()
if Player1 == "Trollface":
    Player1 = ASCII.Trollface()
if Player1 == "Noghosts":
    Player1 = ASCII.Ghostbusters()
if Player1 == "Nyan":
    Player1 = ASCII.Nyan()
Type = ["Barbarian","Elf","Wizard","Dragon","Knight"]
Type = random.choice(Type)

Types = (
    {"Barbarian": {"Power": 60, "Special": 80, "Speed": 5}},
    {"Elf": {"Power": 10, "Special": 90, "Speed": 90}},
    {"Wizard": {"Power": 40, "Special": 90, "Speed": 50}},
    {"Dragon": {"Power": 100, "Special": 100, "Speed": 10}},
    {"Knight": {"Power": 50, "Special": 60, "Speed": 50}}
)

if Type == "Dragon" or Type == "Barbarian":
    NameSil = ["Og","Bog","Um","Dum","Ope","Hul","Eeg","Qwe","Mal","Oop","Awe","Jak","Dug","Pol","Xen","Zop","Rem","Sum","Uio","Ghu","Al","Ka","Zar"]
    Char1Name = random.choice(NameSil) + "-" + random.choice(NameSil) + "-" + random.choice(NameSil)
    print("                              Your Character's Name: " + Char1Name)

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
    Char1Name = (Firstname+" "+Surname)
    print ("                              Your Character's Name: "+Char1Name)

Player1Name = Char1Name
Player1Type = Type
print ("                              Your Character's : "+Type)

print ("\n\n")

Player2 = input("                              Player 2 Name: ")
Player2 = Player2.capitalize()
if Player2 == "Troll":
    Player2 = ASCII.Trollface()
if Player2 == "Noghosts":
    Player2 = ASCII.Ghostbusters()
if Player2 == "Nyan":
    Player2 = ASCII.Nyan()
Type = ["Barbarian","Elf","Wizard","Dragon","Knight"]
Type = random.choice(Type)

if Type == "Dragon" or Type == "Barbarian":
    NameSil = ["Og","Bog","Um","Dum","Ope","Hul","Eeg","Qwe","Mal","Oop","Awe","Jak","Dug","Pol","Xen","Zop","Rem","Sum","Uio","Ghu","Al","Ka","Zar"]
    Char2Name = random.choice(NameSil)+"-"+random.choice(NameSil)+"-"+random.choice(NameSil)
    print ("                              Your Character's Name: "+Char2Name)

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
    Char2Name = (Firstname+" "+Surname)
    print ("                              Your Character's Name: "+Char1Name)

Player2Name = Char2Name
Player2Type = Type
print ("                              Your Character's : "+Type)
print ("\n\n\n\n")

player1no = 1
player2no = 0

player1win = 0
player2win = 1

characterfile = open("characterfile.txt", "w+")
characterfile.write("Player 1")
characterfile.write("\n")
characterfile.write("Name: ")
characterfile.write(Player1Name)
characterfile.write("\n")
characterfile.write("Type: ")
characterfile.write(Player1Type)

characterfile.write("\n")
characterfile.write("\n")

characterfile.write("Player 2")
characterfile.write("\n")
characterfile.write("Name: ")
characterfile.write(Player2Name)
characterfile.write("\n")
characterfile.write("Type: ")
characterfile.write(Player2Type)
characterfile.close()

while player1win < 3 and player2win < 3:
    if player2no > player1no:
        player1no = player1no + 1
        player1choice = input("What do you wish to try? (Power/Special/Speed):  ")
        player1choice = player1choice.capitalize()

        player1attack = Types[player1choice]
        print (player1attack)
