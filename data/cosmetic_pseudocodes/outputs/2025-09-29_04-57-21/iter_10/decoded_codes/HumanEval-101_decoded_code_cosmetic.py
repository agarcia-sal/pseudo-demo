from typing import List

def words_string(input_string: str) -> List[str]:
    if input_string:
        result_chars: List[str] = []
        index: int = 0

        while index < len(input_string):
            current_char: str = input_string[index]

            if current_char != ',':
                result_chars.append(current_char)
            else:
                result_chars.append(' ')

            index += 1

        assembled_str: str = ''
        iter_to_char = iter(result_chars)
        try:
            while True:
                assembled_str += next(iter_to_char)
        except StopIteration:
            pass

        return assembled_str.split()
    return []