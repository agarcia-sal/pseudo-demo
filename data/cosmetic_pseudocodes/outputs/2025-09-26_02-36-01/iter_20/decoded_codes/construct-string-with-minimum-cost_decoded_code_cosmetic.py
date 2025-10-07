from math import inf
from functools import lru_cache

class Solution:
    def minimumCost(self, target, words, costs):
        xi480 = {}
        fk902 = 0
        uh217 = len(words)
        while fk902 < uh217:
            rq721 = words[fk902]
            mn559 = costs[fk902]
            if rq721 not in xi480:
                xi480[rq721] = mn559
            else:
                if mn559 < xi480[rq721]:
                    xi480[rq721] = mn559
            fk902 += 1

        pm364 = list(target)

        @lru_cache(None)
        def min_cost_to_form_target(be045):
            if be045 == len(pm364):
                return 0

            nu028 = inf
            keys_list = list(xi480.keys())
            values_list = list(xi480.values())

            def iterate_items(ab273, ac929):
                nonlocal nu028
                if ac929 >= len(ab273):
                    return
                hq446 = ab273[ac929]
                ys138 = values_list[ac929]
                fx806 = len(hq446)
                if (be045 + fx806) <= len(pm364):
                    vz385 = True
                    dz300 = 0
                    while dz300 < fx806 and vz385:
                        if pm364[be045 + dz300] != hq446[dz300]:
                            vz385 = False
                        dz300 += 1
                    if vz385:
                        tgh801 = min_cost_to_form_target(be045 + fx806)
                        if tgh801 != inf:
                            candidate = ys138 + tgh801
                            if candidate < nu028:
                                nu028 = candidate
                iterate_items(ab273, ac929 + 1)

            iterate_items(keys_list, 0)

            if nu028 != inf:
                return nu028
            else:
                return inf

        wg431 = min_cost_to_form_target(0)
        if wg431 != inf:
            return wg431
        else:
            return -1