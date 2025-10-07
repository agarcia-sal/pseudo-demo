def is_bored(S):
    import re

    sentences = re.split(r"[.?!]\s*", S)
    boredom_count = 0

    for sentence in sentences:
        if sentence.startswith("I "):
            boredom_count += 1

    return boredom_count