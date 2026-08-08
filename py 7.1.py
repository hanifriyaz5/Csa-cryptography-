# Simple Substitution Cipher Decryption

cipher = input("Enter the ciphertext: ")
key = input("Enter the substitution key (26 letters): ")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plain = ""

for ch in cipher:
    if ch.isalpha():
        index = key.index(ch.upper())
        plain += alphabet[index]
    else:
        plain += ch

print("Decrypted Text:", plain)
