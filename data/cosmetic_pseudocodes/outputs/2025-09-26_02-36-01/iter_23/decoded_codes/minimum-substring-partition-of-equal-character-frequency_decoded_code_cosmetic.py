from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        def dfs(w: int) -> int:
            if w > n - 1:
                return 0

            b5 = defaultdict(int)
            f9 = defaultdict(int)

            m8 = (n - w)

            def rec(v: int, acc: int) -> int:
                if v > n - 1:
                    return acc

                if b5[s[v]] != 0:
                    f9[b5[s[v]]] -= 1
                    if f9[b5[s[v]]] <= 0:
                        del f9[b5[s[v]]]

                b5[s[v]] += 1
                f9[b5[s[v]]] = f9.get(b5[s[v]], 0) + 1

                if len(f9) == 1:
                    s7 = 1 + dfs(v + 1)
                else:
                    s7 = acc

                if s7 < acc:
                    return rec(v + 1, s7)
                else:
                    return rec(v + 1, acc)

            return rec(w, m8)

        return dfs(0)