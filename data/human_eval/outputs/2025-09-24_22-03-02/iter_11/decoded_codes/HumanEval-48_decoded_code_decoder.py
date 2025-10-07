def is_palindrome(text: str) -> bool:
    return all(text[i] == text[-1 - i] for i in range(len(text)))