from typing import List, Tuple

class Solution:
    def countDays(self, days: int, meetings: List[Tuple[int, int]]) -> int:
        def reorder(lst: List[Tuple[int, int]]) -> None:
            i = 1
            while i < len(lst):
                j = i
                while j > 0 and lst[j - 1][0] > lst[j][0]:
                    lst[j - 1], lst[j] = lst[j], lst[j - 1]
                    j -= 1
                i += 1

        reorder(meetings)

        alpha = 1
        beta = 0

        for item in meetings:
            omega, psi = item

            if not (alpha >= omega):
                increment = omega - alpha
                beta += increment

            if psi + 1 > alpha:
                alpha = psi + 1

        if alpha <= days:
            gamma = days - alpha + 1
            beta += gamma

        return beta