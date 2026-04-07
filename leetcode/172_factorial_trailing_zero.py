class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        d = 5
        while n >= d:
            count += n // d
            d *= 5
        return count


# Main function
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = [3, 5, 10, 25, 50, 100]

    for n in test_cases:
        result = sol.trailingZeroes(n)
        print(f"n = {n} -> Trailing Zeroes in {n}! = {result}")