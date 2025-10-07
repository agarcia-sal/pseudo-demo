def anti_shuffle(input_string: str) -> str:
    list_of_words = input_string.split(' ')
    ordered_words = []
    for word in list_of_words:
        sorted_characters = sorted(word)
        sorted_word = ''.join(sorted_characters)
        ordered_words.append(sorted_word)
    result_string = ' '.join(ordered_words)
    return result_string