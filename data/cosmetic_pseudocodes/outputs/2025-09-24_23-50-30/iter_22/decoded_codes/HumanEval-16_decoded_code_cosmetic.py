from collections import defaultdict

def count_distinct_characters(text: str) -> int:
    unique_chars: defaultdict[str, bool] = defaultdict(lambda: False)
    index: int = 0
    while index < len(text):
        character: str = text[index].lower()
        if not unique_chars[character]:
            unique_chars[character] = True
        index += 1

    count: int = 0
    for key in unique_chars:
        if unique_chars[key]:
            count += 1

    return count