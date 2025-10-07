def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    ordered_words = []
    for i in words:
        characters = list(i)
        sorted_characters = sorted(characters)
        ordered_word = ''.join(sorted_characters)
        ordered_words.append(ordered_word)
    result = ' '.join(ordered_words)
    return result