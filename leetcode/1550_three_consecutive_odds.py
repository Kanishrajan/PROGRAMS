class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr)-2):
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                return True
        return False


if __name__ == "__main__":

    test_cases = [
        [2,6,4,1],
        [1,2,34,3,4,5,7,23,12],
        [1,3,5],
        [2,4,6,8],
        [7,9,11,2]
    ]

    sol = Solution()

    for arr in test_cases:
        print("Array:", arr)
        print("Three consecutive odds exist:", sol.threeConsecutiveOdds(arr))
        print("-"*40)