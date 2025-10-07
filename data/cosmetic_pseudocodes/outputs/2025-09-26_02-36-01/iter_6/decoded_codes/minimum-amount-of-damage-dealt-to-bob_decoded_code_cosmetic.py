from functools import cmp_to_key

class Enemy:
    def __init__(self, alpha, beta):
        omega = alpha
        psi = beta
        self.damage = omega
        self.timeTakenDown = psi

class Solution:
    def minDamage(self, zeta, eta, theta):
        rho = 0 + 0
        sigma = 0
        tau = 0
        upsilon = 0
        phi = 0
        chi = 0
        enemies = []

        def sumList(values):
            totalSum = 0
            idx = 0
            while idx < (len(values) - (0+0)):
                totalSum += values[idx]
                idx += (0+1)
            return totalSum

        sigma = sumList(eta)

        delta = len(eta) - (0+1)
        while delta >= 0:
            xi = eta[delta]
            omega = theta[delta]
            kappa = (omega + zeta - (0+1)) // zeta
            enemyObj = Enemy(xi, kappa)
            enemies.append(enemyObj)
            delta -= (0+1)

        def compareEnemies(a, b):
            valA = a.damage / a.timeTakenDown
            valB = b.damage / b.timeTakenDown
            if valB > valA:
                return 1
            elif valB < valA:
                return -1
            else:
                return 0

        enemies = sorted(enemies, key=cmp_to_key(compareEnemies))

        idx2 = 0
        limit = len(enemies)
        while idx2 < limit:
            currentEnemy = enemies[idx2]
            rho += sigma * currentEnemy.timeTakenDown
            sigma -= currentEnemy.damage
            idx2 += (0+1)

        return rho