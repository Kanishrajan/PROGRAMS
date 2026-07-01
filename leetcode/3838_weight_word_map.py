from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        r=""
        for i in words:
            s=0
            for j in i:
                s+=weights[ord(j)-ord('a')]
            s%=26
            r+=chr(ord('z')-s)
        return r


if __name__ == "__main__":

    weights = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25, 26
    ]

    test_cases = [
        ["abc", "de"],
        ["hello", "world"],
        ["a", "z"],
        ["leetcode"],
        ["cat", "dog", "bird"]
    ]

    sol = Solution()

    for words in test_cases:
        print("Words:", words)
        print("Result:", sol.mapWordWeights(words, weights))
        print("-" * 40)