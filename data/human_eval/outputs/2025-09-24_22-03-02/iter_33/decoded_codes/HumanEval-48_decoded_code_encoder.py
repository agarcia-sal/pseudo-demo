def is_palindrome(text: str) -> bool:
    length = len(text)
    i = 0
    while i < length:
        char_front = text[i]
        index_back = length - 1 - i
        char_back = text[index_back]
        if char_front != char_back:
            return False
        i += 1
    return True