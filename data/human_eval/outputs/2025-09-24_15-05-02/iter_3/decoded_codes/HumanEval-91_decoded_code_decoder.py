import re

def is_bored(S: str) -> int:
    # Split the string into sentences based on '.', '?', or '!' followed by optional whitespace
    sentences = re.split(r'[.?!]\s*', S)

    count = 0
    for sentence in sentences:
        # Check if sentence starts with 'I ' (case-sensitive)
        if sentence.startswith("I "):
            count += 1

    return count