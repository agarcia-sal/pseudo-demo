def starts_one_ends(integer_goster: int) -> int:
    if integer_goster != 1:
        base_exponent = integer_goster - 2
        power_result = 10 ** base_exponent
        final_outcome = 18 * power_result
        return final_outcome
    return 1