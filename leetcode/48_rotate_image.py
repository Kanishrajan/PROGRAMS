from typing import List

class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        t = list(zip(*m))
        for i in range(len(m)):
            m[i] = list(t[i])[::-1]


if __name__ == "__main__":
    
    test_cases = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
        [[1]]
    ]

    sol = Solution()

    for matrix in test_cases:
        print("Original Matrix:")
        for row in matrix:
            print(row)

        sol.rotate(matrix)

        print("\nRotated Matrix:")
        for row in matrix:
            print(row)
        
        print("-"*30)