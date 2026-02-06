class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to map each number to its index in the list
        numsDict = {}

        # Store each number with its index
        for i in range(len(nums)):
            numsDict[nums[i]] = i # If duplicates exist, the latest index overwrites the previous index

        # Check if the number complement exist
        for j in range(len(nums)):
            complement = target - nums[j]

            # Checks if complement exists in the dictionary and not the same index
            if complement in numsDict and numsDict[complement] != j: 
                    return [j, numsDict[complement]]