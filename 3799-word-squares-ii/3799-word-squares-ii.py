class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        results = []
        n = len(words)
        
        # We need to pick 4 distinct words: top, left, right, bottom
        # Use nested loops (or backtracking) to pick 4 distinct words
        for i in range(n):
            for j in range(n):
                if i == j: continue
                for k in range(n):
                    if k == i or k == j: continue
                    for l in range(n):
                        if l == i or l == j or l == k: continue
                        
                        top = words[i]
                        left = words[j]
                        right = words[k]
                        bottom = words[l]
                        
                        # Check constraints
                        if (top[0] == left[0] and top[3] == right[0] and
                            bottom[0] == left[3] and bottom[3] == right[3]):
                            results.append([top, left, right, bottom])
        
        # Sort results lexicographically as required
        return sorted(results)