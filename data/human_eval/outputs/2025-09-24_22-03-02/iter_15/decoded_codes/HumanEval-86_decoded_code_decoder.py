def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    ordered_words = []
    for i in words:
        char_list = list(i)
        char_list.sort()
        ordered_word = ''.join(char_list)
        ordered_words.append(ordered_word)
    result = ' '.join(ordered_words)
    return result