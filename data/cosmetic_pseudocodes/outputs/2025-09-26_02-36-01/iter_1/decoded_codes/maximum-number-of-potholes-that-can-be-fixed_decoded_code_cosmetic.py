class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        segments = sorted(road.split('.'), key=len)
        total_fixed = 0
        for segment in segments:
            length_seg = len(segment)
            if length_seg == 0:
                continue
            required_cost = length_seg + 1
            if required_cost <= budget:
                total_fixed += length_seg
                budget -= required_cost
            else:
                while length_seg > 0 and budget > 0:
                    required_cost = length_seg + 1
                    if budget >= required_cost:
                        total_fixed += length_seg
                        budget -= required_cost
                        break
                    length_seg -= 1
        return total_fixed