# 1021. Remove Outermost Parentheses - Leet Code
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        count = 0
        for i in s:
            if i == '(':
                count += 1
                if count > 1:
                    ans.append(i)
            elif i == ')':
                count -= 1
                if count > 0:
                    ans.append(i)
        return ''.join(ans)    