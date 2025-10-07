from typing import List

def words_string(input_string: str) -> List[str]:
    result: List[str] = []
    if input_string != "":
        transformed_chars: List[str] = []
        idx: int = 0

        while idx < len(input_string):
            c: str = input_string[idx]
            transformed_chars.append(' ' if c == ',' else c)
            idx += 1

        merged_string: str = ""
        for i in range(len(transformed_chars)):
            merged_string += transformed_chars[i]

        # Split on any whitespace
        result = merged_string.split()
    return result