# Hill Cipher - Known Plaintext Attack (2x2)
# No NumPy required

import math

# Plaintext matrix
P = [[7, 4],
     [11, 15]]

# Ciphertext matrix
C = [[3, 18],
     [17, 2]]


# Modular inverse
def mod_inverse(a, m):
    a = a % m

    for i in range(1, m):
        if (a * i) % m == 1:
            return i

    return None


# Inverse of 2x2 matrix modulo 26
def matrix_inverse(P):

    det = (P[0][0] * P[1][1] -
           P[0][1] * P[1][0]) % 26

    if math.gcd(det, 26) != 1:
        print("Matrix inverse does not exist.")
        return None

    det_inv = mod_inverse(det, 26)

    adj = [
        [P[1][1], -P[0][1]],
        [-P[1][0], P[0][0]]
    ]

    P_inv = [
        [(det_inv * adj[0][0]) % 26,
         (det_inv * adj[0][1]) % 26],

        [(det_inv * adj[1][0]) % 26,
         (det_inv * adj[1][1]) % 26]
    ]

    return P_inv


# Matrix multiplication modulo 26
def matrix_multiply(A, B):

    result = [[0, 0],
              [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]

            result[i][j] %= 26

    return result


P_inv = matrix_inverse(P)

if P_inv is not None:

    K = matrix_multiply(C, P_inv)

    print("Recovered Key Matrix:")

    for row in K:
        print(row)
