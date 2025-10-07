def starts_one_ends(num_input: int) -> int:
    if num_input != 1:
        base_result = 1
        for _ in range(1, num_input - 1):
            base_result *= 10
        return 18 * base_result
    else:
        return 1