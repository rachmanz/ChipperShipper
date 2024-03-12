from src.algorithm import general
from src.algorithm import const
from src.algorithm.vigenere import Vigenere
import math
import numpy as np

#Create a matrices from a number sequence with max col = length
# example: [4, 7, 13, 3, 1, 22, 11, 224, 18, 20, 15, 224, 18, 18, 17, 224]
# return : [[4, 7, 13, 3], 
#           [1, 22, 11, 224],
#           [18, 20, 15, 224],
#           [18, 18, 17, 224]]

def split_len(seq, length):
    matrices = [seq[i:i + length] for i in range(0, len(seq), length)]
    nRow = math.ceil(len(seq)/length)
    lengthLastRow = len(matrices[nRow-1])
    if(lengthLastRow != length):
        for i in range(0,(length-lengthLastRow)):
            matrices[nRow-1].append(const.SENTINEL)
    return matrices

class SuperEncryption:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def preprocess(self):
        # Preprocess text
        # Done in encrypt and decrypt function for special purpose
                
        # Preprocess key
        key = self.key.lower()
        key = general.sanitize(key)
        self.key = [(ord(i)-const.LETTER) for i in key]

    def encrypt(self):
        chiper_text = ''
        
        #Preprocess text
        text = self.text.lower()
        text = general.sanitize(text)
        self.text = [(ord(i)-const.LETTER) for i in text]

        #Encrypt phase
        vig = Vigenere(self.text,self.key).encrypt()

        ord_vig = [(ord(i)-const.LETTER) for i in vig]
        matrices = split_len(ord_vig,const.TRANSPOSEKEY)
        transpose = np.transpose(matrices)

        for row in transpose:
            for col in row:
                if(col != const.SENTINEL):                
                    chiper_text += general.order_to_char(col)
                else:
                    chiper_text += chr(col)

        return chiper_text
  
    def decrypt(self):
        chiper_text = ''

        #Preprocess text
        text = []        
        for i in self.text:
            if(i != chr(const.SENTINEL)):
                text.append(ord(i)-const.LETTER)
            else:
                text.append(const.SENTINEL)

        #Decrypt phase
        nRow = int(len(text)/const.TRANSPOSEKEY)
        matrices = split_len(text,nRow)
        transpose = np.transpose(matrices)

        for row in transpose:
            for col in row:
                if(col != const.SENTINEL):                
                    chiper_text += general.order_to_char(col)

        chiper_text = [(ord(i)-const.LETTER) for i in chiper_text]
        vig = Vigenere(chiper_text,self.key).decrypt()        

        return vig