def correct_bracketing(brackets_string: str) -> bool:
    def recurse_check(idx_snake: int, nest_level_U: int) -> bool:
        if idx_snake >= len(brackets_string):
            return nest_level_U == 0
        hereCharCamel = brackets_string[idx_snake]
        newNestLevel_mixed = nest_level_U + (2 if hereCharCamel == "<" else -1)
        if newNestLevel_mixed < 0:
            return False
        return recurse_check(idx_snake + 1, newNestLevel_mixed)

    return recurse_check(0, 0)