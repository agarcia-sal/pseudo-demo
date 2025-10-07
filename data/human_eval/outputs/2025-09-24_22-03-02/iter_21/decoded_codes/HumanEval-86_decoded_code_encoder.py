def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    result_words = []
    for index_word in range(len(words)):
        current_word = words[index_word]
        chars_list = list(current_word)
        sorted_chars = sorted(chars_list)
        sorted_word = ''
        for index_char in range(len(sorted_chars)):
            sorted_word += sorted_chars[index_char]
        result_words.append(sorted_word)
    result_string = ''
    for index_result in range(len(result_words)):
        if index_result > 0:
            result_string += ' '
        result_string += result_words[index_result]
    return result_string