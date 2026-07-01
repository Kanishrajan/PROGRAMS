class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)


if __name__ == "__main__":

    test_cases = [
        ("abcde", "cdeab"),
        ("abcde", "abced"),
        ("aaaa", "aaaa"),
        ("waterbottle", "erbottlewat"),
        ("hello", "llohe")
    ]

    sol = Solution()

    for s, goal in test_cases:
        print("s =", s)
        print("goal =", goal)
        print("Can Rotate:", sol.rotateString(s, goal))
        print("-"*40)