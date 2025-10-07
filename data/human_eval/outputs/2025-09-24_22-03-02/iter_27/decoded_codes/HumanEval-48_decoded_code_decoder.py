def is_palindrome(text: str) -> bool:
    length = len(text)
    for i in range(length):
        left_char = text[i]
        right_char = text[length - 1 - i]
        if left_char != right_char:
            return False
    return True