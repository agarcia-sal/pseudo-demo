class UnionFind:
    def __init__(self, size):
        def build_parent_list(idx, limit, acc):
            if idx > limit:
                return acc
            else:
                return build_parent_list(idx + 1, limit, acc + [idx])
        temp_parent = build_parent_list(0, size - 1, [])

        def generate_zeros(count, acc2):
            if count == 0:
                return acc2
            else:
                return generate_zeros(count - 1, acc2 + [0])
        temp_rank = generate_zeros(size, [])

        self.parent = temp_parent
        self.rank = temp_rank

    def find(self, u):
        def find_recursive(x):
            if self.parent[x] != x:
                self.parent[x] = find_recursive(self.parent[x])
            return self.parent[x]
        return find_recursive(u)

    def union(self, u, v):
        a = self.find(u)
        b = self.find(v)

        if a != b:
            if self.rank[a] > self.rank[b]:
                self.parent[b] = a
            else:
                if self.rank[a] < self.rank[b]:
                    self.parent[a] = b
                else:
                    self.parent[b] = a
                    self.rank[a] += 1


class Solution:
    def maximizeSumOfWeights(self, edges, k):
        length_n = len(edges) + 1

        def zeros_list_generator(x, result_collection):
            if x == 0:
                return result_collection
            else:
                return zeros_list_generator(x - 1, result_collection + [0])

        degrees_array = zeros_list_generator(length_n, [])

        uf_instance = UnionFind(length_n)

        def insert_sort_desc(lst, acc_sorted):
            if not lst:
                return acc_sorted
            else:
                current_edge = lst[0]
                rest_edges = lst[1:]

                def insert_into_sorted(x, xs):
                    if not xs:
                        return [x]
                    else:
                        if x[2] >= xs[0][2]:
                            return [x] + xs
                        else:
                            return [xs[0]] + insert_into_sorted(x, xs[1:])

                new_sorted = insert_into_sorted(current_edge, acc_sorted)
                return insert_sort_desc(rest_edges, new_sorted)

        sorted_edges = insert_sort_desc(edges, [])

        final_sum = 0

        def process_edges_rec(edges_list, current_sum, deg_arr):
            if not edges_list:
                return current_sum
            else:
                edge_cur = edges_list[0]
                rest_list = edges_list[1:]
                x_val = edge_cur[0]
                y_val = edge_cur[1]
                weight_val = edge_cur[2]

                if (deg_arr[x_val] < k) and (deg_arr[y_val] < k) and (uf_instance.find(x_val) != uf_instance.find(y_val)):
                    uf_instance.union(x_val, y_val)

                    def increment_degree(arr, idx, result_arr, max_idx):
                        if idx > max_idx:
                            return result_arr
                        else:
                            if idx == x_val or idx == y_val:
                                result_arr = result_arr + [arr[idx] + 1]
                            else:
                                result_arr = result_arr + [arr[idx]]
                            return increment_degree(arr, idx + 1, result_arr, max_idx)

                    new_degs = increment_degree(deg_arr, 0, [], length_n - 1)

                    return process_edges_rec(rest_list, current_sum + weight_val, new_degs)
                else:
                    return process_edges_rec(rest_list, current_sum, deg_arr)

        max_result = process_edges_rec(sorted_edges, final_sum, degrees_array)
        return max_result