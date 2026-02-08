# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commonDict = {}
        
        # Count the number of chars in the first word
        for char in words[0]:
            commonDict[char] = commonDict.get(char, 0) + 1

        # Compare count with the rest of the words
        for word in words[1:]:
            tempDict = {}

            for char in word:
                tempDict[char] = tempDict.get(char, 0) + 1

            # Ensure chars exit in commonDict and keep minimum count
            to_delete = []
            for char in commonDict:
                if char in tempDict:
                    commonDict[char] = min(commonDict[char], tempDict[char])
                else:
                    to_delete.append(char)
                
            for char in to_delete:
                del commonDict[char]
            
        common = []
        for char, count in commonDict.items():
            common.extend([char] * count)
        return common