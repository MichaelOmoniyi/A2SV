class Solution:    
    def findUnion(self, a, b):
        # code here
        arrayUnion = set()
        
        for i in range(len(a)):
            arrayUnion.add(a[i])
            
        for j in range(len(b)):
            arrayUnion.add(b[j])
        
        return arrayUnion