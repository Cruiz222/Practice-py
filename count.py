def count_vowels(words):
    vowel = "aeiou"
    count = 0

    texts = words.lower()

    for letter in texts:
        if letter in vowel:
            count += 1

    return count


print(count_vowels("hello, how are you"))
