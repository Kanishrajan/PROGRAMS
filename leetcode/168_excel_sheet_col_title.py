class Solution(object):
    def convertToTitle(self, cn):
        p=""
        while cn>0:
            p=chr(ord('A')+(cn-1)%26)+p
            cn=(cn-1)//26
        return p


if __name__ == "__main__":

    test_cases = [1, 26, 27, 28, 52, 701, 702]

    sol = Solution()

    for n in test_cases:
        print("Column Number:", n)
        print("Excel Column Title:", sol.convertToTitle(n))
        print("-"*30)