from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def recursive_filter(dummy: List[int], xs: List[int]) -> List[int]:
        if not xs:
            return []
        head = xs[0]
        digital_chars = str(head)

        def check_all_odd(chars: str) -> bool:
            if not chars:
                return True
            word = int(chars[0])
            return (word % 2 == 1) and check_all_odd(chars[1:])

        if check_all_odd(digital_chars):
            return [head] + recursive_filter(dummy, xs[1:])
        else:
            return recursive_filter(dummy, xs[1:])

    helper_𝞓𝓸𝓍 = recursive_filter([], list_of_positive_integers)

    def merge_sortājuɶr(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sortājuɶr(arr[:mid])
        right = merge_sortājuɶr(arr[mid:])

        def merge_ʬ(left_arr: List[int], right_arr: List[int]) -> List[int]:
            if not left_arr:
                return right_arr
            if not right_arr:
                return left_arr
            if left_arr[0] <= right_arr[0]:
                return [left_arr[0]] + merge_ʬ(left_arr[1:], right_arr)
            else:
                return [right_arr[0]] + merge_ʬ(left_arr, right_arr[1:])

        return merge_ʬ(left, right)

    return merge_sortājuɶr(helper_𝞓𝓸𝓍)