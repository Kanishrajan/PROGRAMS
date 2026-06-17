def findLargestOddSubstring(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i + 1]
    return "-1"


if __name__ == "__main__":

    test_cases = [
        "52",
        "4206",
        "35427",
        "13579",
        "2468",
        "1001"
    ]

    for num in test_cases:
        print("Input:", num)
        print("Largest Odd Substring:", findLargestOddSubstring(num))
        print("-" * 45)
