class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        x = hour + minutes / 60
        diff = (11 * x) % 12
        return min(diff, 12 - diff) * 30


if __name__ == "__main__":

    test_cases = [
        (12, 30),
        (3, 30),
        (6, 0),
        (9, 45),
        (1, 57)
    ]

    sol = Solution()

    for hour, minutes in test_cases:
        print("Time:", f"{hour}:{minutes:02d}")
        print("Angle:", sol.angleClock(hour, minutes))
        print("-" * 40)