def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    result_words = []
    for index in range(len(words)):
        current_word = words[index]
        characters = list(current_word)
        characters_sorted = sorted(characters)
        sorted_word = ''
        for char_index in range(len(characters_sorted)):
            sorted_word += characters_sorted[char_index]
        result_words.append(sorted_word)
    final_string = ''
    for word_index in range(len(result_words)):
        final_string += result_words[word_index]
        if word_index < len(result_words) - 1:
            final_string += ' '
    return final_string