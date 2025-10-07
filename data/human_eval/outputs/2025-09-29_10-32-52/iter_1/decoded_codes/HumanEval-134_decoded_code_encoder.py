from typing import Union

def check_if_last_char_is_a_letter(text: str) -> bool:
    last_element = text.split()[-1] if text.split() else ''
    if len(last_element) == 1 and 'a' <= last_element.lower() <= 'z':
        return True
    else:
        return False