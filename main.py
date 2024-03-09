import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import string

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
           new_char1, new_char2 = matrix[row1][col2], matrix[row2][col1]

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

# Fungsi untuk menampilkan cipherteks dalam format yang diinginkan
def format_ciphertext(ciphertext, format_type):
   if format_type == "Original":
       return ciphertext
   elif format_type == "No spaces":
       return ciphertext.replace(" ", "")
   elif format_type == "5-character groups":
       formatted = ""
       for i in range(0, len(ciphertext), 5):
           formatted += ciphertext[i:i+5] + " "
       return formatted.strip()

# Fungsi untuk menyimpan cipherteks ke file
def save_ciphertext(ciphertext):
   file_path = filedialog.asksaveasfilename(defaultextension=".txt")
   if file_path:
       with open(file_path, "w") as file:
           file.write(ciphertext)
       messagebox.showinfo("Sukses", "Cipherteks berhasil disimpan.")

# Fungsi untuk mengenkripsi file
def encrypt_file(cipher_func, key, input_file, output_file):
   with open(input_file, "rb") as file:
       plaintext = file.read()
   if cipher_func == extended_vigenere_cipher:
       ciphertext = cipher_func(plaintext, key, encrypt=True)
   else:
       plaintext = plaintext.decode("utf-8")
       ciphertext = cipher_func(plaintext, key, encrypt=True)
   with open(output_file, "wb") as file:
       file.write(ciphertext)

# Fungsi untuk mendekripsi file
def decrypt_file(cipher_func, key, input_file, output_file):
   with open(input_file, "rb") as file:
       ciphertext = file.read()
   if cipher_func == extended_vigenere_cipher:
       plaintext = cipher_func(ciphertext, key, encrypt=False)
   else:
       ciphertext = ciphertext.decode("utf-8")
       plaintext = cipher_func(ciphertext, key, encrypt=False)
       plaintext = plaintext.encode("utf-8")
   with open(output_file, "wb") as file:
       file.write(plaintext)

# GUI dengan customTkinter
root = ctk.CTk()
root.title("Chiper GUI")
root.geometry("1080x1920")

# Pengaturan tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(0.9) 

# Frame utama
main_frame = ctk.CTkFrame(root)
main_frame.pack(pady=20, padx=60, fill="both", expand=True)

# Label judul
title_label = ctk.CTkLabel(main_frame, text="CrackStation Lite", font=ctk.CTkFont(size=24, weight="bold", family="Segoe Print"))
title_label.pack(pady=12, padx=10, anchor="center")

# Frame input
input_frame = ctk.CTkFrame(main_frame)
input_frame.pack(pady=20, padx=10)

input_label = ctk.CTkLabel(input_frame, text="Input Text:", font=ctk.CTkFont(size=12, weight="bold", family="Consolas"))
input_label.pack(side="top", pady=5)

input_text = ctk.CTkTextbox(input_frame, width=400, height=100)
input_text.pack(side="top", pady=5)

# Frame kunci
key_frame = ctk.CTkFrame(main_frame)
key_frame.pack(pady=10, padx=10)

key_label = ctk.CTkLabel(key_frame, text="Kunci:", font=ctk.CTkFont(size=12, weight="bold", family="Consolas"))
key_label.pack(side="left", padx=5)

key_entry = ctk.CTkEntry(key_frame)
key_entry.pack(side="left", padx=5)

# Frame pilihan cipher
cipher_frame = ctk.CTkFrame(main_frame)
cipher_frame.pack(pady=10, padx=10)

cipher_label = ctk.CTkLabel(cipher_frame, text="Pilih Cipher:", font=ctk.CTkFont(size=12, weight="bold", family="Consolas"))
cipher_label.pack(side="top", pady=5)

cipher_var = tk.StringVar()
cipher_options = ["Vigenere Cipher Standard", "Vigenere Cipher Variant 1", "Vigenere Cipher Variant 2",
                 "Vigenere Cipher Variant 3", "Extended Vigenere Cipher", "Playfair Cipher",
                 "Super Enkripsi"]
cipher_dropdown = ctk.CTkComboBox(cipher_frame, values=cipher_options, variable=cipher_var)
cipher_dropdown.pack(side="top", pady=5)

# Frame pilihan aksi
action_frame = ctk.CTkFrame(main_frame)
action_frame.pack(pady=10, padx=10)

action_label = ctk.CTkLabel(action_frame, text="Pilih Aksi:", font=ctk.CTkFont(size=12, weight="bold", family="Consolas"))
action_label.pack(side="left", padx=5)

action_var = tk.StringVar()
action_options = ["Enkripsi", "Dekripsi"]
action_dropdown = ctk.CTkComboBox(action_frame, values=action_options, variable=action_var)
action_dropdown.pack(side="left", padx=5)

# Frame output
output_frame = ctk.CTkFrame(main_frame)
output_frame.pack(pady=20, padx=10)

output_label = ctk.CTkLabel(output_frame, text="Output Text:", font=ctk.CTkFont(size=12, weight="bold", family="Consolas"))
output_label.pack(side="top", pady=5)

output_text = ctk.CTkTextbox(output_frame, width=400, height=100)
output_text.pack(side="top", pady=5)

# Frame format output
format_frame = ctk.CTkFrame(main_frame)
format_frame.pack(pady=10, padx=10)

format_label = ctk.CTkLabel(format_frame, text="Format Output:", font=ctk.CTkFont(size=12, weight="bold", family="Consolas"))
format_label.pack(side="left", padx=5)

format_var = tk.StringVar()
format_options = ["Original", "No spaces", "5-character groups"]
format_dropdown = ctk.CTkComboBox(format_frame, values=format_options, variable=format_var)
format_dropdown.pack(side="left", padx=5)

# Tombol enkripsi/dekripsi
process_button = ctk.CTkButton(main_frame, text="Proses", command=lambda: process_text(), hover_color="green")
process_button.pack(pady=10)

# Tombol simpan
save_button = ctk.CTkButton(main_frame, text="Simpan Output", command=lambda: save_ciphertext(output_text.get("0.0", "end").strip()), hover_color="red")
save_button.pack(pady=10)

# Fungsi untuk memproses teks
def process_text():
   plaintext = input_text.get("0.0", "end").strip()
   key = key_entry.get()
   cipher_choice = cipher_var.get()
   action_choice = action_var.get().lower()
   format_choice = format_var.get()

   if cipher_choice == "Vigenere Cipher Standard":
       cipher_func = vigenere_cipher_standard
   elif cipher_choice == "Vigenere Cipher Variant 1":
       cipher_func = vigenere_cipher_variant1
   elif cipher_choice == "Vigenere Cipher Variant 2":
       cipher_func = vigenere_cipher_variant2
   elif cipher_choice == "Vigenere Cipher Variant 3":
       cipher_func = vigenere_cipher_variant3
   elif cipher_choice == "Extended Vigenere Cipher":
       cipher_func = extended_vigenere_cipher
   elif cipher_choice == "Playfair Cipher":
       cipher_func = playfair_cipher
   elif cipher_choice == "Super Enkripsi":
       cipher_func = super_encryption

   if action_choice == "enkripsi":
       if cipher_choice == "Super Enkripsi":
           key2 = input("Masukkan kunci transposisi (angka tanpa spasi): ")
           ciphertext = cipher_func(plaintext, key, key2, encrypt=True)
       else:
           ciphertext = cipher_func(plaintext, key, encrypt=True)
   else:
       if cipher_choice == "Super Enkripsi":
           key2 = input("Masukkan kunci transposisi (angka tanpa spasi): ")
           ciphertext = cipher_func(plaintext, key, key2, encrypt=False)
       else:
           ciphertext = cipher_func(plaintext, key, encrypt=False)

   formatted_ciphertext = format_ciphertext(ciphertext, format_choice)
   output_text.delete("0.0", "end")
   output_text.insert("0.0", formatted_ciphertext)


# Windows Menjalankan GUI Python Tkinter
root.mainloop()
