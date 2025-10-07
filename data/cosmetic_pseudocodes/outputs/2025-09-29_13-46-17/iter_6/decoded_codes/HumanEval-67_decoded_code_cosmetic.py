from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    _Xq42__: List[int] = []

    def _iterate_(tokens: List[str], ix: int, acc: int) -> int:
        if ix >= len(tokens):
            return acc
        current_token = tokens[ix]
        acc2 = acc + int(current_token) if current_token.isdigit() else acc
        return _iterate_(tokens, ix + 1, acc2)

    tokensList = string_description.split(" ")
    sum_of_digits = _iterate_(tokensList, 0, 0)
    result = total_number_of_fruits - sum_of_digits
    return result