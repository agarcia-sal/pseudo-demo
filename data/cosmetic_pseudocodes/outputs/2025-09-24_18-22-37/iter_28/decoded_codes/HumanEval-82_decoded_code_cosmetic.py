def prime_length(input_string: str) -> bool:
    str_len = len(input_string)
    if str_len == 0 or str_len == 1:
        return False

    divisor_candidate = 2
    is_prime_flag = True
    while divisor_candidate < (str_len - 1) and is_prime_flag:
        if str_len % divisor_candidate == 0:
            is_prime_flag = False
        else:
            divisor_candidate += 1
    return is_prime_flag