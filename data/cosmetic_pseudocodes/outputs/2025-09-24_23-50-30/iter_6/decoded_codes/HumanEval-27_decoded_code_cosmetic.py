from typing import List

def flip_case(alpha_string: str) -> str:
    result_builder: List[str] = []
    index_counter: int = 0
    length: int = len(alpha_string)
    while index_counter < length:
        current_char: str = alpha_string[index_counter]
        if current_char.islower():
            # Convert lowercase to uppercase using ASCII offset
            result_builder.append(chr(ord(current_char) - 32))
        elif current_char.isupper():
            # Convert uppercase to lowercase using ASCII offset
            result_builder.append(chr(ord(current_char) + 32))
        else:
            result_builder.append(current_char)
        index_counter += 1
    return ''.join(result_builder)