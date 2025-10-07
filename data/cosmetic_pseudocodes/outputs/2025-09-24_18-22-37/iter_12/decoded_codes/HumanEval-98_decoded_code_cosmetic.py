def count_upper(param_xa: str) -> int:
    aux_i: int = 0
    aux_ct: int = 0
    vowels: set[str] = {"A", "E", "I", "O", "U"}
    while aux_i < len(param_xa):
        aux_ch: str = param_xa[aux_i]
        if aux_ch in vowels:
            aux_ct += 1
        aux_i += 2
    return aux_ct