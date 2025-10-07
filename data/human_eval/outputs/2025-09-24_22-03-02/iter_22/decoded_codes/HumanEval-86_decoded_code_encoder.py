def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    ordered_words = []
    for index in range(len(words)):
        word = words[index]
        char_list = []
        for char_index in range(len(word)):
            char_element = word[char_index]
            char_list.append(char_element)
        sorted_char_list = sorted(char_list)
        ordered_word = ''
        for sorted_index in range(len(sorted_char_list)):
            ordered_word += sorted_char_list[sorted_index]
        ordered_words.append(ordered_word)
    result = ''
    for result_index in range(len(ordered_words)):
        if result_index > 0:
            result += ' '
        result += ordered_words[result_index]
    return result