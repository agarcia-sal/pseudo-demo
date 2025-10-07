class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        alpha_counts = {}
        for ch in word:
            alpha_counts[ch] = alpha_counts.get(ch, 0) + 1

        freq_list = list(alpha_counts.values())
        freq_list.sort()

        min_del = float('inf')
        n = len(freq_list)
        for p in range(n):
            max_freq = freq_list[p] + k
            delt = 0
            for q in range(p + 1, n):
                if freq_list[q] > max_freq:
                    delt += freq_list[q] - max_freq
            for r in range(p):
                delt += freq_list[r]
            if delt < min_del:
                min_del = delt

        return min_del