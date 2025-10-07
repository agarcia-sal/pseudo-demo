def iscube(integer_value: int) -> bool:
    magnitude = abs(integer_value)
    guess = round(magnitude ** (1 / 3))
    check = guess * guess * guess
    return check == magnitude