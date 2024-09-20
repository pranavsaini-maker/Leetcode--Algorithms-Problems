"""
PROBLEM:
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

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

#SOLUTION:
class Solution:
    def isValid(self, s: str) -> bool:
        brac_map = {')': '(', '}': '{', ']': '['}

        stack = []

        for char in s:
            if char in brac_map:
                top_ele = stack.pop() if stack else '#'

                if brac_map[char] != top_ele:
                    return False

            else:
                stack.append(char)

        return not stack 
