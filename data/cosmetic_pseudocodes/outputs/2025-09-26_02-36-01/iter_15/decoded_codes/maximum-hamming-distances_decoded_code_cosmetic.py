class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        # Convert each number in nums to an m-length binary string
        bin_strings = []
        for num in nums:
            b = bin(num)[2:]  # binary representation without '0b'
            # Take the last m bits, pad with '0' on the left if needed
            if len(b) < m:
                s = '0' * (m - len(b)) + b
            else:
                s = b[-m:]
            bin_strings.append(s)

        def hamming_distance(bin1: str, bin2: str) -> int:
            # Count differing bits between two equal length binary strings
            return sum(c1 != c2 for c1, c2 in zip(bin1, bin2))

        result = []
        n = len(nums)
        for i in range(n):
            max_dist = 0
            for j in range(n):
                if i != j:
                    dist = hamming_distance(bin_strings[i], bin_strings[j])
                    if dist > max_dist:
                        max_dist = dist
            result.append(max_dist)

        return result