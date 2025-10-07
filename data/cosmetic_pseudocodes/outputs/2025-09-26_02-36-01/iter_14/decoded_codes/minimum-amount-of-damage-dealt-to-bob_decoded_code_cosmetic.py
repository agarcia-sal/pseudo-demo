from functools import cmp_to_key

class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power, damage, health):
        omega = 0
        theta = sum(damage)
        lambda_list = []
        kappa = 0
        n = len(damage)
        while kappa < n:
            rho = damage[kappa]
            sigma = health[kappa]
            tau = (sigma + power - 1) // power
            enemy_tmp = Enemy(rho, tau)
            lambda_list.append(enemy_tmp)
            kappa += 1

        def comparator(x, y):
            lhs = x.damage * y.timeTakenDown
            rhs = y.damage * x.timeTakenDown
            if lhs > rhs:
                return -1
            elif lhs < rhs:
                return 1
            else:
                return 0

        lambda_list.sort(key=cmp_to_key(comparator))
        xi = 0
        while True:
            if xi >= len(lambda_list):
                break
            eta = lambda_list[xi]
            omega += theta * eta.timeTakenDown
            theta -= eta.damage
            xi += 1
        return omega