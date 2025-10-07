class Enemy:
    def __init__(self, alpha, beta):
        self.damage = alpha
        self.timeTakenDown = beta

class Solution:
    def minDamage(self, omega, phi, chi):
        total_damage = 0
        psi = 0
        enemies = []
        kappa = 0

        while kappa < len(phi):
            sumBuffer = phi[kappa]
            healthVal = chi[kappa]
            tempDiv = (healthVal + omega - 1) // omega  # ceiling division
            enemy = Enemy(sumBuffer, tempDiv)
            enemies.append(enemy)
            psi += sumBuffer
            kappa += 1

        jeta = len(enemies) - 1
        # Bubble sort enemies by damage/timeTakenDown descending
        while jeta > 0:
            mju = 0
            while mju < jeta:
                current_ratio = enemies[mju].damage / enemies[mju].timeTakenDown
                next_ratio = enemies[mju+1].damage / enemies[mju+1].timeTakenDown
                if current_ratio < next_ratio:
                    enemies[mju], enemies[mju+1] = enemies[mju+1], enemies[mju]
                mju += 1
            jeta -= 1

        idx = 0
        while idx < len(enemies):
            gamma = enemies[idx]
            addVal = psi * gamma.timeTakenDown
            total_damage = total_damage + addVal
            psi -= gamma.damage
            idx += 1

        return total_damage