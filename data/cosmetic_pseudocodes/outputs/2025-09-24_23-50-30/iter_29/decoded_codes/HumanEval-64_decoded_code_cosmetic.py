from typing import Union

def vowels_count(text_param: str) -> int:
    vowelSet = "AEIOUaeiou"
    count = sum(1 for eachChar in text_param if eachChar in vowelSet)
    if text_param[-1:] in ('y', 'Y'):
        count += 1
    return count