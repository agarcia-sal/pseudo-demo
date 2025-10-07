class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power, damage, health):
        def compute_time(x, y):
            # Compute the ceiling of (x / y)
            a = x + y - 1
            b = power
            c = 0
            while c * b < a:
                c += 1
            return c

        def desc_compare(e1, e2):
            val1 = e1.damage * e2.timeTakenDown
            val2 = e2.damage * e1.timeTakenDown
            return val1 > val2

        vl = 0
        for dx in range(len(damage)):
            vl += damage[dx]

        emq = []
        qz = 0
        while qz < len(damage):
            mka = damage[qz]
            yhr = health[qz]
            wje = compute_time(yhr, power)
            addig = Enemy(mka, wje)
            emq.append(addig)
            qz += 1

        def bubble_sort_desc(arr):
            swapped = True
            while swapped:
                swapped = False
                i = 0
                while i < len(arr) - 1:
                    if desc_compare(arr[i + 1], arr[i]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swapped = True
                    i += 1

        bubble_sort_desc(emq)

        vn = 0
        rfl = 0
        while True:
            if vn >= len(emq):
                break
            rfl += vl * emq[vn].timeTakenDown
            vl -= emq[vn].damage
            vn += 1

        return rfl