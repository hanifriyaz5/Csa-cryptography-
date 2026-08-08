# Playfair Cipher Decryption

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    used = []

    for ch in key:
        if ch.isalpha() and ch not in used:
            used.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            used.append(ch)

    matrix = []

    for i in range(0, 25, 5):
        matrix.append(used[i:i+5])

    return matrix


def find_pos(matrix, ch):
    ch = ch.upper().replace("J", "I")

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def decrypt(text, matrix):

    # Remove spaces, newlines and other non-alphabet characters
    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    text = text.replace("J", "I")

    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):

        a = text[i]
        b = text[i + 1]

        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        # Same row
        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]

        # Same column
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]

        # Rectangle rule
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


# Main Program

key = input("Enter the Playfair key: ")

cipher = """KXJEYUREBEZWEHEWRYTUHEYFS
KREHEGOYFIWTTTUOLKSYCAJPO
BOTEIZONTXBYBNTGONEYCUZWR
GDSONSXBOUYWRHEBAAHYUSEDQ"""

matrix = generate_matrix(key)

print("\nPlayfair Matrix:")
for row in matrix:
    print(" ".join(row))

plain = decrypt(cipher, matrix)

print("\nDecrypted Text:")
print(plain)
