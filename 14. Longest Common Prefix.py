'''
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in range(len(strs)-1):
            j=len(strs[i])
            while j>= 0:
                if not strs[i+1].startswith(word[0:j]):
                    j-=1
                else: 
                    word = word[0:j]
                    break
            if not word or j == -1:
                return ""
        return word  

