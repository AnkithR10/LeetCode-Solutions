class Solution:
    def maxLength(self, arr):
        self.max_len = 0
        
        def backtrack(index, current_str):
            if len(set(current_str)) != len(current_str):
                return
            
            self.max_len = max(self.max_len, len(current_str))
            
            for i in range(index, len(arr)):
                backtrack(i + 1, current_str + arr[i])
        
        backtrack(0, "")
        return self.max_len