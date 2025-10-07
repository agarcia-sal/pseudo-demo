def is_palindrome(input_string: str) -> bool:
    length = len(input_string)
    for iterator in range(length // 2):
        if input_string[iterator] != input_string[length - iterator - 1]:
            return False
    return True