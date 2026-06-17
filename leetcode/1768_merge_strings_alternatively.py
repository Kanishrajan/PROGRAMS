class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = []

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                r.append(word1[i])

            if i < len(word2):
                r.append(word2[i])

        return "".join(r)


if __name__ == "__main__":

    test_cases = [
        ("abc", "pqr"),
        ("ab", "pqrs"),
        ("abcd", "pq"),
        ("a", "xyz"),
        ("hello", "world")
    ]

    sol = Solution()

    for word1, word2 in test_cases:
        print("word1 =", word1)
        print("word2 =", word2)
        print("Merged =", sol.mergeAlternately(word1, word2))
        print("-" * 40)
