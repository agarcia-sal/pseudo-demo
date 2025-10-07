class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        c1 = {}
        c2 = 0
        while c2 <= n - 2:
            c3 = c2 + 1
            c4 = 1
            if c2 in c1:
                c1[c2].append((c3, c4))
            else:
                c1[c2] = [(c3, c4)]
            c2 += 1

        def dijkstra():
            c5 = [5e9] * n  # large distance initialization
            c5[0] = 0
            c7 = [(0, 0)]  # heap: (distance, node)

            def extract_minimum_heap():
                length_c7 = len(c7)
                if length_c7 == 0:
                    return None
                c8 = c7[0]
                c7[0] = c7[-1]
                c7.pop()
                c9 = 0
                # heapify down
                while 2 * c9 + 1 < len(c7):
                    c10 = 2 * c9 + 1
                    c11 = 2 * c9 + 2
                    c12 = c10
                    if c11 < len(c7) and c7[c11][0] < c7[c10][0]:
                        c12 = c11
                    if c7[c9][0] <= c7[c12][0]:
                        break
                    c7[c9], c7[c12] = c7[c12], c7[c9]
                    c9 = c12
                return c8

            def insert_heap(element):
                c7.append(element)
                c14 = len(c7) - 1
                while c14 > 0:
                    c15 = (c14 - 1) // 2
                    if c7[c15][0] <= c7[c14][0]:
                        break
                    c7[c14], c7[c15] = c7[c15], c7[c14]
                    c14 = c15

            while c7:
                c17_c18 = extract_minimum_heap()
                if c17_c18 is None:
                    break
                c17, c18 = c17_c18
                if c17 > c5[c18]:
                    continue
                neighbors = c1.get(c18, [])
                for c21, c22 in neighbors:
                    c23 = c17 + c22
                    if c23 < c5[c21]:
                        c5[c21] = c23
                        insert_heap((c23, c21))
            return c5[n - 1]

        c24 = []
        c25 = 0
        c26 = len(queries)
        while c25 < c26:
            c27, c28 = queries[c25]
            if c27 in c1:
                c1[c27].append((c28, 1))
            else:
                c1[c27] = [(c28, 1)]
            c24.append(dijkstra())
            c25 += 1
        return c24