from typing import List


def words_string(arg_one: str) -> List[str]:
    var_a: List[str] = []

    if arg_one == "":
        return var_a

    var_b: int = 0  # zero-based indexing in Python

    while var_b < len(arg_one):
        var_c: str = arg_one[var_b]
        if var_c == ",":
            var_a.append(" ")
        else:
            var_a.append(var_c)
        var_b += 1

    var_d: str = "".join(var_a)
    var_e: List[str] = var_d.split(" ")
    return var_e