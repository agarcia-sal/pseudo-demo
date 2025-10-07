class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        pothole_segments = road.split('.')
        pothole_segments.sort(key=len)
        fixed_potholes = 0
        for segment in pothole_segments:
            n = len(segment)
            if n == 0:
                continue
            cost = n + 1
            if cost <= budget:
                fixed_potholes += n
                budget -= cost
            else:
                while n > 0 and budget > 0:
                    cost = n + 1
                    if budget >= cost:
                        fixed_potholes += n
                        budget -= cost
                        break
                    n -= 1
        return fixed_potholes