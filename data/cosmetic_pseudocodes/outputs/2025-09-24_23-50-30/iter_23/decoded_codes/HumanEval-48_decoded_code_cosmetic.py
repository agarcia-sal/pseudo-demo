def is_palindrome(input_string: str) -> bool:
    pointer_front: int = 0
    pointer_back: int = len(input_string) - 1
    while pointer_front <= pointer_back:
        if input_string[pointer_front] != input_string[pointer_back]:
            return False
        pointer_front += 1
        pointer_back -= 1
    return True