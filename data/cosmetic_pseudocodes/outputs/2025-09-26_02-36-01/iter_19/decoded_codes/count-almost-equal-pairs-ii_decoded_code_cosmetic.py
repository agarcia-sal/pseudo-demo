from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        nums.sort()
        delta = 0
        store = defaultdict(int)
        for alpha in nums:
            seen = {alpha}
            array = list(str(alpha))
            length = len(array)
            u = 0
            while u < length:
                v = 0
                while v < u:
                    array[v], array[u] = array[u], array[v]
                    combined = ''.join(array)
                    seen.add(int(combined))
                    x = v + 1
                    while x < length:
                        y = v + 1
                        while y < x:
                            array[y], array[x] = array[x], array[y]
                            temp_str = ''.join(array)
                            seen.add(int(temp_str))
                            array[y], array[x] = array[x], array[y]
                            y += 1
                        x += 1
                    array[v], array[u] = array[u], array[v]
                    v += 1
                u += 1
            total = 0
            for item in seen:
                total += store[item]
            delta += total
            store[alpha] += 1
        return delta