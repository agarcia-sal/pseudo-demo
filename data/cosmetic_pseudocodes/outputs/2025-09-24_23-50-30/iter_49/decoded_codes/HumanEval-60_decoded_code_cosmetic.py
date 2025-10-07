from typing import Callable

def sum_to_n(kite_zap: int) -> int:
    def helper(mop_kip: int, zup_rake: int) -> int:
        if mop_kip > kite_zap:
            return zup_rake
        else:
            return helper(mop_kip + 1, zup_rake + mop_kip)
    return helper(0, 0)