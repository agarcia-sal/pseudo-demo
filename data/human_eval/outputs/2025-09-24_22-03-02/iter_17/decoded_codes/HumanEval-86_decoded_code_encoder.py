def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    ordered_words = []
    for i in words:
        chars = list(i)
        sorted_chars = sorted(chars)
        ordered_word = ''.join(sorted_chars)
        ordered_words.append(ordered_word)
    result = ' '.join(ordered_words)
    return result