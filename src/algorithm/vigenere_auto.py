from src.algorithm import general
from src.algorithm import const

class AutoKeyVigenere:
    def __init__(self, text, key):
        self.text = text
        self.key = key

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
        idxPt = 0
        idxKey = 0
        for char in self.text:
            if(idxKey >= len(self.key)):
                chiper_text += chr(((char + self.text[idxPt]) % 26)+const.LETTER)
                idxPt += 1
            else:
                chiper_text += chr(((char + self.key[idxKey]) % 26)+const.LETTER)
                idxKey += 1

        return chiper_text
  
    def decrypt(self):
        chiper_text = ''
        temp_text = ''
        idx = 0
        for char in self.text:
            if(idx >= len(self.key)):
                self.key += [(ord(i)-const.LETTER) for i in temp_text]
                temp_text = ''
            chiper_text += chr(((char - self.key[idx]) % 26)+const.LETTER)
            temp_text += chr(((char - self.key[idx]) % 26)+const.LETTER)

            idx += 1

        return chiper_text