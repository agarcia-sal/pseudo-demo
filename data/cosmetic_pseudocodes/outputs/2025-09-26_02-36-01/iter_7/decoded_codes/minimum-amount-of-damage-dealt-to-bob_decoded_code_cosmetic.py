from functools import cmp_to_key


class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown


class Solution:
    def minDamage(self, power, damage, health):
        resultAccumulator = 0
        aggregateDamage = 0
        intermediateEnemies = []

        for d in damage:
            aggregateDamage += d

        for dmg, hp in zip(damage, health):
            segmentsRequired = (hp + power - 1) // power  # ceil division for attacks needed
            tempEnemy = Enemy(dmg, segmentsRequired)
            intermediateEnemies.append(tempEnemy)

        # Sort enemies by damage/timeTakenDown ratio in descending order:
        # Using a comparator that compares (enemy.damage / enemy.timeTakenDown)
        # so that enemies with higher damage per timeTakenDown come first.
        def compare_enemies(a, b):
            # Returns -1 if a should come before b, 1 if after, 0 if equal.
            # Compare a.damage * b.timeTakenDown and b.damage * a.timeTakenDown to avoid float division.
            val1 = a.damage * b.timeTakenDown
            val2 = b.damage * a.timeTakenDown
            if val1 > val2:
                return -1
            elif val1 < val2:
                return 1
            else:
                return 0

        intermediateEnemies.sort(key=cmp_to_key(compare_enemies))

        countdown = 0
        while countdown < len(intermediateEnemies):
            currentEnemy = intermediateEnemies[countdown]
            resultAccumulator += aggregateDamage * currentEnemy.timeTakenDown
            aggregateDamage -= currentEnemy.damage
            countdown += 1

        return resultAccumulator