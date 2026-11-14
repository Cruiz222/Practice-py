# number = "101010"

# dec = int(number, 2)

# print(dec)

def binary_to_decimal(binary):
    decimal = 0

    for index, bit in enumerate(reversed(binary)):
        if bit == "1":
            decimal += 2 ** index

    return decimal

print(binary_to_decimal("101010"))            