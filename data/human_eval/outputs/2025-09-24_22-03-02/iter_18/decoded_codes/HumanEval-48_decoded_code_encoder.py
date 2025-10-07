def is_palindrome(text: str) -> bool:
    length = len(text)
    i = 0
    while i < length:
        front_char = text[i]
        back_char = text[length - 1 - i]
        if front_char != back_char:
            return False
        i += 1
    return True