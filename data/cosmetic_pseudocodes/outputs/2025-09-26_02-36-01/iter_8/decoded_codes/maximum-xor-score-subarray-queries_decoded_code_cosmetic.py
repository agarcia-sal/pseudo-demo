from typing import List

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        p = len(nums)
        q = [[] for _ in range(p)]
        r = [[] for _ in range(p)]
        s = [[] for _ in range(p)]
        t = [[] for _ in range(p)]  # though s and t as lists of lists are created, only t as a flat list is used later

        # Since s and t as lists of lists are not used later, only t as the output list is needed.
        # We'll keep s and t as specified but actual output will be a flat list as per pseudocode's usage of t.

        # We'll overwrite t as a flat list after initialization
        t = []

        u = p - 1
        while u >= 0:
            a0 = nums[u]
            # Insert a0 at position u in q[u] if q and q[u] have length p, else append
            if len(q) == p and len(q[u]) == p:
                q[u].insert(u, a0)
            else:
                q[u].append(a0)

            if len(r) == p and len(r[u]) == p:
                r[u].insert(u, a0)
            else:
                r[u].append(a0)

            u1 = u + 1
            while u1 < p:
                v = q[u][u1 - 1] ^ q[u1][u1]

                if len(q[u]) == p and len(q[u][u1: u1 + 1]) == 1:
                    q[u][u1] = v
                else:
                    # If q[u] not length p or q[u][u1] does not exist, insert at u1
                    if u1 < len(q[u]):
                        q[u].insert(u1, v)
                    else:
                        q[u].append(v)

                w = max(v, r[u][u1 - 1], r[u1][u1])

                if len(r[u]) == p and len(r[u][u1: u1 + 1]) == 1:
                    r[u][u1] = w
                else:
                    if u1 < len(r[u]):
                        r[u].insert(u1, w)
                    else:
                        r[u].append(w)

                u1 += 1
            u -= 1

        for b in queries:
            c, d = b[0], b[1]
            t.append(r[c][d])

        return t