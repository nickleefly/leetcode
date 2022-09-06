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
                stack.append(ch)
                # print('stack after append', stack)
        return not stack

s = Solution()
s_input = "()[]{}"
print(s.is_valid_parentheses(s_input))
