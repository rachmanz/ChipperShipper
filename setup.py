# Library Eksternal 
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import string

# Library Internal
from classes.chiper import *
from classes.enc_dec import *
from classes.progress import *

# GUI dengan customTkinter
root = ctk.CTk()
root.title("ChiperShipper")
root.geometry("1080x1920")

# Pengaturan tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(0.9) 

# Frame utama
main_frame = ctk.CTkFrame(root)
main_frame.pack(pady=20, padx=60, fill="both", expand=True)

# Label judul
title_label = ctk.CTkLabel(main_frame, text="ChiperShipper", font=ctk.CTkFont(size=24, weight="bold", family="Segoe Print"))
title_label.pack(pady=12, padx=10, anchor="center")

# Frame input
input_frame = ctk.CTkFrame(main_frame)
input_frame.pack(pady=20, padx=10)

input_label = ctk.CTkLabel(input_frame, text="Input Text:", font=ctk.CTkFont(size=12, weight="bold", family="Consolas"))
input_label.pack(side="top", pady=5)

input_text = ctk.CTkTextbox(input_frame, width=400, height=100)
input_text.pack(side="top", pady=5)

# Frame upload file
upload_frame = ctk.CTkFrame(input_frame)
upload_frame.pack(pady=5)

upload_label = ctk.CTkLabel(upload_frame, text="Upload File:", font=ctk.CTkFont(size=12, weight="bold", family="Consolas"))
upload_label.pack(side="left", padx=5)

upload_button = ctk.CTkButton(upload_frame, text="Browse", command=lambda: upload_file(input_text), font=ctk.CTkFont(size=12, family="Consolas"), hover_color="green")
upload_button.pack(side="left", padx=5)

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
cipher_label.pack(side="top", pady=3)

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

# Fungsi untuk mengunggah file ke dalam kotak input teks
def upload_file(input_text_widget):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.read()
            input_text_widget.insert("0.0", file_content)


# Windows Menjalankan GUI Python Tkinter
root.mainloop()