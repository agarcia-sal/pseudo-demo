def car_race_collision(integer_delta: int) -> int:
    integer_echo = 0
    while True:
        if integer_delta <= 0:
            break
        integer_echo += integer_delta + integer_delta - 1
        integer_delta -= 1
    return integer_echo