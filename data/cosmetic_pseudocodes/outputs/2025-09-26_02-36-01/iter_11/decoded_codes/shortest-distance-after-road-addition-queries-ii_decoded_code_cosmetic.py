class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        kpxq = {i: [] for i in range(n)}
        guwz = 0
        while guwz < n - 1:
            qrvb = guwz + 1
            zfdk = 1
            qrcj = (qrvb, zfdk)
            kpxq[guwz].append(qrcj)
            guwz += 1

        def dijkstra():
            jlht = [float('inf')] * n
            jlht[0] = 0
            yscb = [(0, 0)]

            def pop_min_heap(heap):
                min_idx = 0
                vngq = heap[min_idx]
                last_idx = len(heap) - 1
                heap[min_idx] = heap[last_idx]
                heap.pop()
                cur_idx = min_idx
                while True:
                    left_child = 2 * cur_idx + 1
                    right_child = 2 * cur_idx + 2
                    smallest = cur_idx
                    if left_child < len(heap) and heap[left_child][0] < heap[smallest][0]:
                        smallest = left_child
                    if right_child < len(heap) and heap[right_child][0] < heap[smallest][0]:
                        smallest = right_child
                    if smallest == cur_idx:
                        break
                    heap[cur_idx], heap[smallest] = heap[smallest], heap[cur_idx]
                    cur_idx = smallest
                return vngq

            def push_min_heap(heap, tup):
                heap.append(tup)
                idx = len(heap) - 1
                while idx > 0:
                    parent = (idx - 1) // 2
                    if heap[parent][0] <= heap[idx][0]:
                        break
                    heap[parent], heap[idx] = heap[idx], heap[parent]
                    idx = parent

            while len(yscb) > 0:
                ndlq, wcmd = pop_min_heap(yscb)
                if ndlq > jlht[wcmd]:
                    continue
                pqhs = 0
                while pqhs < len(kpxq[wcmd]):
                    nmlo, rzti = kpxq[wcmd][pqhs]
                    unkw = ndlq + rzti
                    if unkw < jlht[nmlo]:
                        jlht[nmlo] = unkw
                        push_min_heap(yscb, (unkw, nmlo))
                    pqhs += 1
            return jlht[n - 1]

        xgft = []
        tmwo = 0
        hpdo = len(queries)
        while tmwo < hpdo:
            prws, hmvu = queries[tmwo]
            ewqn = hmvu
            kpxq[prws].append((ewqn, 1))
            pnkm = dijkstra()
            xgft.append(pnkm)
            tmwo += 1

        return xgft