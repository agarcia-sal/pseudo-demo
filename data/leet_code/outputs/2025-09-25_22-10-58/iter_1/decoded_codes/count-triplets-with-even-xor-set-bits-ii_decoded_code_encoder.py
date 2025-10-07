class Solution:
    def tripletCount(self, a: list[int], b: list[int], c: list[int]) -> int:
        def count_even_odd_bits(arr: list[int]) -> tuple[int, int]:
            even_count = 0
            for num in arr:
                # Count number of one bits using built-in bit_count (Python 3.10+)
                if num.bit_count() % 2 == 0:
                    even_count += 1
            odd_count = len(arr) - even_count
            return even_count, odd_count

        even_a, odd_a = count_even_odd_bits(a)
        even_b, odd_b = count_even_odd_bits(b)
        even_c, odd_c = count_even_odd_bits(c)

        case1 = even_a * even_b * even_c
        case2 = even_a * odd_b * odd_c + odd_a * even_b * odd_c + odd_a * odd_b * even_c

        result = case1 + case2
        return result