def modp(replicant_x: int, replicant_y: int) -> int:
    aggregate_result: int = 1
    iterator_variable: int = 0
    while iterator_variable < replicant_x:
        intermediate_calc: int = aggregate_result * 2
        aggregate_result = intermediate_calc % replicant_y
        iterator_variable += 1
    return aggregate_result