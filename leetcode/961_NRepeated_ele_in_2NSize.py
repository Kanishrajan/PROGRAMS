from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(len(A)-2):
            if A[i]==A[i+1] or A[i]==A[i+2]:
                return A[i]
        return A[-1]


if __name__ == "__main__":

    test_cases = [
        [1,2,3,3],
        [2,1,2,5,3,2],
        [5,1,5,2,5,3,5,4],
        [9,5,6,9],
        [7,7,1,2]
    ]

    sol = Solution()

    for arr in test_cases:
        print("Array:", arr)
        print("Repeated N Times:", sol.repeatedNTimes(arr))
        print("-"*40)