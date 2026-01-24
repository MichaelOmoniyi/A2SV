#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
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