def sort_chars(word):
    return ''.join(sorted(word))

def anti_shuffle(s):
    return ' '.join(map(sort_chars, s.split(' ')))