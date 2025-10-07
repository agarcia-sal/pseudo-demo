class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        def sortMeetingsAscending(lst: list[list[int]]) -> None:
            p = 0
            while p < len(lst) - 1:
                q = p + 1
                while q < len(lst):
                    if not (lst[p][0] <= lst[q][0]):
                        lst[p], lst[q] = lst[q], lst[p]
                    q += 1
                p += 1

        sortMeetingsAscending(meetings)

        alpha = 1
        beta = 0
        idx = 0

        while idx < len(meetings):
            mu, nu = meetings[idx]

            if alpha < mu:
                beta += mu - alpha

            max_day = alpha
            if nu > max_day:
                max_day = nu
            alpha = max_day + 1

            idx += 1

        if alpha <= days:
            beta += (days - alpha) + 1

        return beta