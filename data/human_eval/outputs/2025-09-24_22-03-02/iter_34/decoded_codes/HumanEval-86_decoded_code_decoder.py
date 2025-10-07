def anti_shuffle(s) -> str:
    words = s.split(' ')
    ordered_words = []
    index = 0
    while index < len(words):
        current_word = words[index]
        char_list = []
        char_index = 0
        while char_index < len(current_word):
            char_list.append(current_word[char_index])
            char_index += 1
        sorted_chars = sorted(char_list)
        new_word = ''
        sorted_index = 0
        while sorted_index < len(sorted_chars):
            new_word += sorted_chars[sorted_index]
            sorted_index += 1
        ordered_words.append(new_word)
        index += 1
    result = ''
    words_count = len(ordered_words)
    result_index = 0
    while result_index < words_count:
        result += ordered_words[result_index]
        if result_index < words_count - 1:
            result += ' '
        result_index += 1
    return result