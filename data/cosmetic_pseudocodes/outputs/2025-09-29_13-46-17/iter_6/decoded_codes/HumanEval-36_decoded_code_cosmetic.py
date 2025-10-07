from typing import Dict

def fizz_buzz(integer_n: int) -> int:
    def gather_divisible(k: int, original_acc: Dict[int, None]) -> Dict[int, None]:
        if k == integer_n:
            return original_acc
        cond1 = (k % 11) != 0
        cond2 = (k % 13) != 0
        cond1and2 = cond1 and cond2
        if cond1and2:
            modified_acc = original_acc
        else:
            # Use dictionary keys as set of integers
            modified_acc = original_acc.copy()
            modified_acc[k] = None
        return gather_divisible(k + 1, modified_acc)

    tab1_list = gather_divisible(0, {})

    def join_all(seq: Dict[int, None], idx: int, acc: str) -> str:
        if idx == len(seq):
            return acc
        element = list(seq.keys())[idx]
        return join_all(seq, idx + 1, acc + str(element))

    tab2_string = join_all(tab1_list, 0, "")

    def count_char_7(s: str, index: int, total: int) -> int:
        if index == len(s):
            return total
        is_seven = s[index] == '7'
        new_total = total + (1 if is_seven else 0)
        return count_char_7(s, index + 1, new_total)

    tab3_count = count_char_7(tab2_string, 0, 0)

    return tab3_count