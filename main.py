import random

class Character:
    def __init__(self, player,race=None,sex=None,clanName=None, name=None, nickname=None,age=0):
        self.player = player
        self.race = race
        self.sex = sex
        self.age = age
        self.ageGroup = ""
        self.clanName = clanName
        self.name = name
        self.nickname = nickname
        
    def setName(self):
        maleDragonName = ["Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadarr", "Pandjed", "Patrin", "Rhogar", "Shamash", "Shedinn", "Tarhun", "Torinn"]
        femaleDragonName = ["Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Jheri", "Kava", "Korinn", "Mishann", "Nala", "Perra", "Raiann", "Sora", "Surina", "Thava", "Uadjit"]
        clanDragonName = ["Clethtinthiallor", "Daardendrian", "Delmirev", "Drachedandion", "Fenkenkabradon", "Kepeshkmolik", "Kerrhylon", "Kimbatuul", "Linxakasendalor", "Myastan", "Nemmonis", "Norixius", "Ophinshtalajiir", "Prexijandilin", "Shestendeliath", "Turnuroth", "Verthisathurgiesh", "Yarjerit"]
        dragonNickname = ["Climber", "Earbender", "Leaper", "Pious", "Shieldbiter", "Zealous"]
        
        maleDwarfName = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
        femaleDwarfName = ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra"]
        clanDwarfName = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
        
        
        if(self.race == "Dragonborn"):
            if(self.sex == "male"):
                self.name = maleDragonName[random.randint(0,len(maleDragonName) -1)]
            elif(self.sex == "female"):
                self.name = femaleDragonName[random.randint(0,len(femaleDragonName) -1)]
            self.clanName = clanDragonName[random.randint(0,len(clanDragonName)-1)]
            self.nickname = dragonNickname[random.randint(0,len(dragonNickname)-1)]
        
        if(self.race == "Dwarf"):
            if(self.sex == "male"):
                self.name = maleDwarfName[random.randint(0,len(maleDwarfName) -1)]
            elif(self.sex == "female"):
                self.name = femaleDwarfName[random.randint(0,len(femaleDwarfName) -1)]
            self.clanName = clanDwarfName[random.randint(0,len(clanDwarfName)-1)]
    def fullname(self):
        if(self.race == "Dragonborn"):
            return '{} {} the {}'.format(self.clanName, self.name, self.nickname)
        elif(self.race == "Dwarf"):
            return '{} {}'.format(self.clanName, self.name)
        else:
            return '{} {}'.format(self.name, self.clanName)
    
    def setSex(self):
        sex = ["male","female"]
        self.sex = sex[random.randint(0,len(sex) -1)]
    
    def setRace(self):
        #raceList = ["Dragonborn","Dwarf","Elf","Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
        raceList = ["Dragonborn","Dwarf"]
        self.race = raceList[random.randint(0,len(raceList) -1)]
        
    
    def setAge(self):
        if(self.race == "Dragonborn"):
            self.age = random.randint(1,80)
            if(self.age >= 15):
                self.ageGroup = "adult"
            else:
                self.ageGroup = "child"

        if(self.race == "Dwarf"):
            self.age = random.randint(1,350)
            if(self.age >= 50):
                self.ageGroup = "adult"
            else:
                self.ageGroup = "child"
                  
        if(self.race == "Human"):
            self.age = random.randint(1,60)
            if(self.age >= 13):
                self.ageGroup = "adult"
            else:
                self.ageGroup = "child"
    
player1 = Character("Daryn")
player2 = Character("Keegan")
player3 = Character("Felisha", "Human", "female", "Fiona", "Smith")

player1.setRace()
player1.setSex()
player1.setName()
player1.setAge()

player2.setRace()
player2.setSex()
player2.setName()
player2.setAge()

player3.setAge()

print(player1.player + "'s new character is a " + str(player1.age) + " year old " + player1.ageGroup + " " + player1.sex + " " + player1.race + " named " + player1.fullname())
print(player2.player + "'s new character is a " + str(player2.age) + " year old " + player2.ageGroup + " " + player2.sex + " " + player2.race + " named " + player2.fullname())
print(player3.player + "'s new character is a " + str(player3.age) + " year old " + player3.ageGroup + " " + player3.sex + " " + player3.race + " named " + player3.fullname())
