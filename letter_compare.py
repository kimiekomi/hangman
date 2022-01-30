
debug = True

def letter_compare(secret_word, correct_letters):

    if debug: print (f"letter_compare (secret_word={secret_word}, {correct_letters})")

    new_state = ""

    for letter in secret_word:

        if letter in correct_letters:
            new_state += letter.lower ()
        else:
            new_state += "_"

    if debug: print(f"new_state - {new_state}")

    return new_state

if __name__ == "__main__":
    print(letter_compare("apple", "p"))