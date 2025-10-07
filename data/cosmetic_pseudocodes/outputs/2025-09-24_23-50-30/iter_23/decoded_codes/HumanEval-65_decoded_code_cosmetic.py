from typing import Union

def circular_shift(numeric_alpha: Union[int, float], numeric_beta: int) -> str:
    list_chars = list(str(numeric_alpha))
    length = len(list_chars)
    if numeric_beta > length:
        return ''.join(reversed(list_chars))
    return ''.join(list_chars[length - numeric_beta :] + list_chars[: length - numeric_beta])