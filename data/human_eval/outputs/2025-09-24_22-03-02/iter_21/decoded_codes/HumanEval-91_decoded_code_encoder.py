def is_bored(S: str) -> int:
    import re
    sentences = re.split(r"[.?!]\s*", S)
    boredom_count = 0
    for i in range(len(sentences)):
        sentence = sentences[i]
        if len(sentence) >= 2 and sentence[0:2] == "I ":
            boredom_count += 1
    return boredom_count