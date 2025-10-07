def sum_to_n(aux_param: int) -> int:
    aux_accumulator: int = 0
    aux_iterator: int = 0
    while aux_iterator <= aux_param:
        aux_accumulator += aux_iterator
        aux_iterator += 1
    return aux_accumulator