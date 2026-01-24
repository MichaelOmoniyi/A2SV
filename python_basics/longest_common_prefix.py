class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = strs[0]

        prefixLen = len(prefix)

        for words in strs[1:]:
            while prefixLen >= 0 and prefixLen:
                if prefix == words[:prefixLen]:
                    break
                prefixLen -= 1
                prefix = prefix[:prefixLen]
        
        return prefix