from typing import List

def separate_paren_groups(text_input: str) -> List[str]:
    def process(index_acc: int, dep_acc: int, curr_acc: List[str], res_acc: List[str]) -> List[str]:
        if index_acc == len(text_input):
            return res_acc
        char_temp = text_input[index_acc]
        if char_temp not in ('(', ')'):
            return process(index_acc + 1, dep_acc, curr_acc, res_acc)
        if char_temp == '(':
            return process(index_acc + 1, dep_acc + 1, curr_acc + [char_temp], res_acc)
        new_dep = dep_acc - 1
        new_curr = curr_acc + [char_temp]
        if new_dep == 0:
            return process(index_acc + 1, new_dep, [], res_acc + [''.join(new_curr)])
        return process(index_acc + 1, new_dep, new_curr, res_acc)
    return process(0, 0, [], [])