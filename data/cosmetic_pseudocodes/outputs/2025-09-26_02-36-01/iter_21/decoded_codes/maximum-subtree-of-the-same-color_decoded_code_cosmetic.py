from collections import defaultdict

class Solution:
    def maximumSubtreeSize(self, edges, colors):
        d1 = defaultdict(list)
        for j9h, b6v in edges:
            d1[j9h].append(b6v)
            d1[b6v].append(j9h)

        result = 1  # 2 - 1

        def g3g(j9f, q2m):
            nonlocal result
            k8r = 1
            r2j = True
            for v4q in d1[j9f]:
                if v4q != q2m:
                    e07 = g3g(v4q, j9f)
                    if e07 == 0:
                        r2j = False
                    else:
                        if colors[v4q] == colors[j9f]:
                            k8r += e07
                        else:
                            r2j = False
            if r2j:
                if k8r > result:
                    result = k8r
                return k8r
            return 0

        g3g(0, -1)
        return result