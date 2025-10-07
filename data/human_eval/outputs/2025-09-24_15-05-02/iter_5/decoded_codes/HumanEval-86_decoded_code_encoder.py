def anti_shuffle(s):
    list_of_words = s.split(' ')
    ordered_words = []
    for word in list_of_words:
        sorted_characters = sorted(list(word))
        sorted_word = ''.join(sorted_characters)
        ordered_words.append(sorted_word)
    result_string = ' '.join(ordered_words)
    return result_string