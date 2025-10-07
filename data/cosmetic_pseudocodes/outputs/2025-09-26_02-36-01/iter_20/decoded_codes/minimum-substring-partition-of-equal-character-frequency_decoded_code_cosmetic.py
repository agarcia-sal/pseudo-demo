from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(x: int) -> int:
            def inc_map(m: dict, k):
                m[k] = m.get(k, 0) + 1

            def dec_map(m: dict, k):
                if k in m:
                    m[k] -= 1
                    if m[k] == 0:
                        del m[k]

            if x >= len(s):
                return 0

            local_a = dict()
            local_b = dict()
            result_v = len(s) - x

            def helper(y: int, cnt_map: dict, freq_map: dict, best_val: int) -> int:
                if y >= len(s):
                    return best_val

                c = s[y]

                prev_count = cnt_map.get(c, 0)

                dec_map(freq_map, prev_count)
                inc_map(cnt_map, c)
                inc_map(freq_map, cnt_map[c])

                if len(freq_map) == 1:
                    candidate = 1 + dfs(y + 1)
                    if candidate < best_val:
                        best_val = candidate

                return best_val

            i = x
            while i < len(s):
                result_v = helper(i, local_a, local_b, result_v)
                i += 1

            return result_v

        return dfs(0)