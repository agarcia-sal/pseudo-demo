from typing import List

class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        def ConvertToBinary(number: int, length: int) -> str:
            binary_str = ""
            temp = number
            while temp > 0:
                binary_str = str(temp % 2) + binary_str
                temp //= 2
            while len(binary_str) < length:
                binary_str = "0" + binary_str
            return binary_str

        def hamming_distance(str_a: str, str_b: str) -> int:
            diff_count = 0
            for i in range(len(str_a)):
                if str_a[i] != str_b[i]:
                    diff_count += 1
            return diff_count

        binary_representations = [ConvertToBinary(num, m) for num in nums]
        results = []

        for current_index in range(len(nums)):
            max_distance = -1
            for compare_index in range(len(nums)):
                if current_index != compare_index:
                    distance = hamming_distance(binary_representations[current_index], binary_representations[compare_index])
                    if distance > max_distance:
                        max_distance = distance
            results.append(max_distance)

        return results