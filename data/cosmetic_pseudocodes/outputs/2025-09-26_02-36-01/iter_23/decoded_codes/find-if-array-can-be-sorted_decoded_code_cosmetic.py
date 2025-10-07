class Solution:
    def canSortArray(self, nums):
        def count_set_bits(x):
            def helper(val, res):
                if val == 0:
                    return res
                else:
                    return helper(val // 2, res + (val % 2))
            return helper(x, 0)

        length_var = len(nums)
        ordered_list = []
        for idx in range(length_var):
            ordered_list.append(nums[idx])

        def sort_copy(lst):
            def insert_sorted(array, elem):
                if len(array) == 0:
                    return [elem]
                else:
                    if elem <= array[0]:
                        return [elem] + array
                    else:
                        return [array[0]] + insert_sorted(array[1:], elem)

            def sort_recursive(array):
                if len(array) <= 1:
                    return array
                else:
                    head = array[0]
                    tail = array[1:]
                    sorted_tail = sort_recursive(tail)
                    return insert_sorted(sorted_tail, head)

            return sort_recursive(lst)

        target = sort_copy(ordered_list)

        def bubble_pass(a_list, u, v, swap_flag):
            if v > length_var - 2:
                return swap_flag
            else:
                curr_bits = count_set_bits(a_list[v])
                next_bits = count_set_bits(a_list[v + 1])

                if curr_bits == next_bits and a_list[v] > a_list[v + 1]:
                    a_list[v], a_list[v + 1] = a_list[v + 1], a_list[v]
                    return bubble_pass(a_list, u, v + 1, True)
                else:
                    return bubble_pass(a_list, u, v + 1, swap_flag)

        def bubble_outer(a_list, counter):
            if counter > length_var - 1:
                return
            else:
                changes = bubble_pass(a_list, counter, 0, False)
                if not changes:
                    return
                else:
                    bubble_outer(a_list, counter + 1)

        bubble_outer(nums, 0)

        equality_flag = True

        def compare_lists(lst1, lst2, pos):
            nonlocal equality_flag
            if pos >= length_var:
                return
            else:
                if lst1[pos] != lst2[pos]:
                    equality_flag = False
                    return
                else:
                    compare_lists(lst1, lst2, pos + 1)

        compare_lists(nums, target, 0)
        return equality_flag