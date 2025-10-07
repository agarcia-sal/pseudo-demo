def is_palindrome(cipher: str) -> bool:
    i: int = 0
    n: int = len(cipher)
    while i < n:
        left_char: str = cipher[i]
        right_index: int = (n - 1) - i
        right_char: str = cipher[right_index]
        if left_char != right_char:
            return False
        i += 1
    return True