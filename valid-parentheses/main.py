"""
Time: O(n)
Space: O(n)
"""
class Solution:
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
            if c in dic: stack.append(c)
            # if not, we check if matching closing pair in dict
            elif dic[stack.pop()] != c: return False
        return len(stack) == 1

s = Solution()
s_input = "()[]{}"
print(s.is_valid_parentheses2(s_input))
