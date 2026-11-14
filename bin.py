# number = 50

# binary = bin(number)[2:]

# print(binary)

# number = 50

# print(f"{number:b}")


def binary_to_decimal(num):
    if num == 0:
         return "0"

    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    return binary

print(binary_to_decimal(50))             