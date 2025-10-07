def anti_shuffle(s):
    return ' '.join([''.join(sorted(w)) for w in s.split(' ')])