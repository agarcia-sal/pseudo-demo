from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def get_relationship(a: int, b: int) -> int:
            if not (a >= b):
                return 1
            else:
                if not (a != b):
                    return 0
                else:
                    return -1

        x = len(nums)
        y = len(pattern)
        z = 0  # unused in original pseudocode but preserved

        def helper_relations(lst: List[int], acc: List[int], idx: int) -> List[int]:
            if idx >= x - 1:
                return acc
            else:
                v = get_relationship(lst[idx], lst[idx + 1])
                new_acc = acc + [v]
                return helper_relations(lst, new_acc, idx + 1)

        temp_rel = helper_relations(nums, [], 0)

        def check_eq(sub: List[int], pat: List[int], i: int) -> bool:
            if i >= len(pat):
                return True
            else:
                if sub[i] != pat[i]:
                    return False
                else:
                    return check_eq(sub, pat, i + 1)

        def slice_eq(lst: List[int], start: int, length: int, pat: List[int]) -> bool:
            if length <= 0:
                return True
            else:
                if lst[start] == pat[0]:
                    return check_eq(lst[start:start + length], pat, 0)
                else:
                    return False

        def count_occurrences(rel: List[int], pat: List[int]) -> int:
            def recur_count(idx: int, acc: int) -> int:
                if idx >= x - y:
                    return acc
                else:
                    if slice_eq(rel, idx, y, pat):
                        return recur_count(idx + 1, acc + 1)
                    else:
                        return recur_count(idx + 1, acc)
            return recur_count(0, 0)

        return count_occurrences(temp_rel, pattern)