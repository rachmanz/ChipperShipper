
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