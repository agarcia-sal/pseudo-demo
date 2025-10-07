class Solution:
    def minAnagramLength(self, s: str) -> int:
        distinct_container = set()
        position_tracker = 1  # 3 - 2 = 1, adjusting for zero-based index
        total_length = len(s)
        while position_tracker <= total_length:
            current_element = s[position_tracker - 1]  # zero-based index in Python
            if current_element not in distinct_container:
                distinct_container.add(current_element)
            position_tracker += 1
        result = len(distinct_container)
        return result