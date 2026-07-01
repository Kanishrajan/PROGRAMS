from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, a: List[int]) -> bool:
        a.sort()
        for i in a:
            if mass < i:
                return False
            mass += i
        return True


if __name__ == "__main__":

    test_cases = [
        (10, [3,9,19,5,21]),
        (5, [4,9,23,4]),
        (1, [1]),
        (20, [1,2,3,4]),
        (7, [8,1,2])
    ]

    sol = Solution()

    for mass, asteroids in test_cases:
        print("Initial Mass:", mass)
        print("Asteroids:", asteroids)
        print("Can Destroy All:", sol.asteroidsDestroyed(mass, asteroids))
        print("-"*45)