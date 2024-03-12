from src.algorithm import general
from src.algorithm import const
import math


# Move rotor down
def rotateNext(rotor):
    temp = rotor[len(rotor)-1]
    rotor = rotor[:-1]    
    rotor.insert(0,temp)
    return rotor

# Move rotor up
def rotatePrev(rotor):
    temp = rotor[0]
    rotor.pop(0)    
    rotor.append(temp)
    return rotor

def getSecondElementIdx(rotor,target):
    for pair in rotor:
        if(pair[1] == target):
            return rotor.index(pair)

def getFirstElementIdx(rotor,target):
    for pair in rotor:
        if(pair[0] == target):
            return rotor.index(pair)

class Enigma:
    def __init__(self, text, key):
        self.text = text
        self.key = key
        # self.rotor1 = [(24,21),(25,3),(26,15),(1,1),(2,19),(3,10),(4,14),(5,26),(6,20),(7,8),(8,16),(9,7),(10,22),(11,4),(12,11),(13,5),(14,17),(15,9),(16,12),(17,23),(18,18),(19,2),(20,25),(21,6),(22,24),(23,13)]
        # self.rotor2 = [(26,20),(1,1),(2,6),(3,4),(4,15),(5,3),(6,14),(7,12),(8,23),(9,5),(10,16),(11,2),(12,22),(13,19),(14,11),(15,18),(16,25),(17,24),(18,13),(19,7),(20,10),(21,8),(22,21),(23,9),(24,26),(25,17)]  
        # self.rotor3 = [(1,8),(2,18),(3,26),(4,17),(5,20),(6,22),(7,10),(8,3),(9,13),(10,11),(11,4),(12,23),(13,5),(14,24),(15,9),(16,12),(17,25),(18,16),(19,19),(20,6),(21,15),(22,21),(23,2),(24,7),(25,1),(26,14)]  
        # self.rotor4 = [(3,11),(4,13),(5,17),(6,15),(7,19),(8,2),(9,4),(10,10),(11,8),(12,6),(13,21),(14,24),(15,22),(16,23),(17,26),(18,25),(19,12),(20,16),(21,14),(22,18),(23,20),(24,1),(25,3),(26,5),(1,7),(2,9)]  

        # self.rotor5 = [(1,2),(2,3),(3,1)]        
        # self.rotor6 = [(2,3),(3,1),(1,2)]    
        # self.rotor = [[(1,3),(2,5),(3,1),(4,2),(5,4)],        
        #             [(3,5),(4,1),(5,2),(1,4),(2,3)]]

        self.rotor = [[(24,21),(25,3),(26,15),(1,1),(2,19),(3,10),(4,14),(5,26),(6,20),(7,8),(8,16),(9,7),(10,22),(11,4),(12,11),(13,5),(14,17),(15,9),(16,12),(17,23),(18,18),(19,2),(20,25),(21,6),(22,24),(23,13)],
                        [(26,20),(1,1),(2,6),(3,4),(4,15),(5,3),(6,14),(7,12),(8,23),(9,5),(10,16),(11,2),(12,22),(13,19),(14,11),(15,18),(16,25),(17,24),(18,13),(19,7),(20,10),(21,8),(22,21),(23,9),(24,26),(25,17)]  ,
                        [(1,8),(2,18),(3,26),(4,17),(5,20),(6,22),(7,10),(8,3),(9,13),(10,11),(11,4),(12,23),(13,5),(14,24),(15,9),(16,12),(17,25),(18,16),(19,19),(20,6),(21,15),(22,21),(23,2),(24,7),(25,1),(26,14)]  ,
                        [(3,11),(4,13),(5,17),(6,15),(7,19),(8,2),(9,4),(10,10),(11,8),(12,6),(13,21),(14,24),(15,22),(16,23),(17,26),(18,25),(19,12),(20,16),(21,14),(22,18),(23,20),(24,1),(25,3),(26,5),(1,7),(2,9)]  ]

    def moveForward(self,count):
        if(count % math.pow(const.LENGTHALPHABET,3) == 0):
            self.rotor[0] = rotateNext(self.rotor[0])
        if(count % math.pow(const.LENGTHALPHABET,2) == 0):
            self.rotor[1] = rotateNext(self.rotor[1])            
        if(count % math.pow(const.LENGTHALPHABET,1) == 0):
            self.rotor[2] = rotateNext(self.rotor[2])
        self.rotor[3] = rotateNext(self.rotor[3])

    def moveBackward(self,count):
        if(count % math.pow(const.LENGTHALPHABET,3) == 0):
            self.rotor[0] = rotatePrev(self.rotor[0])
        if(count % math.pow(const.LENGTHALPHABET,2) == 0):
            self.rotor[1] = rotatePrev(self.rotor[1])            
        if(count % math.pow(const.LENGTHALPHABET,1) == 0):
            self.rotor[2] = rotatePrev(self.rotor[2])
        self.rotor[3] = rotatePrev(self.rotor[3])

    def preprocess(self):
        # Preprocess text
        text = self.text.lower()
        text = general.sanitize(text)
        self.text = [(ord(i)-const.LETTER) for i in text]
                
    def encrypt(self):
        
        chiper_text = ''
        count = 0
        for char in self.text:
            x = 0
            row = char
            for rotor in self.rotor:
                x = rotor[row][0]
                row = getSecondElementIdx(rotor,x)
            chiper_text += chr((row)+const.LETTER)
            count += 1            
            self.moveForward(count)

        print(count)
        return chiper_text
  
    def decrypt(self):
        chiper_text = ''        
        count = len(self.text)
        for i in range(1,len(self.text)):
            self.moveForward(i)

        for char in reversed(self.text):
            y = 0
            row = char
            for rotor in reversed(self.rotor):
                y = rotor[row][1]
                row = getFirstElementIdx(rotor,y)
            chiper_text += chr((row)+const.LETTER)
            count -= 1       
            self.moveBackward(count)

        return chiper_text[::-1]