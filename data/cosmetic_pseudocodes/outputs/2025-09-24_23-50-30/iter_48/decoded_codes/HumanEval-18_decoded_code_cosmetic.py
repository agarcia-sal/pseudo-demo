from typing import Union

def how_many_times(param1: Union[str, list], param2: Union[str, list]) -> int:
    var1: int = len(param1)
    var2: int = len(param2)
    var3: int = 0
    var4: int = 0
    while var3 <= var1 - var2:
        if not (param1[var3:var3 + var2] != param2):
            var4 += 1
        var3 += 1
    return var4