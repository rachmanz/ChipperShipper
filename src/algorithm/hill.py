from src.algorithm import general
import math
import numpy as np
import json

def is_square(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False

def sqrt(number):
    return int(math.sqrt(number) + 0.5)

def create_n_gram(chars, n):
    ngrams = []
    ngram = []

    chars_append = chars
    chars_mod = len(chars) % n
    if chars_mod != 0:
        chars_append +=  'x' * (n - chars_mod)

    for char in chars_append:
        ngram.append(general.char_to_order(char))

        if len(ngram) == n:
            ngrams.append(ngram)
            ngram = []
    
    return ngrams

class Hill:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def preprocess(self):
        # preprocess key
        try:
            key =  json.loads(self.key)['key']
        except KeyError as err:
            raise Exception(f'required key {err}', 400)
        except Exception as err:
            raise Exception(err.args, 400)
        
        key_length = len(key)
        if not(is_square(key_length)):
            raise Exception("length of key is not perfect square", 400)

        key_sqrt = sqrt(key_length)
        self.key = general.create_square(key, key_sqrt)
        
        # preprocess text
        text = self.text.lower()
        text = general.sanitize(text)
        self.ngrams = create_n_gram(self.text, key_sqrt)

    def encrypt(self):
        chiper_text = ''
        k = np.asmatrix(self.key)
        for ngram in self.ngrams:
            p = np.array(ngram)
            c = np.matmul(k, p).tolist()
            for char in c[0]:
                chiper_text += general.order_to_char(char)
            
        return chiper_text
  
    def decrypt(self):
        chiper_text = ''

        # calculate inverse matrix
        k = np.asmatrix(self.key)
        k_det = round(np.linalg.det(k))
        det_inverse = general.mod_inverse(k_det % 26, 26)
        try: 
            k_inverse = np.linalg.inv(k)
        except np.linalg.LinAlgError:
            raise Exception("this is singular matrix, therefore this matrix doesn't have a determinant", 400)

        k_adjoint = k_inverse * k_det
        self.key = k_adjoint.tolist()

        for col in range(len(self.key)):
            for row in range(len(self.key)):
                self.key[col][row] = round(self.key[col][row])
                self.key[col][row] *= det_inverse
                self.key[col][row] %= 26
        
        for ngram in self.ngrams:
            p = np.array(ngram)
            k = np.asmatrix(self.key)
            c = np.matmul(k, p).tolist()

            for char in c[0]:
                chiper_text += general.order_to_char(char)
            
        return chiper_text
