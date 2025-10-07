def anti_shuffle(s: str) -> str:
    words = s.split(' ')
    sorted_words = [''.join(sorted(word)) for word in words]
    result_string = ' '.join(sorted_words)
    return result_string