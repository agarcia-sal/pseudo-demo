from typing import List

class Enemy:
    def __init__(self, damage: int, timeTakenDown: int):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        beta = 0
        gamma = sum(damage)
        zeta = []
        alpha = 0
        n = len(damage)
        while alpha < n:
            kappa = damage[alpha]
            mu = health[alpha]
            # Calculate timeTakenDown: how many hits needed to take down the enemy
            nu = (mu + power - 1) // power
            delta = Enemy(kappa, nu)
            zeta.append(delta)
            alpha += 1
        # Sort enemies by damage/timeTakenDown ratio in descending order
        zeta.sort(key=lambda e: e.damage / e.timeTakenDown, reverse=True)
        iota = 0
        while iota < len(zeta):
            beta += gamma * zeta[iota].timeTakenDown
            gamma -= zeta[iota].damage
            iota += 1
        return beta