from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def parityBitStats(xs: List[int]) -> Tuple[int, int]:
            even_parity_count = 0
            for val in xs:
                # Count bits set to 1 in val
                bit_count = 0
                tmp_val = val
                while tmp_val > 0:
                    bit_count += tmp_val & 1
                    tmp_val >>= 1
                if (bit_count & 1) == 0:
                    even_parity_count += 1
            odd_parity_count = len(xs) - even_parity_count
            return even_parity_count, odd_parity_count

        lchtj, jeomf = parityBitStats(a)
        vpsqro, dugxmt = parityBitStats(b)
        pwnaje, rzposb = parityBitStats(c)

        def mul(x: int, y: int) -> int:
            return x * y

        def add(x: int, y: int) -> int:
            return x + y

        part1 = mul(mul(lchtj, vpsqro), pwnaje)
        part2 = add(
            add(mul(mul(lchtj, dugxmt), rzposb), mul(mul(jeomf, vpsqro), rzposb)),
            mul(mul(jeomf, dugxmt), pwnaje)
        )

        output_val = add(part1, part2)
        return output_val