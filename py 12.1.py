# Hill Cipher Encryption (2x2)

key = [[9, 4],
       [5, 7]]

text = "meet me at the usual place at ten rather than eight oclock"

# Remove spaces and convert to lowercase
text = text.replace(" ", "").lower()

# Add x if length is odd
if len(text) % 2 != 0:
    text += "x"

cipher = ""

for i in range(0, len(text), 2):
    a = ord(text[i]) - ord('a')
    b = ord(text[i + 1]) - ord('a')

    c1 = (key[0][0] * a + key[0][1] * b) % 26
    c2 = (key[1][0] * a + key[1][1] * b) % 26

    cipher += chr(c1 + ord('a'))
    cipher += chr(c2 + ord('a'))

print("Plaintext :", text)
print("Ciphertext:", cipher)
