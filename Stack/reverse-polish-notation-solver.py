class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        i = 0
        while i < n:

            if tokens[i] not in ['+', '-', '*', '/']:
                stack = stack + [int(tokens[i])]
            elif tokens[i] == '+':
                ans = stack[-1]+stack[-2]
                stack = stack[:-2]
                stack = stack + [int(ans)]
            elif tokens[i] == '-':
                ans = stack[-2]-stack[-1]
                stack = stack[:-2]
                stack = stack + [int(ans)]
            elif tokens[i] == '*':
                ans = stack[-1]*stack[-2]
                stack = stack[:-2]
                stack = stack + [int(ans)]
            elif tokens[i] == '/':
                ans = math.ceil(stack[-2]/stack[-1]) if stack[-1] * \
                    stack[-2] < 1 else math.floor(stack[-2]/stack[-1])
                stack = stack[:-2]
                stack = stack + [int(ans)]
            else:
                throw

            i = i + 1
        return stack[0]
