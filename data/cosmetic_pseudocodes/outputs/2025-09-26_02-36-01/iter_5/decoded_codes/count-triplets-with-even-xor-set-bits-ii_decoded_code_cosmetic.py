class Solution:
    def tripletCount(self, a: list[int], b: list[int], c: list[int]) -> int:
        def count_even_odd_bits(arr: list[int]) -> tuple[int, int]:
            def count_one_bits_recursive(index: int, acc: int) -> int:
                if index < 0:
                    return acc
                shifted_value = arr[index] // 2
                bit_value = arr[index] - shifted_value * 2
                return count_one_bits_recursive(index - 1, acc + bit_value)

            def count_bits_in_number(num: int) -> int:
                if num == 0:
                    return 0
                return (num % 2) + count_bits_in_number(num // 2)

            def helper_loop(pos: int, evens_acc: int) -> int:
                if pos >= len(arr):
                    return evens_acc
                def count_bits_iter(n: int, cnt: int) -> int:
                    if n == 0:
                        return cnt
                    return count_bits_iter(n // 2, cnt + (n % 2))
                ones_count = count_bits_iter(arr[pos], 0)
                new_evens = evens_acc + 1 if (ones_count % 2) == 0 else evens_acc
                return helper_loop(pos + 1, new_evens)

            total_even = helper_loop(0, 0)
            total_odd = len(arr) - total_even
            return total_even, total_odd

        e_a, o_a = count_even_odd_bits(a)
        e_b, o_b = count_even_odd_bits(b)
        e_c, o_c = count_even_odd_bits(c)

        part1 = e_a * e_b * e_c
        part2 = (e_a * o_b * o_c) + (o_a * e_b * o_c) + (o_a * o_b * e_c)

        final_answer = part1 + part2
        return final_answer