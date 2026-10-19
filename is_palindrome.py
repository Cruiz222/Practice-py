def is_palindrome(text):
    cleaned_text = text.lower()

    return cleaned_text == cleaned_text[::-1]


print(is_palindrome("racecar"))
print(is_palindrome("madam"))
print(is_palindrome("John"))    