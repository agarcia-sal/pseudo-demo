def is_palindrome(text) -> bool:
    for index in range(len(text)):
        if text[index] != text[len(text) - 1 - index]:
            return False
    return True