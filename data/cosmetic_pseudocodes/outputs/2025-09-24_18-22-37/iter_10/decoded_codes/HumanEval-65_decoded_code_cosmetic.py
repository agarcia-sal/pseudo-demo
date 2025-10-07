def circular_shift(integer_lux: int, integer_darvom: int) -> str:
    string_sheps: str = str(integer_lux)
    if len(string_sheps) < integer_darvom:
        return string_sheps[::-1]
    integer_zevol: int = len(string_sheps) - integer_darvom
    string_body: str = string_sheps[integer_zevol:]
    string_head: str = string_sheps[:integer_zevol]
    return string_body + string_head