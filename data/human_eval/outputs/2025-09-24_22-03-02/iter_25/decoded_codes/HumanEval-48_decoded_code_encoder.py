def is_palindrome(text: str) -> bool:
    length = len(text)
    for i in range(length):
        forward_char = text[i]
        backward_index = length - 1 - i
        backward_char = text[backward_index]
        if forward_char != backward_char:
            return False
    return True