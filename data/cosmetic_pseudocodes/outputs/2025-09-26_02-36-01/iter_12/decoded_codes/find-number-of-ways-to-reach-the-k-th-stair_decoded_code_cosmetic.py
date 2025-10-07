class Solution:
    def waysToReachStair(self, k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def explorePosition(current_step: int, toggle: int, last_jump: int) -> int:
            if current_step > k + 1:
                return 0

            result = 1 if current_step == k else 0

            if current_step > 0:
                if toggle == 0:
                    result += explorePosition(current_step - 1, 1, last_jump)

            next_jump = last_jump + 1
            forward_step = current_step + 2 * last_jump
            result += explorePosition(forward_step, 0, next_jump)

            return result

        return explorePosition(1, 0, 0)