# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

# Examples:

# Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
# Output: false
# Explanation: b[] is not a subset of a[]
# Constraints:
# 1 <= a.size(), b.size() <= 105
# 1 <= a[i], b[j] <= 106

#User function Template for python3

class Solution:
    #Function to check if b is a subset of a.
    def isSubset(self, a, b):
        # Your code here
        
        aCount = {}
        
        for i in range(len(a)):
            aCount[a[i]] = aCount.get(a[i], 0) + 1
            
        for j in range(len(b)):
            if aCount.get(b[j]):
                if aCount.get(b[j]) > 0:
                    aCount[b[j]] = aCount.get(b[j]) - 1
                else:
                    return False
            else:
                return False
                
        return True