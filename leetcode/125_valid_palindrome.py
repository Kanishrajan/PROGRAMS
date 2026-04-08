class Solution(object):
    def isPalindrome(self, s):
        a = ''
        s = s.lower()
        for i in s:
            if i.isalnum():
                a += i
        return a == a[::-1]


if __name__ == "__main__":

    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "Madam",
        "No lemon, no melon"
    ]

    sol = Solution()

    for s in test_cases:
        print("Input:", s)
        print("Is Palindrome:", sol.isPalindrome(s))
        print("-"*40)