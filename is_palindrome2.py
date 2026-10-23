class StringProcessor:
    def __init__(self, s: str):
        self.s = s

    def is_palindrome(self)-> bool:
        self.chars = [chars.lower() for chars in self.s if chars.isalnum()]

        return self.chars == self.chars[::-1]


processor = StringProcessor("A man, a plan, a canal: Panama")
print(processor.is_palindrome()) 

processor2 = StringProcessor("race a car")
print(processor2.is_palindrome())             