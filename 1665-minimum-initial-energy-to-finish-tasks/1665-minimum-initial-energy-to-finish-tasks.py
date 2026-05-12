class Solution:
    def minimumEffort(self, tasks):
        # Sort by (minimum - actual) in descending order
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:
            # Increase initial energy if current energy is insufficient
            if current < minimum:
                energy += (minimum - current)
                current = minimum

            # Finish task
            current -= actual

        return energy