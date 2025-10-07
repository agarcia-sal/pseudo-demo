def is_bored(S: str) -> int:
    import re
    sentences = re.split(r"[.?!]\s*", S)
    count = 0
    for i in range(len(sentences)):
        sentence = sentences[i]
        if len(sentence) >= 2:
            first_two_chars = sentence[:2]
            if first_two_chars == "I ":
                count += 1
    return count