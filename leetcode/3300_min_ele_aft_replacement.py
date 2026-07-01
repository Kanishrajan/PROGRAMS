from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            s = 0
            while i > 0:
                s += i % 10
                i //= 10
            arr.append(s)
        return min(arr)


if __name__ == "__main__":

    test_cases = [
        [10,12,13,14],
        [99,88,77],
        [1,2,3],
        [123,456,789],
        [1000,2000,3000]
    ]

    sol = Solution()

    for nums in test_cases:
        print("Array:", nums)
        print("Minimum Digit Sum:", sol.minElement(nums))
        print("-"*40)