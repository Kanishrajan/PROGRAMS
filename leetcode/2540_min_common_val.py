from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1,p2=0,0
        n1,n2=len(nums1),len(nums2)
        while p1<n1 and p2<n2:
            if nums1[p1]==nums2[p2]:
                return nums1[p1]
            elif nums1[p1]<nums2[p2]:
                p1+=1
            else:
                p2+=1
        return -1


if __name__ == "__main__":

    test_cases = [
        ([1,2,3], [2,4]),
        ([1,2,3,6], [2,3,4,5]),
        ([1,2,3], [4,5,6]),
        ([5,6,7], [1,2,5]),
        ([1], [1])
    ]

    sol = Solution()

    for nums1, nums2 in test_cases:
        print("nums1:", nums1)
        print("nums2:", nums2)
        print("Smallest Common Element:", sol.getCommon(nums1, nums2))
        print("-"*45)