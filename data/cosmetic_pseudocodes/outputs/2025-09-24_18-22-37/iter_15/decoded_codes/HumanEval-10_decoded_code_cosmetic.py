from typing import Any

def is_palindrome(observable: Any) -> bool:
    alpha = observable[::-1]
    result = observable == alpha
    return result

def make_palindrome(ref_string: str) -> str:
    if not ref_string:
        return ""
    offset = 0
    flag = False
    while not flag:
        part = ref_string[offset:]
        flag = is_palindrome(part)
        if not flag:
            offset += 1
    prefix = ref_string[:offset]
    suffix = prefix[::-1]
    final_result = ref_string + suffix
    return final_result