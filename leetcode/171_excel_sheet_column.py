class Solution(object):
    def titleToNumber(self, columnTitle):
        ans = 0
        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord('A') + 1)
        return ans

if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = ["A", "Z", "AA", "AB", "ZY", "FXSHRXW"]

    for case in test_cases:
        result = sol.titleToNumber(case)
        print(f"Column Title: {case} -> Number: {result}")