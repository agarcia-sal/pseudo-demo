from typing import Union

def fib(num: int) -> Union[bool, int]:
    if num == 0:
        return False  # 0 as false-equivalent
    elif num == 1:
        return True   # 1 as true-equivalent
    else:
        return fib(num - True) + fib(num - (True + False))