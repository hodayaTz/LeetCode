'''
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        bracket = {"(":")", "[":"]", "{":"}"}
        print('(')
        while i < len(s):
            if s[i] in bracket:
                stack.append(s[i])
            elif s[i] in bracket.values():
                if not stack or not stack.pop() == list(bracket.keys())[
                    list(bracket.values()).index(s[i])]:
                    return False
            i+=1
        if stack:
            return False
        return True

