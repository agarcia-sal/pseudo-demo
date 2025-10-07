def is_bored(S) -> int:
    import re
    sentences = re.split(r"[.?!]\s*", S)
    count = 0
    i = 0
    while i < len(sentences):
        sentence = sentences[i]
        if len(sentence) >= 2:
            if sentence[0] == "I" and sentence[1] == " ":
                count += 1
        i += 1
    return count