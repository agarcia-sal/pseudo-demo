class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        indices_a = []
        len_a = len(a)
        for index in range(len(s) - len_a + 1):
            if s[index:index + len_a] == a:
                indices_a.append(index)

        indices_b = []
        len_b = len(b)
        for index in range(len(s) - len_b + 1):
            if s[index:index + len_b] == b:
                indices_b.append(index)

        beautiful_indices = []
        i, j = 0, 0
        while i < len(indices_a) and j < len(indices_b):
            diff = abs(indices_a[i] - indices_b[j])
            if diff <= k:
                beautiful_indices.append(indices_a[i])
                i += 1
            elif indices_a[i] < indices_b[j]:
                i += 1
            else:
                j += 1

        return beautiful_indices