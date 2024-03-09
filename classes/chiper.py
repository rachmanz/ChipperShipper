class Chiper:
    # Vigenere Cipher standard (26 huruf alfabet)
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

    # Variasi Vigenere Cipher 1
    def vigenere_cipher_variant1(text, key, encrypt=True):
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
                    new_idx = (char_idx * key_char) % 26
                else:
                    new_idx = (char_idx * (26 - key_char)) % 26
                new_char = chr(new_idx + base)
                result += new_char
            else:
                result += char
        return result

    # Variasi Vigenere Cipher 2
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

    # Variasi Vigenere Cipher 3
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

    # Extended Vigenere Cipher (256 karakter ASCII)
    def extended_vigenere_cipher(text, key, encrypt=True):
        result = bytearray()
        key_len = len(key)
        key_idx = 0
        for byte in text:
            key_idx = (key_idx + 1) % key_len
            key_char = ord(key[key_idx])
            if encrypt:
                new_byte = (byte + key_char) % 256
            else:
                new_byte = (byte - key_char) % 256
            result.append(new_byte)
        return bytes(result)

    # Playfair Cipher (26 huruf alfabet)
    def playfair_cipher(text, key, encrypt=True):
        # Buat matriks 5x5 dari kunci
        key = key.upper().replace(" ", "")
        key_chars = "".join(sorted(set(key + string.ascii_uppercase), key=key.find))
        matrix = [key_chars[i:i+5] for i in range(0, 25, 5)]

        result = ""
        text = text.upper().replace(" ", "")
        text = "".join(["X" + c if c == text[i-1] else c for i, c in enumerate(text[1:], 2)]).replace("J", "I")
        if len(text) % 2 == 1: # tambahkan ini
            text += "X" # tambahkan ini

        for i in range(0, len(text), 2):
            char1, char2 = text[i], text[i+1]
            row1, col1 = next((row, col) for row in range(5) for col in range(5) if matrix[row][col] == char1)
            row2, col2 = next((row, col) for row in range(5) for col in range(5) if matrix[row][col] == char2)

            if row1 == row2:
                if encrypt:
                    new_char1, new_char2 = matrix[row1][(col1 + 1) % 5], matrix[row2][(col2 + 1) % 5]
                else:
                    new_char1, new_char2 = matrix[row1][(col1 - 1) % 5], matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                if encrypt:
                    new_char1, new_char2 = matrix[(row1 + 1) % 5][col1], matrix[(row2 + 1) % 5][col2]
                else:
                    new_char1, new_char2 = matrix[(row1 - 1) % 5][col1], matrix[(row2 - 1) % 5][col2]
            else:
                new_char1, new_char2 = matrix[col1][row2], matrix[col2][row1] # ubah ini

            result += new_char1 + new_char2

        return result


    # Super enkripsi: Vigenere Cipher standard + cipher transposisi
    def super_encryption(text, key1, key2, encrypt=True):
        # Enkripsi dengan Vigenere Cipher standard
        text = vigenere_cipher_standard(text, key1, encrypt)

        # Cipher transposisi
        result = ""
        key_len = len(key2)
        for i in range(key_len):
            char_idx = key2.index(str(i+1))
            result += text[char_idx::key_len]
        return result