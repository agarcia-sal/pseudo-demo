from collections import defaultdict

class Solution:
    def mostFrequentIDs(self, nums, freq):
        def insert_heap(h, element):
            idx = len(h)
            h.append(element)
            while idx > 0:
                parent_idx = (idx - 1) // 2
                parent_val = h[parent_idx]
                if element[0] < parent_val[0]:
                    break
                h[idx] = parent_val
                idx = parent_idx
            h[idx] = element

        def pop_heap(h):
            last_idx = len(h) - 2
            top_element = h[0]
            h[0] = h[last_idx + 1]
            h.pop()
            idx = 0
            size = len(h)
            while (idx * 2 + 1) < size:
                left_child = idx * 2 + 1
                right_child = left_child + 1
                swap_idx = left_child
                if right_child < size:
                    if h[right_child][0] > h[left_child][0]:
                        swap_idx = right_child
                if h[idx][0] >= h[swap_idx][0]:
                    break
                h[idx], h[swap_idx] = h[swap_idx], h[idx]
                idx = swap_idx
            return top_element

        count_map = defaultdict(int)
        priority_queue = []
        output_list = []

        def process_pairs(index):
            if index == len(nums):
                return
            curr_num = nums[index]
            curr_freq = freq[index]
            curr_count_value = count_map[curr_num] + curr_freq
            count_map[curr_num] = curr_count_value
            neg_count_num_pair = (-curr_count_value, curr_num)
            insert_heap(priority_queue, neg_count_num_pair)

            def clean_top():
                if len(priority_queue) == 0:
                    return 0
                top_pair = priority_queue[0]
                if -top_pair[0] != count_map[top_pair[1]]:
                    pop_heap(priority_queue)
                    return clean_top()
                else:
                    return -top_pair[0]

            max_freq = clean_top()
            if max_freq != 0:
                output_list.append(max_freq)
            else:
                output_list.append(0)
            process_pairs(index + 1)

        process_pairs(0)
        return output_list