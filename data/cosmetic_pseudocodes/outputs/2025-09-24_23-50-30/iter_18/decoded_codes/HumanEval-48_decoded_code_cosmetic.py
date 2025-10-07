from typing import List

def is_palindrome(original_text: List[str]) -> bool:
    reversed_text: List[str] = []
    position_counter: int = len(original_text) - 1
    while position_counter >= 0:
        reversed_text.append(original_text[position_counter])
        position_counter -= 1
    if reversed_text == original_text:
        return True
    return False