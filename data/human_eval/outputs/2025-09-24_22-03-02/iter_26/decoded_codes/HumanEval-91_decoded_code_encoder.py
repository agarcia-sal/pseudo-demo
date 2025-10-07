def is_bored(S) -> int:
    import re
    sentences = re.split(r'[.?!]\s*', S)
    boredom_count = 0
    for sentence in sentences:
        if len(sentence) >= 2 and sentence[0] == 'I' and sentence[1] == ' ':
            boredom_count += 1
    return boredom_count