# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

# Example 1:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
# Example 2:

# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
# Example 3:

# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.
 

# Constraints:

# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 and s2 consist of only lowercase English letters.

# First Solution
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        swapCount = 0
        pos1, pos2 = -1, -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if pos1 == -1:
                    pos1 = i
                elif pos2 == -1:
                    pos2 = i
                swapCount += 1
        
        return swapCount == 2 and s1[pos1] == s2[pos2] and s1[pos2] == s2[pos1]

# Second Solution
class Solution2:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        swapCount = [] # stores a tuple of characters that are not the same at a particular indicies

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swapCount.append((s1[i], s2[i]))

        return len(swapCount) == 2 and swapCount[0] == swapCount[1][::-1]