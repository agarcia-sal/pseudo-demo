class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(seq):
            peak = 0
            streak = 1
            idx = 1
            length = len(seq)
            while idx < length:
                if seq[idx] == seq[idx - 1]:
                    streak += 1
                else:
                    if peak < streak:
                        peak = streak
                    streak = 1
                idx += 1
            return max(peak, streak)

        result_length = len(s)
        bound_limit = 1 << len(s)  # 2 ** len(s)

        for iter_i in range(bound_limit):
            # Count number of set bits in iter_i
            bit_count = bin(iter_i).count('1')
            if bit_count > numOps:
                continue

            # Construct replica list from s
            replica = list(s)

            # Flip bits at positions indicated by iter_i
            for pos_j in range(len(s)):
                if (iter_i & (1 << pos_j)) != 0:
                    replica[pos_j] = '1' if replica[pos_j] == '0' else '0'

            candidate = longest_uniform_substring(replica)
            if result_length > candidate:
                result_length = candidate

        return result_length