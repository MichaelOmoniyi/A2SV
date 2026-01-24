class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        intRange = [value for value in range(left, right + 1)]

        for integer in intRange:
            intervalFound = True
            for interval in ranges:
                if interval[0] <= integer and interval[1] >= integer:
                    intervalFound = True
                    break
                else:
                    intervalFound = False

            if intervalFound == False:
                return False

        return True