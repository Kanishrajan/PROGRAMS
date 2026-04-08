class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        r = len(nums) - k
        
        new = nums[0:r]
        nums[0:r] = []
        nums.extend(new)


# Main function
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = [
        ([1,2,3,4,5,6,7], 3),
        ([-1,-100,3,99], 2),
        ([1,2], 1),
        ([1], 0)
    ]

    for nums, k in test_cases:
        print(f"Original: {nums}, k = {k}")
        sol.rotate(nums, k)
        print(f"Rotated:  {nums}")
        print("-" * 30)