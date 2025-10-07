def is_palindrome(text: str) -> bool:
    return all(text[i] == text[~i] for i in range(len(text)))