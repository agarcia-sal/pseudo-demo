def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    sorted_words = []
    for i in words:
        characters = list(i)
        sorted_characters = sorted(characters)
        sorted_word = ''.join(sorted_characters)
        sorted_words.append(sorted_word)
    result = ' '.join(sorted_words)
    return result