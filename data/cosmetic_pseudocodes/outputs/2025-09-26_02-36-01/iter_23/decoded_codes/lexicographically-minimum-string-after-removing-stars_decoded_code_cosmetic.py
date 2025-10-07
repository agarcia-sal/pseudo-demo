class Solution:
    def clearStars(self, s: str) -> str:
        def aux(tracker, idx, limit):
            if not (idx < limit):
                return tracker
            val = s[idx]
            if val == "*":
                if len(tracker) > 0:
                    tracker = tracker[:-1]
            else:
                tracker.append(val)
            return aux(tracker, idx + 1, limit)

        acc = aux([], 0, len(s))
        return "".join(acc)