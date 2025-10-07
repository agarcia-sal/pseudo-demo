def is_palindrome(text):
    length = len(text)
    for i in range(length):
        if text[i] != text[length - 1 - i]:
            return False
    return True