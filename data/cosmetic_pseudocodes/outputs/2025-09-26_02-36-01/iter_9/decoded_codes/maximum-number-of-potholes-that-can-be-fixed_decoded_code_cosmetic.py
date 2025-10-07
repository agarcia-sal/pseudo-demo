class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:

        def splitByDot(input_str: str) -> list[str]:
            result = []
            current = ""
            idx = 0
            while idx < len(input_str):
                if input_str[idx] == '.':
                    result.append(current)
                    current = ""
                else:
                    current += input_str[idx]
                idx += 1
            result.append(current)
            return result

        def sortByLengthAscending(segs: list[str]) -> list[str]:
            sorted_segs = segs[:]
            changeMade = True
            while changeMade:
                changeMade = False
                for i in range(len(sorted_segs)-1):
                    if len(sorted_segs[i]) > len(sorted_segs[i+1]):
                        sorted_segs[i], sorted_segs[i+1] = sorted_segs[i+1], sorted_segs[i]
                        changeMade = True
            return sorted_segs

        segments = splitByDot(road)
        ordered_segments = sortByLengthAscending(segments)
        accum_fixed = 0
        seg_idx = 0

        while seg_idx < len(ordered_segments):
            curr_seg = ordered_segments[seg_idx]
            length_seg = len(curr_seg)

            if length_seg != 0:
                expense = length_seg + 1
                if budget >= expense:
                    accum_fixed += length_seg
                    budget -= expense
                else:
                    temp_len = length_seg
                    while temp_len > 0 and budget > 0:
                        current_cost = temp_len + 1
                        if budget >= current_cost:
                            accum_fixed += temp_len
                            budget -= current_cost
                            break
                        else:
                            temp_len -= 1
            seg_idx += 1

        return accum_fixed