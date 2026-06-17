def reverseWords(s: str) -> str:
    s = s.strip().split()[::-1]
    return " ".join(s)


if __name__ == "__main__":

    test_cases = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
        "Bob Loves Alice",
        "single"
    ]

    for s in test_cases:
        print("Original:", repr(s))
        print("Reversed:", reverseWords(s))
        print("-" * 45)
