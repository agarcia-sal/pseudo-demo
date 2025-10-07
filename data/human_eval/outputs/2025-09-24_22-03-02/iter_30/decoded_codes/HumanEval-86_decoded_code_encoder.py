def anti_shuffle(s) -> str:
    words = s.split(' ')
    result_words = []
    for i in range(len(words)):
        current_word = list(words[i])
        sorted_chars = sorted(current_word)
        new_word = ''
        for j in range(len(sorted_chars)):
            new_word += sorted_chars[j]
        result_words.append(new_word)
    final_string = ''
    for k in range(len(result_words)):
        final_string += result_words[k]
        if k < len(result_words) - 1:
            final_string += ' '
    return final_string