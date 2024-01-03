class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        def helper(open_count, close_count, curr_str, n):
            if len(curr_str) == 2*n:
                ans.append(curr_str)
                return
            if open_count < n:
                helper(open_count + 1, close_count, curr_str + '(', n)
            if open_count > close_count:
                helper(open_count, close_count + 1, curr_str + ')', n)

        ans = []
        helper(0, 0, '', n)
        return ans
