from typing import List

class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:
        return k * max(A) - k * min(A)


if __name__ == "__main__":

    test_cases = [
        ([1, 2, 3, 4], 2),
        ([5, 10], 3),
        ([7, 7, 7], 5),
        ([1, 100], 1),
        ([2, 4, 6, 8], 10)
    ]

    sol = Solution()

    for A, k in test_cases:
        print("Array:", A)
        print("k =", k)
        print("Maximum Total Value:", sol.maxTotalValue(A, k))
        print("-" * 40)