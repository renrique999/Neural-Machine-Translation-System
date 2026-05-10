# ==========================================
# English to Hindi Translation System
# Using Bigrams
# ==========================================

import nltk
from nltk.util import bigrams

# ==========================================
# Sample Parallel Corpus
# ==========================================

english_sentences = [

    "hello",

    "how are you",

    "good morning",

    "thank you",

    "machine learning"
]

hindi_sentences = [

    "namaste",

    "aap kaise ho",

    "shubh prabhat",

    "dhanyavaad",

    "machine learning"
]

# ==========================================
# Create Translation Dictionary
# ==========================================

translation_dict = dict(
    zip(english_sentences, hindi_sentences)
)

print("\nTranslation System Ready!")

# ==========================================
# User Input
# ==========================================

sentence = input("\nEnter English Sentence: ")

# ==========================================
# Translation
# ==========================================

if sentence in translation_dict:

    print("\nHindi Translation:")

    print(translation_dict[sentence])

else:

    print("\nTranslation not found!")

# ==========================================
# Bigram Generation
# ==========================================

tokens = sentence.split()

bigram_output = list(bigrams(tokens))

print("\nGenerated Bigrams:")

print(bigram_output)