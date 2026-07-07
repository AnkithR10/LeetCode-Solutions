class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: if the string length is 2*n, it's complete
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Choice 1: Add '(' if we haven't used all n yet
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
            
            # Choice 2: Add ')' if it's valid (i.e., fewer closed than open)
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result