class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        prime=[True]*n
        prime[0]=prime[1]=False
        for i in range(2,n):
            if prime[i]:
                for j in range(2*i,n,i):
                    prime[j]=False
        return sum(prime)


if __name__ == "__main__":

    test_cases = [0, 1, 2, 10, 20, 50]

    sol = Solution()

    for n in test_cases:
        print("n =", n)
        print("Number of primes less than n:", sol.countPrimes(n))
        print("-"*30)