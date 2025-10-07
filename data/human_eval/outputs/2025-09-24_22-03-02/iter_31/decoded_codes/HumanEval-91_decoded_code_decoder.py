import re

def is_bored(S):
    sentences = re.split(r"[.?!]\s*", S)
    boredom_count = 0
    index = 0
    length_sentences = len(sentences)
    while index < length_sentences:
        sentence = sentences[index]
        if len(sentence) >= 2:
            first_two_chars = sentence[0] + sentence[1]
            if first_two_chars == "I ":
                boredom_count += 1
        index += 1
    return boredom_count