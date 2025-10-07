def is_palindrome(text: str) -> bool:
    length = len(text)
    index = 0
    while index < length:
        left_char = text[index]
        right_char = text[length - 1 - index]
        if left_char != right_char:
            return False
        index += 1
    return True