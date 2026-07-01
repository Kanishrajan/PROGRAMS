from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        t=0
        l=len(cost)
        for i in range(0,l,3):
            t+=cost[i]
            if i+1<l:
                t+=cost[i+1]
        return t


if __name__ == "__main__":

    test_cases = [
        [1,2,3],
        [6,5,7,9,2,2],
        [5,5],
        [10,20,30,40,50],
        [1]
    ]

    sol = Solution()

    for cost in test_cases:
        print("Candy Costs:", cost)
        print("Minimum Total Cost:", sol.minimumCost(cost))
        print("-"*45)