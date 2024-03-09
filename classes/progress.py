
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