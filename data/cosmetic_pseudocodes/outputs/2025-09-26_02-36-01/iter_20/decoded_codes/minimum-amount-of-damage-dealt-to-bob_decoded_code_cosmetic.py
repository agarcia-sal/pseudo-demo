from typing import List

class Enemy:
    def __init__(self, damage: int, timeTakenDown: int):
        self.damage = damage
        self.timeTakenDown = timeTakenDown


class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        def divide_floor(x: int, y: int) -> int:
            # Floor division equivalent
            return (x - (x % y)) // y

        def sum_list(lst: List[int]) -> int:
            total = 0
            i = 0
            while i < len(lst):
                total += lst[i]
                i += 1
            return total

        def cmp_enemy_ratio(e1: Enemy, e2: Enemy) -> int:
            def ratio(enemy: Enemy) -> float:
                return enemy.damage / enemy.timeTakenDown
            r1 = ratio(e1)
            r2 = ratio(e2)
            if r1 < r2:
                return 1
            elif r1 > r2:
                return -1
            else:
                return 0

        zxfw = 0
        fhtq = sum_list(damage)
        rnpu: List[Enemy] = []

        def createEnemy(dmg: int, ttd: int) -> Enemy:
            return Enemy(dmg, ttd)

        kqxv = 0
        while kqxv < len(damage):
            mdvja = damage[kqxv]
            xkpab = health[kqxv]
            arto = divide_floor(xkpab + power - 1, power)
            pgbq = createEnemy(mdvja, arto)
            rnpu.append(pgbq)
            kqxv += 1

        def quicksort(arr: List[Enemy], left: int, right: int) -> None:
            if left >= right:
                return
            pivot = arr[right]
            i = left - 1
            j = left
            while j < right:
                if cmp_enemy_ratio(arr[j], pivot) <= 0:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                j += 1
            arr[i + 1], arr[right] = arr[right], arr[i + 1]
            quicksort(arr, left, i)
            quicksort(arr, i + 2, right)

        quicksort(rnpu, 0, len(rnpu) - 1)

        utzgpc = 0  # unused in original code but preserved

        def add_mul(a: int, b: int) -> int:
            return a * b

        def inc_ans(ans_ref: List[int], val: int) -> None:
            ans_ref[0] += val

        ans_wrapper = [zxfw]

        def process_enemies(lst: List[Enemy]) -> None:
            nonlocal fhtq
            if len(lst) == 0:
                return
            first_enemy = lst[0]
            inc_ans(ans_wrapper, add_mul(fhtq, first_enemy.timeTakenDown))
            fhtq -= first_enemy.damage
            process_enemies(lst[1:])

        process_enemies(rnpu)

        return ans_wrapper[0]