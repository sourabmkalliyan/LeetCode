class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        minEnergy = min(enemyEnergies)

        if currentEnergy < minEnergy:
            return 0

        my_sum = 0
        for e in enemyEnergies:
            my_sum += e
        my_sum -= minEnergy
        my_sum += currentEnergy
        return my_sum // minEnergy
