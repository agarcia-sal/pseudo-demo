def is_bored(S) -> int:
    import re
    sentences = re.split(r'[.?!]\s*', S)
    count = 0
    for sentence in sentences:
        if sentence[:2] == 'I ':
            count += 1
    return count