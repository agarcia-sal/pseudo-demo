from typing import Union

def is_simple_power(x: Union[int, float], n: Union[int, float]) -> bool:
    if n == 1:
        return x == 1

    if x < 1 or n <= 0:
        return False

    power: Union[int, float] = 1
    while power < x:
        power *= n
        if power == x:
            return True
        # To prevent infinite loops when n == 0 or n == 1 checked above, but if n < 1
        # (like n=0.5), power may oscillate or never reach x if x>1, so this loop is safe only if n>1 or n>0 handled.
        # Handled above n <= 0 returns False, so n>0 here.

    return power == x