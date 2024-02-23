class Solution(object):
    def is_valid_parentheses(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

solution = Solution()
print(solution.is_valid_parentheses("(){}[]"))  
print(solution.is_valid_parentheses("([)]"))
