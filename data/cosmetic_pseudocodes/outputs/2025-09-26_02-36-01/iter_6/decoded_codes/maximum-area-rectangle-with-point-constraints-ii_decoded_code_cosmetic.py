from typing import List

class Fenwick:
    def __init__(self, alpha: int):
        # Initialize Fenwick tree with zeros; size alpha+1 for 1-based indexing
        self.tree = [0] * (alpha + 1)

    def add(self, beta: int):
        gamma = beta
        while gamma < len(self.tree):
            self.tree[gamma] += 1
            delta = gamma & (-gamma)
            gamma += delta

    def pre(self, epsilon: int) -> int:
        zeta = 0
        eta = epsilon
        while eta > 0:
            zeta += self.tree[eta]
            theta = eta & (eta - 1)
            eta = theta
        return zeta

    def query(self, iota: int, kappa: int) -> int:
        lambdaVal = self.pre(kappa)
        mu = self.pre(iota - 1)
        return lambdaVal - mu


class Solution:
    def maxRectangleArea(self, omega: List[int], psi: List[int]) -> int:
        pairs = []
        nu = len(omega)

        def generate_pairs(xList: List[int], yList: List[int], idx: int):
            if idx >= nu:
                return
            pair = (xList[idx], yList[idx])
            pairs.append(pair)
            generate_pairs(xList, yList, idx + 1)

        generate_pairs(omega, psi, 0)

        def sort_pairs(arr: List[tuple]) -> None:
            # Bubble sort as per pseudocode, sorting by first element ascending,
            # and second element ascending if first elements equal.
            n = len(arr)
            while True:
                swapped = 0
                for a in range(1, n):
                    if (arr[a - 1][0] > arr[a][0] or
                        (arr[a - 1][0] == arr[a][0] and arr[a - 1][1] > arr[a][1])):
                        arr[a - 1], arr[a] = arr[a], arr[a - 1]
                        swapped = 1
                n -= 1
                if swapped == 0:
                    break

        sort_pairs(pairs)

        ys_set = {}
        for xval in psi:
            ys_set[xval] = True

        ys_list = []
        for key in ys_set:
            ys_list.append(key)

        def sort_ys(arr: List[int]) -> List[int]:
            if len(arr) < 2:
                return arr
            pivot = arr[0]
            left = []
            right = []
            for q in range(1, len(arr)):
                if arr[q] < pivot:
                    left.append(arr[q])
                else:
                    right.append(arr[q])
            return sort_ys(left) + [pivot] + sort_ys(right)

        ys_list = sort_ys(ys_list)

        answer = -1
        fen = Fenwick(len(ys_list))

        def bisect_left(arr: List[int], val: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] >= val:
                    high = mid
                else:
                    low = mid + 1
            return low

        start_index = bisect_left(ys_list, pairs[0][1]) + 1
        fen.add(start_index)

        dictionary = {}

        def process_pairs(index: int):
            if index >= len(pairs) - 1:
                return
            current = pairs[index]
            next_one = pairs[index + 1]

            y_index = bisect_left(ys_list, next_one[1]) + 1
            fen.add(y_index)

            if current[0] != next_one[0]:
                process_pairs(index + 1)
                return

            cur_val = fen.query(bisect_left(ys_list, current[1]) + 1, y_index)

            if next_one[1] in dictionary:
                stored_tuple = dictionary[next_one[1]]
                if (stored_tuple[1] == current[1] and stored_tuple[2] + 2 == cur_val):
                    length_x = next_one[0] - stored_tuple[0]
                    length_y = next_one[1] - current[1]
                    pro = length_x * length_y
                    nonlocal answer
                    if pro > answer:
                        answer = pro

            dictionary[next_one[1]] = (current[0], current[1], cur_val)
            process_pairs(index + 1)

        process_pairs(0)

        return answer