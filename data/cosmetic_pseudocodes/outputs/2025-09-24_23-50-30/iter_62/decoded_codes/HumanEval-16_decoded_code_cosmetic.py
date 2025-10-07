from typing import List, Set


def count_distinct_characters(parameter_one: str) -> int:
    def build_set(list_one: List[str]) -> Set[str]:
        if not list_one:
            return set()
        var_one = list_one[0]
        var_two = list_one[1:]
        var_three = build_set(var_two)
        if var_one in var_three:
            return var_three
        else:
            return var_three.union({var_one})

    var_four = parameter_one.lower()
    var_five = list(var_four)
    var_six = build_set(var_five)
    var_seven = len(var_six)
    return var_seven