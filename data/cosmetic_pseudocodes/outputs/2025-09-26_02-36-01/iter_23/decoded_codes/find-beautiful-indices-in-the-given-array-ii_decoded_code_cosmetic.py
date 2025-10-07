from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def check_and_collect_A(pos: int, acc: List[int]) -> List[int]:
            if pos > len(s) - len(a):
                return acc
            if s[pos:pos + len(a)] == a:
                return check_and_collect_A(pos + 1, acc + [pos])
            else:
                return check_and_collect_A(pos + 1, acc)

        def check_and_collect_B(pos: int, acc: List[int]) -> List[int]:
            if pos > len(s) - len(b):
                return acc
            new_acc = acc + [pos] if s[pos:pos + len(b)] == b else acc
            return check_and_collect_B(pos + 1, new_acc)

        ai_indices = check_and_collect_A(0, [])
        bi_indices = check_and_collect_B(0, [])

        def find_beautiful(i: int, j: int, result: List[int]) -> List[int]:
            if i >= len(ai_indices) or j >= len(bi_indices):
                return result
            diff = ai_indices[i] - bi_indices[j]
            abs_diff = diff if diff >= 0 else -diff
            if abs_diff <= k:
                return find_beautiful(i + 1, j, result + [ai_indices[i]])
            else:
                if ai_indices[i] < bi_indices[j]:
                    return find_beautiful(i + 1, j, result)
                else:
                    return find_beautiful(i, j + 1, result)

        return find_beautiful(0, 0, [])