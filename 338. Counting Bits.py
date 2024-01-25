class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # Use the previously computed values to determine the count of 1's in the binary representation of i
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
