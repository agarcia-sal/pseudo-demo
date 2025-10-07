class Solution:
    def shortestSubstrings(self, arr):
        _dict_counter = {}

        def _init_counter():
            _idx_a = 0

            def _add_substrings(str_p, len_p):
                def _loop_j(i_p, j_p):
                    if j_p < len_p + 1:
                        _sub_p = str_p[i_p:j_p]
                        _dict_counter[_sub_p] = _dict_counter.get(_sub_p, 0) + 1
                        _loop_j(i_p, j_p + 1)
                    else:
                        return

                nonlocal _idx_a
                if _idx_a < len_p:
                    _loop_j(_idx_a, _idx_a + 1)
                    _idx_a += 1
                    _add_substrings(str_p, len_p)
                else:
                    return

            for s in arr:
                _dict_counter.clear()
                _add_substrings(s, len(s))

        _init_counter()

        answer = []

        def _find_shortest_unique(sq):
            len_sq = len(sq)
            ret_val = ""

            def _walker_i(i_i):
                def _walker_j(j_j):
                    nonlocal ret_val
                    if j_j <= len_sq:
                        subs_i_j = sq[i_i:j_j]
                        if _dict_counter.get(subs_i_j, 0) == 1:
                            if (ret_val == "") or (len(subs_i_j) < len(ret_val)) or (
                                len(subs_i_j) == len(ret_val) and subs_i_j < ret_val
                            ):
                                ret_val = subs_i_j
                        _walker_j(j_j + 1)
                    else:
                        return

                if i_i < len_sq:
                    _walker_j(i_i + 1)
                    _walker_i(i_i + 1)
                else:
                    return

            _walker_i(0)
            return ret_val

        for _curr_str in arr:
            res_substr = _find_shortest_unique(_curr_str)
            answer.append(res_substr)

        return answer