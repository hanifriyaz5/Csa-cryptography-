# Playfair Cipher Encryption

matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

text = "Must see you over Cadogan West Coming at once"
text = text.upper().replace(" ", "").replace(".", "").replace("J", "I")

# Prepare plaintext
pt = ""
i = 0
while i < len(text):
    pt += text[i]
    if i + 1 < len(text):
        if text[i] == text[i + 1]:
            pt += "X"
        else:
            pt += text[i + 1]
            i += 1
    i += 1

if len(pt) % 2 != 0:
    pt += "X"

def find(ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

cipher = ""

for i in range(0, len(pt), 2):
    a = pt[i]
    b = pt[i + 1]

    r1, c1 = find(a)
    r2, c2 = find(b)

    if r1 == r2:          # Same row
        cipher += matrix[r1][(c1 + 1) % 5]
        cipher += matrix[r2][(c2 + 1) % 5]

    elif c1 == c2:        # Same column
        cipher += matrix[(r1 + 1) % 5][c1]
        cipher += matrix[(r2 + 1) % 5][c2]

    else:                 # Rectangle
        cipher += matrix[r1][c2]
        cipher += matrix[r2][c1]

print("Encrypted Text:")
print(cipher)
