class Solution:
    def find_successors(self, hand, groupSize, i, n):
        next_val = hand[i] + 1
        hand[i] = -1
        count = 1
        i += 1
        while i < n and count < groupSize:
            if hand[i] == next_val:
                next_val = hand[i] + 1
                hand[i] = -1
                count += 1

            i += 1

        return count == groupSize

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if (n % groupSize) != 0:
            return False

        hand.sort()
        for i in range(len(hand)):
            if hand[i] >= 0:
                if not self.find_successors(hand, groupSize, i, n):
                    return False

        return True


# Time Complexity: O(n log n + n / groupSize)
# Space Complexity: O(1)
