def is_palindrome(text: str) -> bool:
    length = len(text)
    i = 0
    while i < length:
        j = length - 1 - i
        char_i = text[i]
        char_j = text[j]
        if char_i != char_j:
            return False
        i += 1
    return True