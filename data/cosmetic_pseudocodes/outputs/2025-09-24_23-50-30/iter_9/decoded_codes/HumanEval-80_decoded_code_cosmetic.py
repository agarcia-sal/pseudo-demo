def is_happy(text: str) -> bool:
    length_text: int = len(text)
    if length_text < 3:
        return False
    for count in range(length_text - 2):
        c1, c2, c3 = text[count], text[count + 1], text[count + 2]
        if not (c1 != c2 and c2 != c3 and c1 != c3):
            return False
    return True