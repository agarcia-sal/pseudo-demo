from typing import List, Union

def reverse_delete(s: str, c: str) -> List[Union[str, bool]]:
    result_string = []
    for current_char in s:
        is_in_c = False
        for char_c in c:
            if current_char == char_c:
                is_in_c = True
                break
        if not is_in_c:
            result_string.append(current_char)
    result_string = ''.join(result_string)
    reversed_string = result_string[::-1]
    is_palindrome = reversed_string == result_string
    return [result_string, is_palindrome]