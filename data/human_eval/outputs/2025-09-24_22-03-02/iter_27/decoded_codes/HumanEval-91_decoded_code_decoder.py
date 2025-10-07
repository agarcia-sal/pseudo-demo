def is_bored(S) -> int:
    sentences = []
    import re
    sentences = re.split(r'[.?!]\s*', S)
    boredom_count = 0
    for index in range(len(sentences)):
        sentence = sentences[index]
        if len(sentence) >= 2 and sentence[0:2] == 'I ':
            boredom_count += 1
    return boredom_count