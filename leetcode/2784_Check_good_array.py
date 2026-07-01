from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx=max(nums)
        if len(nums)!=mx+1:
            return False
        fr=[0]*(mx+1)
        for x in nums:
            if x<1 or x>mx:
                return False
            fr[x]+=1
        for i in range(1,mx):
            if fr[i]!=1:
                return False
        return fr[mx]==2


if __name__ == "__main__":

    test_cases = [
        [2,1,3],
        [1,3,3,2],
        [1,1],
        [3,4,4,1,2],
        [1,2,2,3]
    ]

    sol = Solution()

    for nums in test_cases:
        print("Array:", nums)
        print("Is Good:", sol.isGood(nums))
        print("-"*40)