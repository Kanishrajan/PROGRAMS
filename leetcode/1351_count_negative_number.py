from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for i in grid:
            for j in i:
                if j < 0:
                    c += 1
        return c


if __name__ == "__main__":

    test_cases = [
        [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
        [[3,2],[1,0]],
        [[1,-1],[-1,-1]],
        [[-1]],
        [[5,4,3,2]]
    ]

    sol = Solution()

    for grid in test_cases:
        print("Grid:")
        for row in grid:
            print(row)

        print("Negative Count:", sol.countNegatives(grid))
        print("-" * 45)
