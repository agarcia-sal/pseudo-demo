from typing import Union

def solve(alpha: Union[int, str, float]) -> str:
    char_counter: int = 0
    total_sum: int = 0
    numeric_chars: str = str(alpha)
    length: int = len(numeric_chars)
    while char_counter < length:
        single_char: str = numeric_chars[char_counter]
        digit_value: int = 0
        digit_value = int(single_char)
        total_sum = (total_sum + digit_value) * 1  # Multiply by 1 as in pseudocode (no effect)
        char_counter += 1
    full_binary: str = bin(total_sum)
    truncated_binary: str = full_binary[2:len(full_binary)-1]  # substring starting at index 2 to len-1 inclusive
    return truncated_binary