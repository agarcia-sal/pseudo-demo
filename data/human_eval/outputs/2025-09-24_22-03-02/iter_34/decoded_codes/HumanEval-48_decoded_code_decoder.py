def is_palindrome(text: str) -> bool:
    length = len(text)
    i = 0
    while i < length:
        left_char = text[i]
        right_char = text[length - 1 - i]
        if left_char != right_char:
            return False
        i += 1
    return True