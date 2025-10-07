class Solution:
    def mostFrequentIDs(self, nums, freq):
        # Helper functions for length and empty check to exactly match pseudocode behavior
        def length(collection):
            count = 0
            for _ in collection:
                count += 1
            return count

        def is_empty(collection):
            return length(collection) == 0

        # Priority queue operations for min-heap by first element of tuple
        def function_push(queue, element):
            queue.append(element)
            def sift_up():
                pos = length(queue) - 1
                while pos > 0:
                    parent = (pos - 1) // 2
                    if queue[parent][0] > queue[pos][0]:
                        queue[parent], queue[pos] = queue[pos], queue[parent]
                        pos = parent
                    else:
                        break
            sift_up()

        def function_pop(queue):
            if length(queue) == 0:
                return
            queue[0] = queue[-1]
            queue.pop()
            def sift_down():
                pos = 0
                len_q = length(queue)
                while True:
                    left = pos * 2 + 1
                    right = pos * 2 + 2
                    smallest = pos
                    if left < len_q and queue[left][0] < queue[smallest][0]:
                        smallest = left
                    if right < len_q and queue[right][0] < queue[smallest][0]:
                        smallest = right
                    if smallest == pos:
                        break
                    queue[smallest], queue[pos] = queue[pos], queue[smallest]
                    pos = smallest
            sift_down()

        # create_dictionary_with_default returns an empty dict, relying on manual get/set
        def create_dictionary_with_default(default_provider):
            # Since Python dict does not auto fill default, handle default in get/set
            return {}

        tally = create_dictionary_with_default(lambda: 0)
        priority_queue = []
        output_list = []

        index_counter = 0
        while True:
            if index_counter >= length(nums):
                break

            value_current = nums[index_counter]
            frequency_current = freq[index_counter]

            prior_count = tally.get(value_current, 0)
            updated_count = prior_count + frequency_current
            tally[value_current] = updated_count

            entry_pair = (-updated_count, value_current)
            function_push(priority_queue, entry_pair)

            while (not is_empty(priority_queue)
                   and (-priority_queue[0][0]) != tally[priority_queue[0][1]]):
                function_pop(priority_queue)

            if not is_empty(priority_queue):
                top_frequency = -priority_queue[0][0]
                output_list.append(top_frequency)
            else:
                output_list.append(0)

            index_counter += 1

        return output_list