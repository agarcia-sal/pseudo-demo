class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        for i in range(1, n + 1):
            temp1 = self.h[i - 1] * base + ord(s[i - 1])
            self.h[i] = temp1 - (temp1 // mod) * mod
            temp2 = self.p[i - 1] * base
            self.p[i] = temp2 - (temp2 // mod) * mod

    def query(self, l, r):
        subhash = self.h[r] - self.h[l - 1] * self.p[r - l + 1]
        return subhash - (subhash // self.mod) * self.mod


class Solution:
    def findAnswer(self, parent, s):
        length_s = len(s)
        graph = [[] for _ in range(length_s)]
        for i in range(1, length_s):
            graph[parent[i]].append(i)

        traversal_string = []
        position_map = {}

        def recursive_search(current_node):
            start_pos = len(traversal_string) + 1  # 1-based indexing for hashing
            for neighbor in graph[current_node]:
                recursive_search(neighbor)
            traversal_string.append(s[current_node])
            end_pos = len(traversal_string)
            position_map[current_node] = (start_pos, end_pos)

        recursive_search(0)

        constant_base = 33331
        constant_mod = 998244353

        hash_object1 = Hashing(traversal_string, constant_base, constant_mod)
        reversed_traversal = traversal_string[::-1]
        hash_object2 = Hashing(reversed_traversal, constant_base, constant_mod)

        result_list = []
        for idx in range(length_s):
            left_bound, right_bound = position_map[idx]
            segment_length = right_bound - left_bound + 1
            half_len = segment_length // 2
            half_query1 = hash_object1.query(left_bound, left_bound + half_len - 1)
            rev_start = length_s - right_bound + 1
            rev_end = rev_start + half_len - 1
            half_query2 = hash_object2.query(rev_start, rev_end)
            is_palindrome_half = (half_query1 == half_query2)
            result_list.append(is_palindrome_half)

        return result_list