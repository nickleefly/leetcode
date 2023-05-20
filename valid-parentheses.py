"""
Time: O(n)
Space: O(n)
"""


class Solution:
    """
    Declare a character stack temp.
    Now traverse the string exp.
    * If the current character is a starting bracket ( or { or [ then push it to stack.
    * If the current character is a closing bracket  ( or } or ] then pop from stack and if the popped character is the matching starting bracket then fine else brackets are Not Balanced.
    After complete traversal, if there is some starting bracket left in stack then Not balanced , else Balanced.
    """
    def areBracketsBalanced(expr):
        stack = []

        # Traversing the Expression
        for char in expr:
            if char in ["(", "{", "["]:
                # Push the element in the stack
                stack.append(char)
            else:
                # If current character is not opening
                # bracket, then it must be closing.
                # So stack cannot be empty at this point.
                if not stack:
                    return False
                current_char = stack.pop()
                # print('current_char is %s, char is %s' % (current_char, char))
                if current_char == '(':
                    if char != ")":
                        return False
                if current_char == '{':
                    if char != "}":
                        return False
                if current_char == '[':
                    if char != "]":
                        return False

        # Check Empty Stack, in this case all matching
        if stack:
            return False
        return True

    def is_valid_parentheses(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            # print('\n')
            # print("ch is %s, ch in pairs %s" % (ch, ch in pairs))

            # when its right parentheses, we check if top of stack matching with current
            # if not matching return False
            # if matching we pop out left parentheses from stack
            if ch in pairs:
                # print('stack is ', stack)
                # print('stack[-1] is %s pairs["%s"] is %s' % (stack[-1], ch, pairs[ch]))
                # check if stack is empty or stack last element is pairs matching key/value pair
                if not stack or stack[-1] != pairs[ch]:
                    return False
                # if matching we pop out the character from stack
                stack.pop()
                # print('stack after pop', stack)
            else:
                # we put left parentheses in stack
                stack.append(ch)
                # print('stack after append', stack)
        return not stack

    """

    """

    def is_valid_parentheses2(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            # left parentheses put in to stack
            if c in dic:
                stack.append(c)
            # if not, we check if matching closing pair in dict
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


s = Solution()
s_input = "()[]{}"
print(s.is_valid_parentheses2(s_input))
