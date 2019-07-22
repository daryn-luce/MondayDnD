import random

class Character:
    
    def __init__(self, player,race=None,sex=None,familyName=None, name=None, nickname=None,age=0):
        self.player = player
        self.race = race
        self.sex = sex
        self.age = age
        self.ageGroup = ""
        self.familyName = familyName
        self.name = name
        self.nickname = nickname
        
        
    def setName(self):
        maleNames = self.lines[0].split(', ')
        femaleNames = self.lines[1].split(', ')
        familyName = self.lines[2].split(', ')
        
        if(self.sex == 'male'):
            self.name = maleNames[random.randint(0,len(maleNames) - 1)]
        elif(self.sex == 'female'):
            self.name = femaleNames[random.randint(0,len(femaleNames) - 1)]
        self.familyName = familyName[random.randint(0,len(familyName) - 1)]
        
        if(self.lines[3] != '-'):
            childNames = self.lines[3].split(', ')
            self.name = childNames[random.randint(0,len(childNames) - 1)]
        
    def fullname(self):
        return '{} {}'.format(self.name, self.familyName)
    
    def setSex(self):
        sex = ["male","female"]
        self.sex = sex[random.randint(0,len(sex) -1)]
    
    def setRace(self):
        race = ['Dwarf','Elf','Halfling']
        self.race = race[random.randint(0,len(race) -1)]
        
    def setSubRace(self):
        subrace = self.lines[8].split(', ')
        self.subrace = subrace[random.randint(0,len(subrace) - 1)]
    
    def setAge(self):
        
        ageList = self.lines[4].split(':')
        self.age = random.randint(1,int(ageList[1]))
        if(self.age >= int(ageList[0])):
            self.ageGroup = "adult"
        else:
            self.ageGroup = "child"
    
    def openFile(self):
        filepath = self.race + '.txt'
        
        self.lines = []
        for line in open(filepath):
            self.lines.append(line.rstrip('\n'))

    
    
player1 = Character("Daryn")
player1.setRace()
player1.openFile()
player1.setSubRace()
player1.setAge()
player1.setSex()
player1.setName()


print(player1.player + "'s new character is a " + str(player1.age) + " year old " + player1.ageGroup + " " + player1.sex + " " + player1.race + " of the " + player1.subrace + " race named " + player1.fullname())
