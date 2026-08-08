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
# Playfair Cipher Decryption

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = []

    for ch in key:
        if ch not in used and ch.isalpha():
            used.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            used.append(ch)

    for i in range(0, 25, 5):
        matrix.append(used[i:i+5])

    return matrix

def find_pos(matrix, ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def decrypt(text, matrix):
    text = text.replace(" ", "").upper()
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]

        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:      # Same row
            result += matrix[r1][(c1-1) % 5]
            result += matrix[r2][(c2-1) % 5]

        elif c1 == c2:    # Same column
            result += matrix[(r1-1) % 5][c1]
            result += matrix[(r2-1) % 5][c2]

        else:             # Rectangle rule
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

key = input("Enter the Playfair key: ")

cipher = """KXJEYUREBEZWEHEWRYTUHEYFS
KREHEGOYFIWTTTUOLKSYCAJPO
BOTEIZONTXBYBNTGONEYCUZWR
GDSONSXBOUYWRHEBAAHYUSEDQ"""

matrix = generate_matrix(key)

print("Playfair Matrix:")
for row in matrix:
    print(row)

plain = decrypt(cipher, matrix)

print("\nDecrypted Text:")
print(plain)
