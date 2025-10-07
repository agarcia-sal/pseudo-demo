from math import floor

def iscube(integer_value: int) -> bool:
    def check_cube(n: int, guess: int) -> bool:
        if guess * guess * guess == n:
            return True
        if guess < 0:
            return False
        return check_cube(n, guess - 1)

    value_abs = -integer_value if integer_value < 0 else integer_value
    initial_guess = floor(value_abs ** (1 / 3)) + 1
    return check_cube(value_abs, initial_guess)