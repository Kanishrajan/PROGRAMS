class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


if __name__ == "__main__":

    test_cases = [
        ("abc", "ahbgdc"),
        ("axc", "ahbgdc"),
        ("", "ahbgdc"),
        ("ace", "abcde"),
        ("aec", "abcde")
    ]

    sol = Solution()

    for s, t in test_cases:
        print("s =", s)
        print("t =", t)
        print("Is Subsequence:", sol.isSubsequence(s, t))
        print("-" * 40)