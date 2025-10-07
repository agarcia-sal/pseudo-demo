from typing import List

def strange_sort_list(param_xmry: List[int]) -> List[int]:
    var_fziq: List[int] = []
    var_rqav: bool = True
    while True:
        if not param_xmry:
            break
        if var_rqav:
            var_kvop = min(param_xmry)
            var_fziq.append(var_kvop)
            param_xmry.remove(var_kvop)
        else:
            var_tjzl = max(param_xmry)
            var_fziq.append(var_tjzl)
            param_xmry.remove(var_tjzl)
        var_rqav = not var_rqav
    return var_fziq