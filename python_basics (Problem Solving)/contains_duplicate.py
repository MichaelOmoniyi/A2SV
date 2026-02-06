class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        unique = {}

        for num in nums:
            unique[num] = unique.get(num, 0) + 1

            if unique[num] > 1:
                return True
        return False