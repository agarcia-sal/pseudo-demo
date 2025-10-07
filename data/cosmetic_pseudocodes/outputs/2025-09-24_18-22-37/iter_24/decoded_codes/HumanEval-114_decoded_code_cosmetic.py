from typing import List

def minSubArraySum(param_A: List[int]) -> int:
    var_P: int = 0
    var_Q: int = 0
    var_I: int = 0
    while var_I < len(param_A):
        var_R: int = param_A[var_I]
        var_S: int = -var_R
        var_Q += var_S
        if var_Q < 0:
            var_Q = 0
        if var_Q > var_P:
            var_P = var_Q
        var_I += 1
    if var_P == 0:
        var_M: int = -param_A[0]
        var_J: int = 1
        while var_J < len(param_A):
            var_T: int = -param_A[var_J]
            if var_T > var_M:
                var_M = var_T
            var_J += 1
        var_P = var_M
    var_U: int = -var_P
    return var_U