from typing import List


def match_parens(params_0: List[str]) -> str:
    def check(param_0: str) -> bool:
        def helper(param_1: int, param_2: int) -> bool:
            if param_1 >= len(param_0):
                return param_2 == 0
            if param_2 < 0:
                return False
            return helper(param_1 + 1, param_2 + (1 if param_0[param_1] == '(' else -1))

        return helper(0, 0)

    var_0 = params_0[0] + params_0[1]
    var_1 = params_0[1] + params_0[0]

    if check(var_0) or check(var_1):
        return 'Yes'
    return 'No'