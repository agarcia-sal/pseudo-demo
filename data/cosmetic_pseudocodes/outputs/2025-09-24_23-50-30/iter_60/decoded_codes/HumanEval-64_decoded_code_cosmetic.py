from typing import Callable

def vowels_count(var1: str) -> int:
    var2: str = "aeiouAEIOU"

    def count_chars(var3: str, var4: str, var5: int) -> int:
        if var5 == len(var3):
            return 0
        return (var3[var5] in var4) + count_chars(var3, var4, var5 + 1)

    var6: int = count_chars(var1, var2, 0)

    if var1 and (var1[-1] == 'y' or var1[-1] == 'Y'):
        var6 += 1

    return var6