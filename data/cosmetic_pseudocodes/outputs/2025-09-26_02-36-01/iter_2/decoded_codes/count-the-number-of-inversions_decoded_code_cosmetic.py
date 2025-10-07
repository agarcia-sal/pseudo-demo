class Solution:
    def numberOfPermutations(self, size: int, conditions: list[tuple[int, int]]) -> int:
        modulus = 10**9 + 7
        condition_map = {}
        for end_pos, required_count in conditions:
            condition_map[end_pos] = required_count

        def count_permutations(current_length: int, inversion_total: int, bits_used: int) -> int:
            if current_length == size:
                expected_inversions = condition_map.get(size - 1, 0)
                return 1 if inversion_total == expected_inversions else 0

            if current_length > 0:
                expected_inversions = condition_map.get(current_length - 1, inversion_total)
                if inversion_total != expected_inversions:
                    return 0

            total_count = 0
            candidate = 0
            while candidate < size:
                if (bits_used & (1 << candidate)) == 0:
                    updated_inversions = inversion_total
                    checker = candidate + 1
                    while checker < size:
                        if (bits_used & (1 << checker)) != 0:
                            updated_inversions += 1
                        checker += 1
                    updated_bits = bits_used | (1 << candidate)
                    total_count = (total_count + count_permutations(current_length + 1, updated_inversions, updated_bits)) % modulus
                candidate += 1

            return total_count

        return count_permutations(0, 0, 0)