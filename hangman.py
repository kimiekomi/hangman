import random
import word_bank

def random_word(list):
    hidden_word = random.choice(list)

    return hidden_word

print(random_word(word_bank.word_bank))