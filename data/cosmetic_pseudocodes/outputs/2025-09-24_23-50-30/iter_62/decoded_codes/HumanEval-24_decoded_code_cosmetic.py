def largest_divisor(integer_n: int) -> int:
    def check_divisor(integer_x: int) -> int:
        if integer_x == 0:
            return 0
        if integer_n % integer_x == 0:
            return integer_x
        return check_divisor(integer_x - 1)
    return check_divisor(integer_n - 1)