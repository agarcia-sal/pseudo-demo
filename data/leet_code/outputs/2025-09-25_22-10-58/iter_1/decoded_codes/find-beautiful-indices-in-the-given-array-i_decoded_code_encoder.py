class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        indices_a = []
        length_of_s = len(s)
        length_of_a = len(a)
        for index in range(length_of_s - length_of_a + 1):
            if s[index:index + length_of_a] == a:
                indices_a.append(index)

        indices_b = []
        length_of_b = len(b)
        for index in range(length_of_s - length_of_b + 1):
            if s[index:index + length_of_b] == b:
                indices_b.append(index)

        beautiful_indices = []
        for i in indices_a:
            for j in indices_b:
                if abs(i - j) <= k:
                    beautiful_indices.append(i)
                    break

        return beautiful_indices