def count_upper(email: str) -> int:
    result = 0
    iterator = 0
    length = len(email)
    while iterator <= length - 1:
        if email[iterator] in {'A', 'E', 'I', 'O', 'U'}:
            result += 1
        # Move forward by 2 positions each iteration
        iterator += 2
    return result