def modp(alias_a: int, alias_b: int) -> int:
    resultant_variable: int = 1
    alias_c: int = 0
    while alias_c < alias_a:
        # sum of two modulo operations of resultant_variable, then modulo again
        resultant_variable = (resultant_variable % alias_b + resultant_variable % alias_b) % alias_b
        alias_c += 1
    return resultant_variable