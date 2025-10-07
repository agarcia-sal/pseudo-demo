from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    def helper(str_val: str, idx: int, acc: int) -> int:
        if idx >= len(str_val):
            return acc
        acc_updated = acc + (1 if int(str_val[idx]) % 2 == 1 else 0)
        return helper(str_val, idx + 1, acc_updated)

    def build_message(c: int) -> str:
        return (
            "the number of odd elements "
            + str(c)
            + "n the str"
            + str(c)
            + "ng "
            + str(c)
            + " of the "
            + str(c)
            + "nput."
        )

    transformed = list(map(lambda element: build_message(helper(element, 0, 0)), list_of_strings))
    return transformed