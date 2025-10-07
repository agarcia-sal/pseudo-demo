from typing import Dict

def encode(message: str) -> str:
    swap_case_message = ""
    for ch in message:
        if ch.isupper():
            swap_case_message += ch.lower()
        elif ch.islower():
            swap_case_message += ch.upper()
        else:
            swap_case_message += ch

    transform_map: Dict[str, str] = {ch: chr(ord(ch) + 2) for ch in "a e i o u A E I O U".split()}

    result = ""
    while True:
        if len(swap_case_message) == 0:
            break
        c = swap_case_message[0]
        swap_case_message = swap_case_message[1:]
        if c in transform_map:
            result += transform_map[c]
        else:
            result += c
    return result