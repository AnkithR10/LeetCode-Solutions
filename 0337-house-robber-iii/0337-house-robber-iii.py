# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rob(self, root):
        """:type root: Optional[TreeNode]

        :rtype: int
        """
        # Helper function returns a pair: (max money if we rob this node, max money if we skip this node)
        def dfs(node):
            if not node:
                return (0, 0)
            
            # Recurse down to left and right subtrees
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            
            # Option 1: Rob this node (cannot rob its direct children)
            rob_current = node.val + left_skip + right_skip
            
            # Option 2: Skip this node (can choose whether to rob or skip children)
            skip_current = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (rob_current, skip_current)

        # The final answer is the maximum of robbing or skipping the root
        return max(dfs(root))