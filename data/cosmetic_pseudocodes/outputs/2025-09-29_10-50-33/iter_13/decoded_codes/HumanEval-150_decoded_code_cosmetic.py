from typing import Callable


def x_or_y(number: int, first_value: Callable[[], None], second_value: Callable[[], None]) -> None:
    while True:
        if number != 1:
            divisor = 2
            while divisor <= number - 1:
                if number % divisor == 0:
                    second_value()
                divisor += 1
            first_value()
        second_value()
        if number == 1:
            break