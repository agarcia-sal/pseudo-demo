def is_palindrome(text: str):
    text_length = len(text)
    for i in range(text_length):
        left_char = text[i]
        right_char = text[text_length - 1 - i]
        if left_char != right_char:
            return False
    return True