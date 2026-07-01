class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['A','a','E','e','I','i','O','o','U','u']
        p = []

        s = list(s)

        for ch in s:
            if ch in v:
                p.append(ch)

        for i in range(len(s)):
            if s[i] in v:
                s[i] = p.pop()

        return "".join(s)


if __name__ == "__main__":

    test_cases = [
        "hello",
        "leetcode",
        "aA",
        "IceCreAm",
        "race car"
    ]

    sol = Solution()

    for s in test_cases:
        print("Original:", s)
        print("After Reversing Vowels:", sol.reverseVowels(s))
        print("-" * 45)