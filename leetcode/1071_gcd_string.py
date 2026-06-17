from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 != str2 + str1):
            return ""
        return str1[:gcd(len(str1), len(str2))]


if __name__ == "__main__":

    test_cases = [
        ("ABCABC", "ABC"),
        ("ABABAB", "ABAB"),
        ("LEET", "CODE"),
        ("AAAAAA", "AAA"),
        ("XYZXYZXYZ", "XYZXYZ")
    ]

    sol = Solution()

    for str1, str2 in test_cases:
        print("str1 =", str1)
        print("str2 =", str2)
        print("GCD String =", sol.gcdOfStrings(str1, str2))
        print("-" * 45)
