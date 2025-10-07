def anti_shuffle(input_string: str) -> str:
    list_of_words = input_string.split(' ')
    ordered_words = []
    for word in list_of_words:
        sorted_characters = sorted(word)
        ordered_word = ''.join(sorted_characters)
        ordered_words.append(ordered_word)
    ordered_string = ' '.join(ordered_words)
    return ordered_string