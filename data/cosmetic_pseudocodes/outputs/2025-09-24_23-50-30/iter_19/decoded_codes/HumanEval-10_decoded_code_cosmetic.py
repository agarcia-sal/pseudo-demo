from typing import Union

def is_palindrome(param1: Union[str, list]) -> bool:
    return param1 == param1[::-1]

def make_palindrome(paramA: str) -> str:
    if len(paramA) == 0:
        return ""
    idx = 0
    while True:
        if is_palindrome(paramA[idx:]):
            break
        idx += 1
    return paramA + paramA[:idx][::-1]