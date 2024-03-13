import tkinter as tk
from tkinter import filedialog, messagebox
import string
import os
import customtkinter as ctk

class CipherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CipherShipper")
        self.geometry("800x600")

        self.cipher_types = ["Vigenere Standard", "Full Vigenere", "Auto-Key Vigenere", "Running-Key Vigenere",
                            "Extended Vigenere", "Playfair", "Super Enkripsi"]

        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.create_widgets()

    def create_widgets(self):

        self.plaintext_label = ctk.CTkLabel(self, text="Plaintext:")
        self.plaintext_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.plaintext_entry = ctk.CTkEntry(self, width=400)
        self.plaintext_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

        self.key_label = ctk.CTkLabel(self, text="Key:")
        self.key_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.key_entry = ctk.CTkEntry(self, width=400)
        self.key_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

        self.cipher_label = ctk.CTkLabel(self, text="Select Cipher:")
        self.cipher_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.cipher_var = ctk.StringVar()
        self.cipher_dropdown = ctk.CTkComboBox(self, values=self.cipher_types, variable=self.cipher_var)
        self.cipher_dropdown.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        self.cipher_var.set(self.cipher_types[0])

        self.output_label = ctk.CTkLabel(self, text="Ciphertext:")
        self.output_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.output_text = ctk.CTkTextbox(self, height=150)
        self.output_text.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

        # Create buttons
        self.encrypt_button = ctk.CTkButton(self, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=4, column=1, padx=10, pady=10)
        self.decrypt_button = ctk.CTkButton(self, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=4, column=2, padx=10, pady=10)
        self.load_button = ctk.CTkButton(self, text="Load File", command=self.load_file)
        self.load_button.grid(row=5, column=1, padx=10, pady=10)
        self.save_button = ctk.CTkButton(self, text="Save File", command=self.save_file)
        self.save_button.grid(row=5, column=2, padx=10, pady=10)

        # Title label
        title_label = ctk.CTkLabel(self, text="CipherShipper", font=ctk.CTkFont(size=24, weight="bold", family="Segoe Print"))
        title_label.grid(row=0, column=3, columnspan=2, padx=10, pady=10, sticky="s")

    def vigenere_encrypt(self, plaintext, key):
        plaintext = plaintext.upper()
        key = key.upper()
        ciphertext = ""
        key_index = 0

        for char in plaintext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                ciphertext += shifted_char
                key_index += 1
            else:
                ciphertext += char

        return ciphertext

    def vigenere_decrypt(self, ciphertext, key):
        ciphertext = ciphertext.upper()
        key = key.upper()
        plaintext = ""
        key_index = 0

        for char in ciphertext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                plaintext += shifted_char
                key_index += 1
            else:
                plaintext += char

        return plaintext

    def generate_key_table(self, key):
        key_table = []
        key_upper = key.upper()
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for char in key_upper:
            if char.isalpha():
                row = alphabet[alphabet.index(char):] + alphabet[:alphabet.index(char)]
                key_table.append(row)
            else:
                key_table.append(alphabet)

        return key_table

    def vigenere_encrypt_full(self, plaintext, key):
        plaintext = plaintext.upper()
        key_table = self.generate_key_table(key)
        ciphertext = ""
        key_index = 0

        for char in plaintext:
            if char.isalpha():
                row = kecy_table[key_index % len(key)]
                ciphertext += row[ord(char) - ord('A')]
                key_index += 1
            else:
                ciphertext += char

        return ciphertext

    def vigenere_decrypt_full(self, ciphertext, key):
        ciphertext = ciphertext.upper()
        key_table = self.generate_key_table(key)
        plaintext = ""
        key_index = 0

        for char in ciphertext:
            if char.isalpha():
                row = key_table[key_index % len(key)]
                plaintext += chr(ord('A') + row.index(char))
                key_index += 1
            else:
                plaintext += char

        return plaintext

    def generate_key_stream_auto(self, plaintext, key):
        key = key.upper().replace(" ", "")
        key_stream = key
        remaining_text = plaintext.upper().replace(" ", "")[len(key):]
        key_stream += remaining_text
        return key_stream

    def vigenere_encrypt_auto(self, plaintext, key):
        plaintext = plaintext.upper().replace(" ", "")
        key_stream = self.generate_key_stream_auto(plaintext, key)
        ciphertext = ""

        for i in range(len(plaintext)):
            char = plaintext[i]
            if char.isalpha():
                shift = ord(key_stream[i]) - ord('A')
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                ciphertext += shifted_char
            else:
                ciphertext += char

        return ciphertext, key_stream

    def vigenere_decrypt_auto(self, ciphertext, key):
        ciphertext = ciphertext.upper()
        plaintext = ""
        key_stream = self.generate_key_stream_auto(ciphertext, key)

        for i in range(len(ciphertext)):
            char = ciphertext[i]
            if char.isalpha():
                shift = ord(key_stream[i]) - ord('A')
                shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                plaintext += shifted_char
            else:
                plaintext += char

        return plaintext

    def generate_key_stream_run(self, plaintext, key):
        key = key.upper().replace(" ", "")
        key_stream = ""
        i = 0
        while len(key_stream) < len(plaintext):
            key_stream += key[i % len(key)]
            i += 1
        return key_stream

    def vigenere_encrypt_run(self, plaintext, key):
        plaintext = plaintext.upper().replace(" ", "")
        key_stream = self.generate_key_stream_run(plaintext, key)
        ciphertext = ""

        for i in range(len(plaintext)):
            char = plaintext[i]
            if char.isalpha():
                shift = ord(key_stream[i]) - ord('A')
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                ciphertext += shifted_char
            else:
                ciphertext += char

        return ciphertext, key_stream

    def vigenere_decrypt_run(self, ciphertext, key):
        ciphertext = ciphertext.upper()
        plaintext = ""
        key_stream = self.generate_key_stream_run(ciphertext, key)

        for i in range(len(ciphertext)):
            char = ciphertext[i]
            if char.isalpha():
                shift = ord(key_stream[i]) - ord('A')
                shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                plaintext += shifted_char
            else:
                plaintext += char

        return plaintext

    def vigenere_encrypt_ascii(self, plaintext, key):
        key_stream = self.generate_key_stream_run(plaintext, key)
        ciphertext = ""

        for i in range(len(plaintext)):
            char = plaintext[i]
            shift = ord(key_stream[i])
            shifted_char = chr((ord(char) + shift) % 256)
            ciphertext += shifted_char

        return ciphertext, key_stream

    def vigenere_decrypt_ascii(self, ciphertext, key):
        plaintext = ""
        key_stream = self.generate_key_stream_run(ciphertext, key)

        for i in range(len(ciphertext)):
            char = ciphertext[i]
            shift = ord(key_stream[i])
            shifted_char = chr((ord(char) - shift) % 256)
            plaintext += shifted_char

        return plaintext

    def generate_matrix(self, key):
        key = key.upper().replace(" ", "").replace("J", "")
        matrix = []
        used = set()

        # Add key characters to the matrix
        for char in key:
            if char not in used and char in string.ascii_uppercase.replace("J", ""):
                matrix.append(char)
                used.add(char)

        # Add remaining characters to the matrix
        for char in string.ascii_uppercase.replace("J", ""):
            if char not in used:
                matrix.append(char)
                used.add(char)

        # Convert the list to a 5x5 matrix
        matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return matrix

    def get_position(self, matrix, char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return None

    def prepare_plaintext(self, plaintext):
        plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
        prepared_text = ""
        bigrams = []

        for i in range(0, len(plaintext), 2):
            if i == len(plaintext) - 1:
                prepared_text += plaintext[i] + "X"
                bigrams.append(plaintext[i] + "X")
            else:
                char1 = plaintext[i]
                char2 = plaintext[i + 1]

                if char1 == char2:
                    prepared_text += char1 + "X"
                    bigrams.append(char1 + "X")
                else:
                    prepared_text += char1 + char2
                    bigrams.append(char1 + char2)

        return prepared_text, bigrams

    def playfair_encrypt(self, plaintext, key):
        matrix = self.generate_matrix(key)
        prepared_text, bigrams = self.prepare_plaintext(plaintext)
        ciphertext = ""

        for bigram in bigrams:
            row1, col1 = self.get_position(matrix, bigram[0])
            row2, col2 = self.get_position(matrix, bigram[1])

            if row1 == row2:
                ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                ciphertext += matrix[row1][col2] + matrix[row2][col1]

        return ciphertext, bigrams

    def playfair_decrypt(self, ciphertext, key):
        ciphertext = ciphertext.upper()
        matrix = self.generate_matrix(key)
        plaintext = ""

        for i in range(0, len(ciphertext), 2):
            char1 = ciphertext[i]
            char2 = ciphertext[i+1]

            row1, col1 = self.get_position(matrix, char1)
            row2, col2 = self.get_position(matrix, char2)

            if row1 == row2:
                plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                plaintext += matrix[row1][col2] + matrix[row2][col1]

        plaintext = plaintext.replace("X", "")
        return plaintext

    def super_enkripsi(self, plaintext, key, mode):
        def vigenere_cipher(text, key, mode):
            result = ""
            key_index = 0
            for char in text:
                if char.isalpha():
                    key_char = key[key_index % len(key)]
                    key_offset = ord(key_char.upper()) - ord('A')
                    if char.isupper():
                        char_offset = ord(char) - ord('A')
                        new_offset = (char_offset + key_offset) % 26 if mode == "encrypt" else (char_offset - key_offset) % 26
                        result += chr(new_offset + ord('A'))
                    elif char.islower():
                        char_offset = ord(char) - ord('a')
                        new_offset = (char_offset + key_offset) % 26 if mode == "encrypt" else (char_offset - key_offset) % 26
                        result += chr(new_offset + ord('a'))
                    key_index += 1
                else:
                    result += char
            return result

        def transpose_cipher(text, mode):
            result = ""
            rows = len(text) // 5 + 1
            cols = 5
            if mode == "encrypt":
                for col in range(cols):
                    for row in range(rows):
                        index = row * cols + col
                        if index < len(text):
                            result += text[index]
            elif mode == "decrypt":
                for row in range(rows):
                    for col in range(cols):
                        index = row + col * rows
                        if index < len(text):
                            result += text[index]
            return result

        if mode == "encrypt":
            step1 = vigenere_cipher(plaintext, key, "encrypt")
            ciphertext = transpose_cipher(step1, "encrypt")
        elif mode == "decrypt":
            step1 = transpose_cipher(plaintext, "decrypt")
            ciphertext = vigenere_cipher(step1, key, "decrypt")
        else:
            raise ValueError("Mode harus 'encrypt' atau 'decrypt'")
        return ciphertext


    def encrypt(self):
        plaintext = self.plaintext_entry.get()
        key = self.key_entry.get()
        cipher_type = self.cipher_var.get()
        if cipher_type == "Vigenere Standard":
            ciphertext = self.vigenere_encrypt(plaintext, key)
        elif cipher_type == "Full Vigenere":
            ciphertext = self.vigenere_encrypt_full(plaintext, key)
        elif cipher_type == "Auto-Key Vigenere":
            ciphertext, _ = self.vigenere_encrypt_auto(plaintext, key)
        elif cipher_type == "Running-Key Vigenere":
            ciphertext, _ = self.vigenere_encrypt_run(plaintext, key)
        elif cipher_type == "Extended Vigenere":
            ciphertext, _ = self.vigenere_encrypt_ascii(plaintext, key)
        elif cipher_type == "Playfair":
            ciphertext, _ = self.playfair_encrypt(plaintext, key)
        elif cipher_type == "Super Enkripsi":
            ciphertext = self.super_enkripsi(plaintext, key, "encrypt")

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, ciphertext)

    def decrypt(self):
        ciphertext = self.plaintext_entry.get()
        key = self.key_entry.get()
        cipher_type = self.cipher_var.get()
        if cipher_type == "Vigenere Standard":
            plaintext = self.vigenere_decrypt(ciphertext, key)
        elif cipher_type == "Full Vigenere":
            plaintext = self.vigenere_decrypt_full(ciphertext, key)
        elif cipher_type == "Auto-Key Vigenere":
            plaintext = self.vigenere_decrypt_auto(ciphertext, key)
        elif cipher_type == "Running-Key Vigenere":
            plaintext = self.vigenere_decrypt_run(ciphertext, key)
        elif cipher_type == "Extended Vigenere":
            plaintext = self.vigenere_decrypt_ascii(ciphertext, key)
        elif cipher_type == "Playfair":
            plaintext = self.playfair_decrypt(ciphertext, key)
        elif cipher_type == "Super Enkripsi":
            plaintext = self.super_enkripsi(ciphertext, key, "decrypt")

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, plaintext)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                data = file.read()
            self.plaintext_entry.delete(0, tk.END)
            self.plaintext_entry.insert(tk.END, data)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                data = self.output_text.get(1.0, tk.END)
                file.write(data)
            messagebox.showinfo("Save File", "File saved successfully.")

if __name__ == "__main__":
    app = CipherApp()
    app.mainloop()