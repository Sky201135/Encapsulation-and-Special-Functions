class StringReverse:
    def __init__(self, text):
        self.__text = text   # private attribute

    def reverse_words(self):
        words = self.__text.split()
        reversed_words = " ".join(reversed(words))
        return reversed_words

    def __str__(self):
        return f"Original: {self.__text}\nReversed: {self.reverse_words()}"


if __name__ == "__main__":
    sentence = StringReverse("Hello world this is Python")
    print(sentence)
