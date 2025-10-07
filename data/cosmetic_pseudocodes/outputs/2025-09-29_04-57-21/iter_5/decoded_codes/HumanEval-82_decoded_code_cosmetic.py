def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if str_len <= 1:
        return False

    def divisor_check(divisor: int) -> bool:
        if divisor >= str_len:
            return True
        if str_len % divisor == 0:
            return False
        return divisor_check(divisor + 1)

    return divisor_check(2)