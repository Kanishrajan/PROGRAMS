class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])

        return " ".join(res)


if __name__ == "__main__":

    test_cases = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
        "Bob Loves Alice",
        "single"
    ]

    sol = Solution()

    for s in test_cases:
        print("Original:", repr(s))
        print("Reversed:", sol.reverseWords(s))
        print("-" * 40)
