import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence_letters = set(sentence.lower())
    return alphabet.issubset(sentence_letters)

sentence_1 = "The quick brown fox jumps over the lazy dog"
result_1 = is_pangram(sentence_1)
print(result_1)  # Output: True
