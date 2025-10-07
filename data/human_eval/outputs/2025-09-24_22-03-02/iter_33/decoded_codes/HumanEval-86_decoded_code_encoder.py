def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    result_words = []
    for index in range(len(words)):
        word = words[index]
        characters = []
        for char_index in range(len(word)):
            character = word[char_index]
            characters.append(character)
        characters.sort()
        ordered_word = ''
        for char_index in range(len(characters)):
            character = characters[char_index]
            ordered_word += character
        result_words.append(ordered_word)
    result_string = ''
    for index in range(len(result_words)):
        result_string += result_words[index]
        if index < len(result_words) - 1:
            result_string += ' '
    return result_string