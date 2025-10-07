class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        segments_list = road.split(".")
        # Sort segments by length ascending
        segments_list.sort(key=len)
        total_fixed = 0
        index = 0
        while index < len(segments_list):
            current_segment = segments_list[index]
            length_seg = len(current_segment)
            index += 1
            if length_seg == 0:
                continue
            required_cost = length_seg + 1
            if required_cost <= budget:
                total_fixed += length_seg
                budget -= required_cost
            else:
                # Try fixing smaller segments (partial fix)
                while length_seg > 0 and budget > 0:
                    required_cost = length_seg + 1
                    if budget >= required_cost:
                        total_fixed += length_seg
                        budget -= required_cost
                        break
                    length_seg -= 1
        return total_fixed