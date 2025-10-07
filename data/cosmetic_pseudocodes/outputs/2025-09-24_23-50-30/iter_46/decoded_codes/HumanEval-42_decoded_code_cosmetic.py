from typing import List

def incr_list(var1: List[int]) -> List[int]:
    var2: List[int] = []

    def add_element(var3: int) -> None:
        if var3 < len(var1):
            var2.append(var1[var3] + 1)
            add_element(var3 + 1)
        else:
            return

    add_element(0)
    return var2