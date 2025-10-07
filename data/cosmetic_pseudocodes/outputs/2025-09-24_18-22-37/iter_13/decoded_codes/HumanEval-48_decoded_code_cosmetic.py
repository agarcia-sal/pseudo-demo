def is_palindrome(input_string: str) -> bool:
    length_of_input: int = len(input_string)
    position: int = 0
    while position < length_of_input:
        mirror_position: int = length_of_input - 1 - position
        left_character: str = input_string[position]
        right_character: str = input_string[mirror_position]
        if left_character != right_character:
            return False
        position += 1
    return True