class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        # Mapping based on telephone keypad
        letter_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        combinations = []

        def backtrack(index, current_string):
            # Base case: we've built a combination of the same length as digits
            if index == len(digits):
                combinations.append(current_string)
                return

            # Fetch letters for the current digit
            letters = letter_map[digits[index]]
            
            # Recurse for each letter
            for char in letters:
                backtrack(index + 1, current_string + char)

        backtrack(0, "")
        return combinations