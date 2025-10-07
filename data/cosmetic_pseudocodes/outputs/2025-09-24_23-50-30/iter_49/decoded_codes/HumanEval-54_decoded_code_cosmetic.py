from typing import Sequence

def same_chars(param_alpha: Sequence[str], param_beta: Sequence[str]) -> bool:
    def build_map(target_seq: Sequence[str]) -> dict[str, bool]:
        local_map: dict[str, bool] = {}
        idx = 0
        while idx < len(target_seq):
            local_map[target_seq[idx]] = True
            idx += 1
        return local_map

    map_one = build_map(param_alpha)
    map_two = build_map(param_beta)

    result_flag = True
    for key in map_one.keys():
        if key not in map_two:
            result_flag = False
            break
    if result_flag:
        for key in map_two.keys():
            if key not in map_one:
                result_flag = False
                break

    return result_flag