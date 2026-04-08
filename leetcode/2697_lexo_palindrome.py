class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans,n=list(s),len(s)
        for i in range(n//2):
            ans[i]=ans[n-i-1]=min(ans[i],ans[n-i-1])
        return ''.join(ans)


if __name__ == "__main__":
    
    test_cases = [
        "egcfe",
        "abcd",
        "seven",
        "race",
        "a"
    ]

    sol = Solution()

    for s in test_cases:
        print("Original:", s)
        result = sol.makeSmallestPalindrome(s)
        print("Smallest Palindrome:", result)
        print("-"*30)