import math

# Total possible Playfair keys = 25!
keys = math.factorial(25)

print("Total possible keys (25!) =")
print(keys)

# Approximate power of 2
power = math.log2(keys)

print("\nApproximate power of 2:")
print("2^", round(power, 2))

# Effectively unique keys
unique = keys // 2

print("\nEffectively unique keys:")
print(unique)

power2 = math.log2(unique)

print("\nApproximate power of 2:")
print("2^", round(power2, 2))
