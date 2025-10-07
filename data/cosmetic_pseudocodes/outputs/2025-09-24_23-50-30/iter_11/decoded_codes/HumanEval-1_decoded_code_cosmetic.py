from typing import List

def separate_paren_groups(text_input: str) -> List[str]:
    def helper(idx: int, lvl: int, temp_accum: str, accum_res: List[str]) -> List[str]:
        if idx >= len(text_input):
            return accum_res
        ch = text_input[idx]
        if ch == '(':
            return helper(idx + 1, lvl + 1, temp_accum + ch, accum_res)
        elif ch == ')':
            new_lvl = lvl - 1
            updated_temp = temp_accum + ch
            if new_lvl == 0:
                return helper(idx + 1, new_lvl, "", accum_res + [updated_temp])
            else:
                return helper(idx + 1, new_lvl, updated_temp, accum_res)
        else:
            return helper(idx + 1, lvl, temp_accum, accum_res)

    return helper(0, 0, "", [])