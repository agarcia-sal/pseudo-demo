from typing import List

def solve(string_input: str) -> str:
    marker: bool = False
    pos: int = 0
    char_array: List[str] = list(string_input)
    for letter in string_input:
        if letter.isalpha():
            # Toggle case
            char_array[pos] = letter.swapcase()
            marker = True
        pos += 1
    assembled_string: str = "".join(char_array)
    if not marker:
        return assembled_string[::-1]
    else:
        return assembled_string