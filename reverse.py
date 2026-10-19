#text = "hello"
#reversed_text = text[::-1]

#print(reversed_text)

#text = "John"

#reversed_text = "".join(reversed(text))

#print(reversed_text)

def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


print(reverse_string("marry"))


