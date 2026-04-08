from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in image:
            i.reverse()
            res.append([x ^ 1 for x in i])
        return res


# Main function
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = [
        [[1,1,0],[1,0,1],[0,0,0]],
        [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    ]

    for img in test_cases:
        print("Original:")
        for row in img:
            print(row)
        
        result = sol.flipAndInvertImage(img)

        print("\nFlipped & Inverted:")
        for row in result:
            print(row)
        print("-" * 40)