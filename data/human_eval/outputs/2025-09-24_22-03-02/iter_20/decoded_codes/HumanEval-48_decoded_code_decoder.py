def is_palindrome(text: str) -> bool:
    length = len(text)
    index = 0
    while index < length:
        front_char = text[index]
        back_char = text[length - 1 - index]
        if front_char != back_char:
            return False
        index += 1
    return True