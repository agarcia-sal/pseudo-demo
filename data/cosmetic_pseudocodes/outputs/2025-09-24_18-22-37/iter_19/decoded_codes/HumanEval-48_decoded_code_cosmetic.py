def is_palindrome(subject: str) -> bool:
    position: int = 0
    len_subject: int = len(subject)
    while position <= len_subject - 1:
        if subject[position] != subject[len_subject - 1 - position]:
            return False
        position += 1
    return True