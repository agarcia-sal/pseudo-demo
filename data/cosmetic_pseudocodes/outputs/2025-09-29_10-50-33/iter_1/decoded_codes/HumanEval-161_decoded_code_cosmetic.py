from typing import List

def solve(string_input: str) -> str:
    flag: bool = False
    new_chars: List[str] = []
    for current_char in string_input:
        if current_char.isalpha():
            if current_char.isupper():
                new_chars.append(current_char.lower())
            else:
                new_chars.append(current_char.upper())
            flag = True
        else:
            new_chars.append(current_char)

    result: str = ''.join(new_chars)

    if not flag:
        reversed_result: str = result[::-1]
        return reversed_result
    else:
        return result