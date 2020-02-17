import string

# STOP_WORDS = [
#     'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
#     'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
#     'will', 'with'
# ]

test_sentence = "I would love to learn to code in one day!" 
test_sentence = test_sentence.lower()
new_test_sentence = str.maketrans('', '', string.punctuation)

punctuation_removed = test_sentence.translate(new_test_sentence)
print(punctuation_removed)