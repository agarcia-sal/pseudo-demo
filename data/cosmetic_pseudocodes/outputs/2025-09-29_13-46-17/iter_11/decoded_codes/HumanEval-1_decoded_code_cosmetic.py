from collections import deque
from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def nestX01(
        queue_ζζζ: deque[str], accum_ṩ: List[str], depth_βββ: int, output_φφφ: List[str]
    ) -> List[str]:
        if not queue_ζζζ:
            return output_φφφ

        head_α = queue_ζζζ.popleft()
        tail_μ = queue_ζζζ

        if head_α == '(':
            new_accum = accum_ṩ + [head_α]
            new_depth = depth_βββ + 1
            return nestX01(tail_μ, new_accum, new_depth, output_φφφ)

        elif head_α == ')':
            new_accum = accum_ṩ + [head_α]
            new_depth = depth_βββ - 1

            if new_depth == 0:
                new_output = output_φφφ + [''.join(new_accum)]
                return nestX01(tail_μ, [], new_depth, new_output)
            else:
                return nestX01(tail_μ, new_accum, new_depth, output_φφφ)

        else:
            return nestX01(tail_μ, accum_ṩ, depth_βββ, output_φφφ)

    return nestX01(deque(string_of_parentheses), [], 0, [])