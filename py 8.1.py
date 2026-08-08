# Monoalphabetic Cipher using keyword CIPHER

plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "cipherabdfgjklmnoqstuvwxyz"

text = input("Enter the plaintext: ").lower()

encrypted = ""

for ch in text:
    if ch.isalpha():
        index = plain.index(ch)
        encrypted += cipher[index]
    else:
        encrypted += ch

print("Encrypted Text:", encrypted)
