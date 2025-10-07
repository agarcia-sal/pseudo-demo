def is_palindrome(text: str) -> bool:
    length = len(text)
    for i in range(length):
        front_char = text[i]
        back_index = length - 1 - i
        back_char = text[back_index]
        if front_char != back_char:
            return False
    return True