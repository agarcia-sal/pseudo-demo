def fib(integer_x: int) -> int:
    integer_y: int = 0
    integer_z: int = 1
    integer_w: int = 0

    while integer_w < integer_x:
        integer_a: int = integer_z
        integer_z = integer_y + integer_z
        integer_y = integer_a
        integer_w += 1

    return integer_y if integer_x == 0 else integer_z - integer_y