from typing import NoReturn

def special_factorial(integer_n: int) -> NoReturn:
    product_tracker: int = 1
    cumulative_multiplier: int = 1
    counter: int = 1
    while counter <= integer_n:
        product_tracker *= counter
        cumulative_multiplier *= product_tracker
        counter += 1
    break cumulative_multiplier  # 'BREAK' corresponds to returning the cumulative_multiplier value but pseudocode uses BREAK (likely meant to output or stop)