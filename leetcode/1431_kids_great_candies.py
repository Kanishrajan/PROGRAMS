from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r = []
        mx = max(candies)

        for i in candies:
            r.append(i + extraCandies >= mx)

        return r


if __name__ == "__main__":

    test_cases = [
        ([2,3,5,1,3], 3),
        ([4,2,1,1,2], 1),
        ([12,1,12], 10),
        ([1,2,3], 0),
        ([5], 5)
    ]

    sol = Solution()

    for candies, extraCandies in test_cases:
        print("Candies:", candies)
        print("Extra Candies:", extraCandies)
        print("Result:", sol.kidsWithCandies(candies, extraCandies))
        print("-" * 45)
