from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        mi=[]
        for i in range(len(nums)-k+1):
            cd=nums[i+k-1]-nums[i]
            mi.append(cd)
        return min(mi)


if __name__ == "__main__":

    test_cases = [
        ([9,4,1,7], 2),
        ([90], 1),
        ([1,5,6,14,15], 3),
        ([3,8,2,10,15], 2),
        ([7,7,7,7], 2)
    ]

    sol = Solution()

    for nums, k in test_cases:
        print("Array:", nums)
        print("k =", k)
        print("Minimum Difference:", sol.minimumDifference(nums, k))
        print("-"*45)