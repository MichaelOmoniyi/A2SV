class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiple = 2 * n

        if n % 2 == 0:
            return(min(n, multiple))
        else:
            return multiple