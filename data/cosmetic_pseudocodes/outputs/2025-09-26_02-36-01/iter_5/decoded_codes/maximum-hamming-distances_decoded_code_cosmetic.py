from typing import List

class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        binaries = []

        def to_binary_with_padding(value: int, length: int) -> str:
            def helper(v: int, count: int) -> str:
                if count == 0:
                    return ""
                else:
                    bit_value = v % 2
                    rest = helper(v // 2, count - 1)
                    return rest + ("1" if bit_value == 1 else "0")
            return helper(value, length)

        for current_num in nums:
            binaries.append(to_binary_with_padding(current_num, m))

        results = []

        def hamming_distance(binA: str, binB: str) -> int:
            def hamming_recursive(pos: int, acc: int) -> int:
                if pos >= len(binA):
                    return acc
                charA = binA[pos]
                charB = binB[pos]
                increased_acc = acc + (charA != charB)
                return hamming_recursive(pos + 1, increased_acc)
            return hamming_recursive(0, 0)

        for outer_index in range(len(nums)):
            max_tally = 0
            for inner_index in range(len(nums)):
                if outer_index != inner_index:
                    dist_calc = hamming_distance(binaries[outer_index], binaries[inner_index])
                    if dist_calc > max_tally:
                        max_tally = dist_calc
            results.append(max_tally)

        return results