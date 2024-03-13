import string
import binascii


# Constrains
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
LETTER = 97
CAPITAL = 65
SENTINEL = 224
TRANSPOSEKEY = 4
LENGTHALPHABET = 26

##################################################

import re
# use this to remove duplicate character from text preserving the order.
# Example: remove_duplicate_char('testacoba') -> tesacob 
def remove_duplicate_char(text):
    return "".join(dict.fromkeys(text))

# use this to remove character from text.
# Example: remove_char('test', 't') -> es 
def remove_char(text, char):
    return text.replace(char, '')

# sanitize will remove space, number, and puctuation from given text
def sanitize(text):
    return re.sub('[^A-Za-z]+', '', text)

# use this to replace a character with another character.
# Example: replace_char('test', 't', 'b') -> besb 
def replace_char(text, old_char, new_char):
    return text.replace(old_char, new_char)

# return order of given character in alphabetical rank, start from 0
# Example: char_to_order('a') -> 0, char_to_order('k') -> 10
def char_to_order(char):
    return ord(char.lower()) - ord('a')

# return lowercase character of given order in alphabetical rank, start from 0
# Example: order_to_char('0') -> a, order_to_char('10') -> k, order_to_char('26') -> a
def order_to_char(order):
    while order >= 26:
        order -= 26
    
    while order < 0:
        order += 26

    return chr(order + ord('a'))    

# create square matrix with given length from given array. 
# Matrix will be filled with priority from left to right then top to bottom.
def create_square(arr, length):
    rows, cols = (length, length) 
    square = [] 
    idx = 0
    for i in range(cols): 
        col = [] 
        for j in range(rows): 
            col.append(arr[idx])
            idx += 1 
        square.append(col)
    return square

# X that satisfy aX = 1 mod m
def mod_inverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

##################################################################

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

# Variasi Vigenere Full (OK)
def vigenere_cipher_variant1(text, key, encrypt=True):
    matrices_sollution = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a'],
        ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b'],
        ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c'],
        ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd'],
        ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e'],
        ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f'],
        ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],
        ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
        ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
        ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
        ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
        ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'],
        ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'],
        ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
        ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
        ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],
        ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'],
        ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'],
        ['t', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'],
        ['u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
        ['v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'],
        ['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'],
        ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
        ['y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
        ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']]

    def preprocess(text, key):
        # Preprocess text
        text = text.lower()
        text = sanitize(text)
        text = [(ord(i) - LETTER) for i in text]

        # Preprocess key
        key = key.lower()
        key = sanitize(key)
        key = [(ord(i) - LETTER) for i in key]

        return text, key

    def encrypt_text(text, key, matrices_sollution):
        ciphertext = ''
        idx = 0
        for char in text:
            if idx >= len(key):
                idx = 0
            ciphertext += matrices_sollution[char][key[idx]]
            idx += 1

        return ciphertext

    def decrypt_text(text, key, matrices_sollution):
        plaintext = ''
        idx = 0
        for char in text:
            if idx >= len(key):
                idx = 0

            element = chr(char + LETTER)
            plaintext += chr(matrices_sollution[key[idx]].index(element) + LETTER)
            idx += 1

        return plaintext

    text, key = preprocess(text, key)

    if encrypt:
        return encrypt_text(text, key, matrices_sollution)
    else:
        return decrypt_text(text, key, matrices_sollution)
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

def super_encryption(text, key1, key2, encrypt=True):
    # Enkripsi/Dekripsi Vigenere Cipher
    ciphertext = vigenere_cipher_variant1(text, key1, encrypt)

    # Enkripsi/Dekripsi Transposisi
    if encrypt:
        return encrypt_transposition(ciphertext, key2)
    else:
        return decrypt_transposition(ciphertext, key2)

def encrypt_transposition(text, key):
    """Mengenkripsi teks dengan transposisi kunci."""
    key = list(map(int, key))  # Mengubah kunci menjadi list of int
    rows = len(set(key))  # Jumlah baris adalah jumlah angka unik dalam kunci
    cols = (len(text) + rows - 1) // rows
    table = [[] for _ in range(rows)]

    # Mengisi tabel
    idx = 0
    for col in range(cols):
        for row in range(rows):
            if idx >= len(text):
                break
            table[row].append(text[idx])
            idx += 1

    # Membaca tabel berdasarkan kunci
    ciphertext = ''
    for k in sorted(set(key)):
        for i in range(cols):
            if i < len(table[key.index(k)]):
                ciphertext += table[key.index(k)][i]

    return ciphertext

def decrypt_transposition(text, key):
    """Mendekripsi teks dengan transposisi kunci."""
    key = list(map(int, key))  # Mengubah kunci menjadi list of int
    rows = len(set(key))  # Jumlah baris adalah jumlah angka unik dalam kunci
    cols = (len(text) + rows - 1) // rows
    table = [[] for _ in range(rows)]

    # Mengisi tabel
    idx = 0
    for k in sorted(set(key)):
        for i in range(cols):
            if idx >= len(text):
                break
            table[key.index(k)].append(text[idx])
            idx += 1

    # Membaca tabel secara normal
    plaintext = ''
    for row in table:
        plaintext += ''.join(row)

    return plaintext
