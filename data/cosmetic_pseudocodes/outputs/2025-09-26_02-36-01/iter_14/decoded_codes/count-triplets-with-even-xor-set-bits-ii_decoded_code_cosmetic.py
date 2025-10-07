class Solution:
    def tripletCount(self, a: list[int], b: list[int], c: list[int]) -> int:
        def count_even_odd_bits(arr: list[int]) -> tuple[int, int]:
            even_counter = 0
            for num in arr:
                bit_sum = 0
                bit_pos = 0
                # Count bits in integer (assume standard 4-byte int = 32 bits)
                while bit_pos < 8 * 4:
                    if num & (1 << bit_pos):
                        bit_sum += 1
                    bit_pos += 1
                if (bit_sum & 1) == 0:
                    even_counter += 1
            odd_counter = len(arr) - even_counter
            return even_counter, odd_counter

        m, n = count_even_odd_bits(a)
        p, q = count_even_odd_bits(b)
        r, s = count_even_odd_bits(c)

        tmp1 = m * p * r
        tmp2 = (m * q * s) + (n * p * s) + (n * q * r)

        total = tmp1 + tmp2

        return total