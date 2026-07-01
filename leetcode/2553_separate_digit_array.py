from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
            s=str(i)
            for j in s:
                result.append(int(j))
        return result


if __name__ == "__main__":

    test_cases = [
        [13,25,83,77],
        [7,1,3,9],
        [100,20],
        [5],
        [12345]
    ]

    sol = Solution()

    for nums in test_cases:
        print("Input:", nums)
        print("Separated Digits:", sol.separateDigits(nums))
        print("-"*40)