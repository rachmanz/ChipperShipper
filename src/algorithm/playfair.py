from src.algorithm import general
from src.algorithm import const

def create_bigram(text):
    bigrams = []
    bigram = ''
    for char in text:
        if bigram == '':
            bigram += char
        else:
            if bigram == char and bigram != 'x':
                bigram += 'x'
                bigrams.append(bigram)
                bigram = char
            else:
                bigram += char
                bigrams.append(bigram)
                bigram = ''

    if bigram != '':
       bigram += 'x'
       bigrams.append(bigram)         
    
    return bigrams

def get_index(square, char):
    rows, cols = (5, 5)
    for i in range(cols):
        for j in range(rows):
            if square[i][j] == char:
                return i, j
    return -1, -1

def get_element(square, i, j):
    if i > 4:
        i -= 5
    elif i < 0:
        i += 5

    if j > 4:
        j -= 5
    elif j < 0:
        j += 5

    return square[i][j]

class Playfair:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def preprocess(self):
        # Preprocess text
        text = self.text.lower()
        text = general.sanitize(text)
        text = general.replace_char(text, 'j', 'i')
        self.bigrams = create_bigram(text)
        
        # Preprocess key
        key = self.key.lower()
        key = general.sanitize(key)
        key += const.ALPHABET
        key = general.remove_duplicate_char(key)
        key = general.remove_char(key, 'j')
        self.key = general.create_square(key, 5)

    def encrypt(self):
        chiper_text = ''
        for bigram in self.bigrams:
            first_x, first_y = get_index(self.key, bigram[0])
            second_x, second_y = get_index(self.key, bigram[1])

            if first_x == -1 or second_x == -1:
                raise Exception(f'bigram not found in key', 500)

            first_el = ''
            second_el = ''

            if bigram[0] == bigram[1]:
                first_el = bigram[0]
                second_el = bigram[1]
            elif first_x == second_x:
                first_el = get_element(self.key, first_x, first_y + 1)
                second_el = get_element(self.key, second_x, second_y + 1)
            elif first_y == second_y:
                first_el = get_element(self.key, first_x + 1, first_y)
                second_el = get_element(self.key, second_x + 1, second_y)
            else:
                first_el = get_element(self.key, first_x, second_y)
                second_el = get_element(self.key, second_x, first_y)

            chiper_text += first_el
            chiper_text += second_el

        return chiper_text
  
    def decrypt(self):
        chiper_text = ''
        for bigram in self.bigrams:
            first_x, first_y = get_index(self.key, bigram[0])
            second_x, second_y = get_index(self.key, bigram[1])

            if first_x == -1 or second_x == -1:
                print(self.key)
                print(self.bigram)
                raise Exception(f'bigram not found in key', 500)

            first_el = ''
            second_el = ''

            if bigram[0] == bigram[1]:
                first_el = bigram[0]
                second_el = bigram[1]
            elif first_x == second_x:
                first_el = get_element(self.key, first_x, first_y - 1)
                second_el = get_element(self.key, second_x, second_y - 1)
            elif first_y == second_y:
                first_el = get_element(self.key, first_x - 1, first_y)
                second_el = get_element(self.key, second_x - 1, second_y)
            else:
                first_el = get_element(self.key, first_x, second_y)
                second_el = get_element(self.key, second_x, first_y)

            chiper_text += first_el
            chiper_text += second_el

        return chiper_text