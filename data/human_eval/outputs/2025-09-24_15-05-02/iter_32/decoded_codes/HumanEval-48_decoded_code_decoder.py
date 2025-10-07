def is_palindrome(text_string: str) -> bool:
    length: int = len(text_string)
    for index in range(length):
        if text_string[index] != text_string[length - 1 - index]:
            return False
    return True