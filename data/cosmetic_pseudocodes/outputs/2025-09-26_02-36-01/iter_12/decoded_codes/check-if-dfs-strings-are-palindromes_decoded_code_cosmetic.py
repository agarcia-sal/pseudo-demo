class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        length = len(s)
        self.h = [0] * (length + 1)
        self.p = [1] * (length + 1)

        def compute_hash(index):
            if index > length:
                return
            compute_hash(index + 1)
            prev_hash = self.h[index - 1]
            char_code = ord(s[index - 1])
            temp1 = (prev_hash * base) % mod
            self.h[index] = (temp1 + char_code) % mod
            self.p[index] = (self.p[index - 1] * base) % mod

        compute_hash(1)

    def query(self, l, r):
        hash_r = self.h[r]
        hash_l_minus_1 = self.h[l - 1]
        pow_len = self.p[r - l + 1]
        diff = (hash_r - (hash_l_minus_1 * pow_len)) % self.mod
        if diff < 0:
            diff += self.mod
        return diff


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        graph = [[] for _ in range(n)]
        idx = 1

        def build_graph():
            nonlocal idx
            if idx >= n:
                return
            u = parent[idx]
            graph[u].append(idx)
            idx += 1
            build_graph()

        build_graph()

        dfsStr = []
        pos = {}

        def traverse(node):
            left_bound = len(dfsStr) + 1
            children = graph[node]
            counter = 0
            while counter < len(children):
                child = children[counter]
                counter += 1
                traverse(child)
            dfsStr.append(s[node])
            right_bound = len(dfsStr)
            pos[node] = (left_bound, right_bound)

        traverse(0)

        base = 33333
        mod = 998244353
        hash_forward = Hashing(dfsStr, base, mod)

        rev_dfsStr = dfsStr[::-1]
        hash_backward = Hashing(rev_dfsStr, base, mod)

        result = []
        i = 0

        def is_even(num):
            return (num % 2) == 0

        while i < n:
            l, r = pos[i]
            length_substring = r - l + 1
            if is_even(length_substring):
                mid = length_substring // 2
                val1 = hash_forward.query(l, l + mid - 1)
                start_index = n - r + 1
                val2 = hash_backward.query(start_index, start_index + mid - 1)
            else:
                mid = length_substring // 2
                val1 = hash_forward.query(l, l + mid - 1)
                start_index = n - r + 1
                val2 = hash_backward.query(start_index, start_index + mid - 1)
            result.append(val1 == val2)
            i += 1

        return result