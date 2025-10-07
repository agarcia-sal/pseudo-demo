def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    ordered_words = []
    for index in range(len(words)):
        word = words[index]
        sorted_characters = sorted(list(word))
        ordered_word = ''
        for char_index in range(len(sorted_characters)):
            ordered_word += sorted_characters[char_index]
        ordered_words.append(ordered_word)
    result = ''
    for ordered_index in range(len(ordered_words)):
        if ordered_index > 0:
            result += ' '
        result += ordered_words[ordered_index]
    return result