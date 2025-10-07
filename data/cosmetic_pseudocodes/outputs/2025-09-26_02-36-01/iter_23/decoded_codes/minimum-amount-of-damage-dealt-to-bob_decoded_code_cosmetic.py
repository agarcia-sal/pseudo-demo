from typing import List

class Enemy:
    def __init__(self, damage: int, timeTakenDown: int):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        def rdrps(arr: List[int]) -> int:
            def aux(idx: int, acc: int) -> int:
                if idx < 0:
                    return acc
                return aux(idx - 1, acc + arr[idx])
            return aux(len(arr) - 1, 0)

        sfdpx = rdrps(damage)

        def jhmqe(idx: int, out_list: List[Enemy]) -> List[Enemy]:
            if idx > len(damage) - 1:
                return out_list
            drlxb = damage[idx]
            txans = health[idx]
            dyewm = (txans + power - 1) // power
            wezvl = Enemy(drlxb, dyewm)
            out_list.append(wezvl)
            return jhmqe(idx + 1, out_list)

        bbyco = jhmqe(0, [])

        def cmpFn(e1: Enemy, e2: Enemy) -> int:
            # Compare by integer division of damage/timeTakenDown in descending order
            return (e2.damage // e2.timeTakenDown) - (e1.damage // e1.timeTakenDown)

        def quicksort(arr: List[Enemy]) -> List[Enemy]:
            def qsortRec(lst: List[Enemy]) -> List[Enemy]:
                if not lst:
                    return []
                pvt = lst[0]
                def partition(i: int, left: List[Enemy], right: List[Enemy]) -> (List[Enemy], List[Enemy]):
                    if i >= len(lst):
                        return left, right
                    el = lst[i]
                    if cmpFn(el, pvt) < 0:
                        left.append(el)
                    else:
                        right.append(el)
                    return partition(i + 1, left, right)
                lt, gt = partition(1, [], [])
                return qsortRec(lt) + [pvt] + qsortRec(gt)
            return qsortRec(arr)

        bbyco = quicksort(bbyco)

        def loop1(idx: int, accum_ans: int, accum_sum: int) -> int:
            if idx >= len(bbyco):
                return accum_ans
            curEnemy = bbyco[idx]
            new_ans = accum_ans + (accum_sum * curEnemy.timeTakenDown)
            new_sum = accum_sum - curEnemy.damage
            return loop1(idx + 1, new_ans, new_sum)

        qbrim = loop1(0, 0, sfdpx)

        return qbrim