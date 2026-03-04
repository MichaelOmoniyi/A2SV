class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        
        # Pair each score with its original index
        scoreWithIndex = [(s, i) for i, s in enumerate(score)]
        
        # Sort by score descending
        scoreWithIndex.sort(reverse=True)
        
        result = [""] * n
        
        for rank, (s, index) in enumerate(scoreWithIndex):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)
        
        return result