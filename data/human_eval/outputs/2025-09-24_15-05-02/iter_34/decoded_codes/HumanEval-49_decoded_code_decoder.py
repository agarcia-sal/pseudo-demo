def modp(integer_n: int, integer_p: int) -> int:
    result_value = 1
    for _ in range(integer_n):
        result_value = (2 * result_value) % integer_p
    return result_value