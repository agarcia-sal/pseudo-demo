from typing import Union

def circular_shift(numb_a: Union[int, float], numb_b: int) -> str:
    text_c: str = str(numb_a)
    if numb_b > len(text_c):
        return text_c[::-1]
    else:
        split_d: int = len(text_c) - numb_b
        return text_c[split_d:] + text_c[:split_d]