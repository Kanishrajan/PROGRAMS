from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        prev=1
        for i in range(1,rowIndex+1):
            next_val=prev*(rowIndex-i+1)//i
            res.append(next_val)
            prev=next_val
        return res


if __name__ == "__main__":

    test_cases = [0, 1, 3, 4, 5]

    sol = Solution()

    for n in test_cases:
        print("Row Index:", n)
        print("Pascal Row:", sol.getRow(n))
        print("-"*30)