from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elementCount = Counter(nums)        
        ans = []

        for num in elementCount:
            if elementCount[num] > (len(nums) / 3):
                ans.append(num)
        return ans