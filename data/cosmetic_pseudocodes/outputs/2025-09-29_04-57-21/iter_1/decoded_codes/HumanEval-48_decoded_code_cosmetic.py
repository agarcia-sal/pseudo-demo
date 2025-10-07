def is_palindrome(text: str) -> bool:
    last_index: int = len(text) - 1
    pointer: int = 0
    while pointer <= last_index:
        if text[pointer] != text[last_index - pointer]:
            return False
        pointer += 1
    return True