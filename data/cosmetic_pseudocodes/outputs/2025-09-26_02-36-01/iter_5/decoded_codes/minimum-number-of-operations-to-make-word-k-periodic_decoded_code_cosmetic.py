class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, argument_k: int) -> int:
        def countOccurrences(list_ref, key_value):
            if not list_ref:
                return 0
            head_element = list_ref[0]
            tail_list = list_ref[1:]
            if head_element == key_value:
                return 1 + countOccurrences(tail_list, key_value)
            else:
                return countOccurrences(tail_list, key_value)

        length_word = len(word) - 1

        def collectSegments(current_pos, accum_segments):
            if current_pos > length_word:
                return accum_segments
            segment_slice = word[current_pos:current_pos + argument_k]
            return collectSegments(current_pos + argument_k, accum_segments + [segment_slice])

        collected_segments = collectSegments(0, [])

        def appendIfNew(item, seen):
            if item in seen:
                return seen
            return seen + [item]

        unique_segments = []
        for segment in collected_segments:
            unique_segments = appendIfNew(segment, unique_segments)

        def maxCountHelper(items, keys, current_max):
            if not keys:
                return current_max
            current_key = keys[0]
            rest_keys = keys[1:]
            current_frequency = countOccurrences(items, current_key)
            updated_max = current_max
            if current_frequency > current_max:
                updated_max = current_frequency
            return maxCountHelper(items, rest_keys, updated_max)

        max_frequency = maxCountHelper(collected_segments, unique_segments, 0)

        final_result = len(collected_segments) - max_frequency
        return final_result