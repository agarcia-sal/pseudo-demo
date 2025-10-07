def is_bored(S) -> int:
    import re
    sentences = re.split(r"[.?!]\s*", S)
    boredom_count = 0
    index = 0
    while index < len(sentences):
        sentence = sentences[index]
        if len(sentence) >= 2:
            if sentence[:2] == "I ":
                boredom_count += 1
        index += 1
    return boredom_count