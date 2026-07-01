class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0

        for c in s:
            if c == '*':
                length = max(0, length - 1)
            elif c == '#':
                length *= 2
            elif c != '%':
                length += 1

        if k >= length:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c == '*':
                length += 1

            elif c == '#':
                half = length // 2
                if k >= half:
                    k -= half
                length = half

            elif c == '%':
                k = length - 1 - k

            else:
                if k == length - 1:
                    return c
                length -= 1

        return '.'


if __name__ == "__main__":

    test_cases = [
        ("a#b%*", 0),
        ("a#b%*", 1),
        ("abc", 2),
        ("abc#", 4),
        ("ab%c", 1),
        ("x#y#", 3)
    ]

    sol = Solution()

    for s, k in test_cases:
        print("String:", s)
        print("k =", k)
        print("Character:", sol.processStr(s, k))
        print("-" * 45)