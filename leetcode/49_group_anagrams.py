class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in d:
                d[key] = []
            d[key].append(word)

        return list(d.values())


if __name__ == "__main__":

    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
        ["abc","bca","cab","dog","god"]
    ]

    sol = Solution()

    for strs in test_cases:
        print("Input:", strs)
        result = sol.groupAnagrams(strs)
        print("Grouped Anagrams:", result)
        print("-"*40)