class Solution:
    def maxPotholes(self, inputRoad: str, budget: int) -> int:
        def countLength(s: str) -> int:
            count_acc = 0
            index_cursor = 0
            while True:
                if index_cursor == len(s):
                    break
                count_acc += 1
                index_cursor += 1
            return count_acc

        def splitByDot(text: str) -> list[str]:
            result_list = []
            start_pos = 0
            i_pos = 0
            while True:
                if i_pos == len(text):
                    result_list.append(text[start_pos:i_pos])
                    break
                if text[i_pos] == '.':
                    result_list.append(text[start_pos:i_pos])
                    start_pos = i_pos + 1
                i_pos += 1
            return result_list

        def ascendingLengthSort(lst: list[str]) -> list[str]:
            def lengthOfString(x: str) -> int:
                return countLength(x)

            sorted_list = lst[:]
            swapped_flag = True
            while swapped_flag:
                swapped_flag = False
                idx = 0
                while idx < len(sorted_list) - 1:
                    if lengthOfString(sorted_list[idx]) > lengthOfString(sorted_list[idx + 1]):
                        sorted_list[idx], sorted_list[idx + 1] = sorted_list[idx + 1], sorted_list[idx]
                        swapped_flag = True
                    idx += 1
            return sorted_list

        pieces = splitByDot(inputRoad)
        ordered_segments = ascendingLengthSort(pieces)
        total_fixed = 0
        current_budget = budget

        def attemptFix(segment_str: str, available_budget: int) -> tuple[int, int]:
            segment_len = countLength(segment_str)
            fixed_count = 0
            length_remaining = segment_len

            while True:
                total_needed = length_remaining + 1
                if available_budget >= total_needed:
                    fixed_count = length_remaining
                    available_budget -= total_needed
                    break
                length_remaining -= 1
                if length_remaining == 0 or available_budget == 0:
                    break
            return fixed_count, available_budget

        for segment_var in ordered_segments:
            len_s = countLength(segment_var)
            if len_s == 0:
                continue
            cost_required = len_s + 1
            if cost_required <= current_budget:
                total_fixed += len_s
                current_budget -= cost_required
            else:
                fixed_part, new_budget = attemptFix(segment_var, current_budget)
                total_fixed += fixed_part
                current_budget = new_budget

        return total_fixed