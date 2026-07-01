from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        return nums


if __name__ == "__main__":

    test_cases = [
        [0,1,0,3,12],
        [0],
        [1,2,3],
        [0,0,1],
        [4,0,5,0,0,3,1]
    ]

    sol = Solution()

    for nums in test_cases:
        print("Original:", nums)

        result = sol.moveZeroes(nums[:])

        print("After Moving Zeroes:", result)
        print("-" * 45)