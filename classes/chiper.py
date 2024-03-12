import string
import binascii
from src.algorithm import general
from src.algorithm import const
from src.algorithm import vigenere

# Vigenere Cipher Standar (OK)
def vigenere_cipher_standard(text, key, encrypt=True):
    result = ""
    key_len = len(key)
    key_idx = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            char_idx = ord(char) - base
            key_idx = (key_idx + 1) % key_len
            key_char = ord(key[key_idx].upper()) - ord('A')
            if encrypt:
                new_idx = (char_idx + key_char) % 26
            else:
                new_idx = (char_idx - key_char) % 26
            new_char = chr(new_idx + base)
            result += new_char
        else:
            result += char
    return result

######################################################################

# Variasi Vigenere Full
def vigenere_cipher_variant1(text, key, encrypt=True):
    matrices_sollution =[
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

    def preprocess(text, key):
        # Preprocess text
        text = text.lower()
        text = general.sanitize(text)
        text = [(ord(i) - const.LETTER) for i in text]

        # Preprocess key
        key = key.lower()
        key = general.sanitize(key)
        key = [(ord(i) - const.LETTER) for i in key]

        return text, key

    def encrypt_text(text, key, matrices_solution):
        ciphertext = ''
        idx = 0
        for char in text:
            if idx >= len(key):
                idx = 0
            ciphertext += matrices_solution[char][key[idx]]
            idx += 1

        return ciphertext

    def decrypt_text(text, key, matrices_solution):
        plaintext = ''
        idx = 0
        for char in text:
            if idx >= len(key):
                idx = 0

            element = chr(char + const.LETTER)
            plaintext += chr(matrices_solution[key[idx]].index(element) + const.LETTER)
            idx += 1

        return plaintext

    text, key = preprocess(text, key)

    if encrypt:
        return encrypt_text(text, key, matrices_solution)
    else:
        return decrypt_text(text, key, matrices_solution)
################################################################
# Variasi Vigenere Auto Key (OK)
def vigenere_cipher_variant2(text, key, encrypt=True):
    result = ""
    key_len = len(key)
    key_idx = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            char_idx = ord(char) - base
            key_idx = (key_idx + 1) % key_len
            key_char = ord(key[key_idx].upper()) - ord('A')
            if encrypt:
                new_idx = (char_idx + key_char * key_idx) % 26
            else:
                new_idx = (char_idx - key_char * key_idx) % 26
            new_char = chr(new_idx + base)
            result += new_char
        else:
            result += char
    return result

##############################################################

# Variasi Vigenere Running (OK)
def vigenere_cipher_variant3(text, key, encrypt=True):
    result = ""
    key_len = len(key)
    key_idx = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            char_idx = ord(char) - base
            key_idx = (key_idx + 1) % key_len
            key_char = ord(key[key_idx].upper()) - ord('A')
            if encrypt:
                new_idx = (char_idx + key_char * (key_idx + 1)) % 26
            else:
                new_idx = (char_idx - key_char * (key_idx + 1)) % 26
            new_char = chr(new_idx + base)
            result += new_char
        else:
            result += char
    return result

#######################################################################

# Extended Vigenere Cipher (256 karakter ASCII) (OK)
def extended_vigenere_cipher(text, key, encrypt=True):
    def preprocess(text, key, is_binary, mode):
        # Preprocess text
        if is_binary and mode == 'encrypt':
            text = text.hex()
        text = [ord(char) for char in text]

        # Preprocess key
        key = [ord(char) for char in key]

        return text, key

    def encrypt_text(text, key):
        ciphertext = ''
        idx = 0
        for char in text:
            if idx >= len(key):
                idx = 0
            ciphertext += chr((char + key[idx]) % 256)
            idx += 1
        return ciphertext

    def decrypt_text(text, key):
        plaintext = ''
        idx = 0
        for char in text:
            if idx >= len(key):
                idx = 0
            plaintext += chr((char - key[idx]) % 256)
            idx += 1
        return plaintext

    is_binary = isinstance(text, bytes)
    if is_binary and not encrypt:
        text = binascii.unhexlify(text.decode('utf-8'))

    text, key = preprocess(text, key, is_binary, 'encrypt' if encrypt else 'decrypt')

    if encrypt:
        ciphertext = encrypt_text(text, key)
    else:
        ciphertext = decrypt_text(text, key)

    if is_binary and encrypt:
        ciphertext = binascii.unhexlify(ciphertext)

    return ciphertext

#####################################################################################3

# Playfair Cipher (26 huruf alfabet) (OK)
# Fungsi untuk membuat bigram dari teks
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

# Fungsi untuk mendapatkan indeks karakter dalam matriks kunci
def get_index(square, char):
    rows, cols = (5, 5)
    for i in range(cols):
        for j in range(rows):
            if square[i][j] == char:
                return i, j
    return -1, -1

# Fungsi untuk mendapatkan elemen di posisi (i, j) dalam matriks kunci
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

# Playfair Cipher
def playfair_cipher(text, key, encrypt=True):
    # Preprocess text
    text = text.lower()
    text = ''.join(char for char in text if char.isalpha())
    text = text.replace('j', 'i')
    bigrams = create_bigram(text)

    # Preprocess key
    key = key.lower()
    key = ''.join(char for char in key if char.isalpha())
    key = key.replace('j', '')
    key += string.ascii_lowercase
    key = ''.join(dict.fromkeys(key))
    key_square = [list(key[i:i+5]) for i in range(0, len(key), 5)]

    # Enkripsi atau dekripsi
    ciphertext = ''
    for bigram in bigrams:
        first_x, first_y = get_index(key_square, bigram[0])
        second_x, second_y = get_index(key_square, bigram[1])

        if first_x == -1 or second_x == -1:
            raise Exception(f'Bigram {bigram} tidak ditemukan dalam kunci', 500)

        if bigram[0] == bigram[1]:
            first_el = bigram[0]
            second_el = bigram[1]
        elif first_x == second_x:
            if encrypt:
                first_el = get_element(key_square, first_x, first_y + 1)
                second_el = get_element(key_square, second_x, second_y + 1)
            else:
                first_el = get_element(key_square, first_x, first_y - 1)
                second_el = get_element(key_square, second_x, second_y - 1)
        elif first_y == second_y:
            if encrypt:
                first_el = get_element(key_square, first_x + 1, first_y)
                second_el = get_element(key_square, second_x + 1, second_y)
            else:
                first_el = get_element(key_square, first_x - 1, first_y)
                second_el = get_element(key_square, second_x - 1, second_y)
        else:
            first_el = get_element(key_square, first_x, second_y)
            second_el = get_element(key_square, second_x, first_y)

        ciphertext += first_el + second_el

    return ciphertext
#########################################################################################################

# Super enkripsi: Vigenere Cipher standard + cipher transposisi

def split_len(seq, length):
    matrices = [seq[i:i + length] for i in range(0, len(seq), length)]
    nRow = math.ceil(len(seq)/length)
    lengthLastRow = len(matrices[nRow-1])
    if lengthLastRow != length:
        for i in range(0, (length-lengthLastRow)):
            matrices[nRow-1].append(const.SENTINEL)
    return matrices

def super_encryption(text, key1, key2, encrypt=True):
    def preprocess(text, key):
        # Preprocess text
        text = text.lower()
        text = general.sanitize(text)
        text = [(ord(i) - const.LETTER) for i in text]

        # Preprocess key
        key = key.lower()
        key = general.sanitize(key)
        key = [(ord(i) - const.LETTER) for i in key]

        return text, key

    def encrypt_text(text, key1, key2):
        # Encrypt phase 1: Vigenere Cipher
        vig = vigenere_cipher(text, key1, encrypt=True)
        ord_vig = [(ord(i) - const.LETTER) for i in vig]

        # Encrypt phase 2: Transposition Cipher
        matrices = split_len(ord_vig, const.TRANSPOSEKEY)
        transpose = np.transpose(matrices)
        ciphertext = ''
        for row in transpose:
            for col in row:
                if col != const.SENTINEL:
                    ciphertext += general.order_to_char(col)
                else:
                    ciphertext += chr(col)

        return ciphertext

    def decrypt_text(text, key1, key2):
        # Decrypt phase 1: Transposition Cipher
        text = []
        for char in text:
            if char != chr(const.SENTINEL):
                text.append(ord(char) - const.LETTER)
            else:
                text.append(const.SENTINEL)

        nRow = int(len(text) / const.TRANSPOSEKEY)
        matrices = split_len(text, nRow)
        transpose = np.transpose(matrices)
        ciphertext = ''
        for row in transpose:
            for col in row:
                if col != const.SENTINEL:
                    ciphertext += general.order_to_char(col)

        ciphertext = [(ord(char) - const.LETTER) for char in ciphertext]

        # Decrypt phase 2: Vigenere Cipher
        plaintext = vigenere_cipher(ciphertext, key1, encrypt=False)

        return plaintext

    text, key1 = preprocess(text, key1)

    if encrypt:
        return encrypt_text(text, key1, key2)
    else:
        return decrypt_text(text, key1, key2)