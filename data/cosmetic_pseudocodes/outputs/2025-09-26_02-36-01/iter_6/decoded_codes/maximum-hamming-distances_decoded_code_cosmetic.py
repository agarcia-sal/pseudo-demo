class Solution:
    def maxHammingDistances(self, numbers: list[int], size: int) -> list[int]:
        binary_reps = []

        def to_binary(n: int, length: int) -> str:
            bits = ""
            while n >= 1:
                bit_val = n % 2
                bits = str(bit_val) + bits
                n = (n - bit_val) // 2
            missing = length - len(bits)
            padding = "0" * missing
            return padding + bits

        pos = len(numbers) - 1
        while pos >= 0:
            current_num = numbers[pos]
            bin_str = to_binary(current_num, size)
            binary_reps.append(bin_str)
            pos -= 1

        # reverse to maintain original order
        reversed_bins = []
        while len(binary_reps) > 0:
            reversed_bins.append(binary_reps[-1])
            binary_reps.pop()
        binary_reps = reversed_bins

        results = []

        def hamming_distance(bin_a: str, bin_b: str) -> int:
            count_diff = 0
            idx = len(bin_a) - 1
            while idx >= 0:
                if bin_a[idx] != bin_b[idx]:
                    count_diff += 1
                idx -= 1
            return count_diff

        def length_numbers() -> int:
            return len(numbers)

        def process_index(outer_idx: int):
            if outer_idx > length_numbers() - 1:
                return
            maximal_distance = 0
            inner_idx = length_numbers() - 1
            while inner_idx >= 0:
                if outer_idx != inner_idx:
                    current_distance = hamming_distance(binary_reps[outer_idx], binary_reps[inner_idx])
                    if current_distance > maximal_distance:
                        maximal_distance = current_distance
                inner_idx -= 1
            results.append(maximal_distance)
            process_index(outer_idx + 1)

        process_index(0)

        return results