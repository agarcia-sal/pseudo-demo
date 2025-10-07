def starts_one_ends(integer_n: int) -> int:
    def nested_case(integer_q: int) -> int:
        if integer_q == 1:
            return 1
        else:
            return 18 * (10 ** (integer_q - 2))

    return nested_case(integer_n)