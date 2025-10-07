from typing import List

def incr_list(var0: List[int]) -> List[int]:
    var1: List[int] = []
    var2: int = 0
    while var2 < len(var0):
        var1.append(var0[var2] + 1)
        var2 += 1
    return var1