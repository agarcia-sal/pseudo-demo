import re

def is_bored(S) -> int:
    sentences = re.split(r'[.?!]\s*', S)
    boredom_count = 0
    index = 0
    while index < len(sentences):
        sentence = sentences[index]
        if len(sentence) >= 2:
            first_two_characters = sentence[0] + sentence[1]
            if first_two_characters == 'I ':
                boredom_count += 1
        index += 1
    return boredom_count