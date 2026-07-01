class Solution:
    def processStr(self, s: str) -> str:
        ans = ""

        for x in s:
            if x == '*':
                ans = ans[:-1]

            elif x == '#':
                ans += ans

            elif x == '%':
                ans = ans[::-1]

            else:
                ans += x

        return ans


if __name__ == "__main__":

    test_cases = [
        "a#b%*",
        "abc",
        "a#",
        "ab*",
        "ab%c",
        "x#y#",
        "*abc"
    ]

    sol = Solution()

    for s in test_cases:
        print("Input :", s)
        print("Output:", sol.processStr(s))
        print("-" * 40)