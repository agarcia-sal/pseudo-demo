def is_palindrome(original_string: str) -> bool:
    position_counter: int = 0
    string_limit: int = len(original_string) - 1
    while position_counter <= string_limit:
        left_character: str = original_string[position_counter]
        right_index: int = string_limit - position_counter
        right_character: str = original_string[right_index]
        if left_character != right_character:
            return False
        position_counter += 1
    return True