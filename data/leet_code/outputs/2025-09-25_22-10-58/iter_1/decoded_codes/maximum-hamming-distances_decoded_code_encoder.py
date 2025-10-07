class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        # Convert each number to a binary string of length m with leading zeros
        binary_nums = [format(num, f'0{m}b') for num in nums]

        def hamming_distance(bin1: str, bin2: str) -> int:
            # Calculate the number of differing bits between two binary strings
            return sum(ch1 != ch2 for ch1, ch2 in zip(bin1, bin2))

        answer = []
        n = len(nums)
        for i in range(n):
            max_dist = 0
            for j in range(n):
                if i != j:
                    dist = hamming_distance(binary_nums[i], binary_nums[j])
                    if dist > max_dist:
                        max_dist = dist
            answer.append(max_dist)

        return answer