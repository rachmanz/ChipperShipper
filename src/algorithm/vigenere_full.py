from src.algorithm import general
from src.algorithm import const

class FullVigenere:
    def __init__(self, text, key):
        self.text = text
        self.key = key
        self.matrices_sollution =[
            ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],    
            ['t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o'],#a
            ['b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t'],#b
            ['g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b'],#c
            ['u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g'],#d
            ['k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u'],#e
            ['f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k'],#f
            ['c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f'],#g
            ['r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c'],#h
            ['w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r'],#i
            ['j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w'],#j
            ['e','l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j'],#k
            ['l','p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e'],#l
            ['p','n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l'],#m
            ['n','z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p'],#n
            ['z','m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n'],#o
            ['m','q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z'],#p
            ['q','h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m'],#q
            ['h','s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q'],#r
            ['s','a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h'],#s
            ['a','d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s'],#t
            ['d','v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a'],#u
            ['v','i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d'],#v
            ['i','x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v'],#w
            ['x','y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i'],#x
            ['y','o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x'],#y
            ['o','t','b','g','u','k','f','c','r','w','j','e','l','p','n','z','m','q','h','s','a','d','v','i','x','y']]#z            

    def preprocess(self):
        # Preprocess text
        text = self.text.lower()
        text = general.sanitize(text)
        self.text = [(ord(i)-const.LETTER) for i in text]
                
        # Preprocess key
        key = self.key.lower()
        key = general.sanitize(key)
        self.key = [(ord(i)-const.LETTER) for i in key]

    def encrypt(self):
        chiper_text = ''
        idx = 0
        for char in self.text:
            if(idx >= len(self.key)):
                idx = 0
            chiper_text += self.matrices_sollution[char][self.key[idx]]
            idx += 1

        return chiper_text

    def decrypt(self):
        chiper_text = ''
        idx = 0
        for char in self.text:
            if(idx >= len(self.key)):
                idx = 0
                        
            element = chr(char + const.LETTER)
            chiper_text += chr(self.matrices_sollution[self.key[idx]].index(element) + const.LETTER)
            idx += 1

        return chiper_text