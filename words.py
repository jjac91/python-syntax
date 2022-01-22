def print_upper_words(words, must_start_with):
    """Takes in a list of words and a list of letters
        and prints out a list of words with a capital first letter
        if the first letter matches one of the letters in the list of
        letters
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())