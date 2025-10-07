def anti_shuffle(s: str) -> str:
    return ' '.join(''.join(sorted(i)) for i in s.split(' '))