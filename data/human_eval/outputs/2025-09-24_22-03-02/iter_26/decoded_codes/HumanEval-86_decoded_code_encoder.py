def anti_shuffle(s: str) -> str:
    result_words = []
    words = s.split(' ')
    for index in range(len(words)):
        current_word = words[index]
        char_list = []
        for char_index in range(len(current_word)):
            char = current_word[char_index]
            char_list.append(char)
        sorted_char_list = sorted(char_list)
        sorted_word = ''
        for sorted_char_index in range(len(sorted_char_list)):
            sorted_word += sorted_char_list[sorted_char_index]
        result_words.append(sorted_word)
    joined_string = ''
    for result_index in range(len(result_words)):
        if result_index > 0:
            joined_string += ' '
        joined_string += result_words[result_index]
    return joined_string