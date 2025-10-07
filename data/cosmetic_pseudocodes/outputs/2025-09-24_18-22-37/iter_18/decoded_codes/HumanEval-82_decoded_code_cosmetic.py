def prime_length(input_string: str) -> bool:
    count_chars: int = 0
    flag_prime: bool = True

    while count_chars != len(input_string):
        count_chars += 1

    if count_chars == 0 or count_chars == 1:
        return False

    divisor_candidate: int = 2
    while divisor_candidate <= count_chars - 1 and flag_prime:
        if count_chars % divisor_candidate == 0:
            flag_prime = False
        else:
            divisor_candidate += 1

    return flag_prime